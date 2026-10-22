
from fastapi import FastAPI, HTTPException
import sqlite3

from database import get_connection, create_table
from schemas import StudentCreate, StudentUpdate

app = FastAPI(title="Student Database CRUD API")

# Create the students table when the application starts
create_table()

@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            INSERT INTO students (name, dob, email, phone, course, address)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                student.name,
                student.dob.isoformat(),
                student.email,
                student.phone,
                student.course,
                student.address,
            ),
        )

        connection.commit()
        student_id = cursor.lastrowid

        new_student = connection.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()

        return dict(new_student)

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="A student with this email already exists.",
        )

    finally:
        connection.close()
    

# Get all students, with optional search and filtering
@app.get("/students")
def get_all_students(
    name: str | None = None,
    course: str | None = None,
):
    connection = get_connection()

    try:
        query = "SELECT * FROM students WHERE 1=1"
        parameters = []

        if name:
            query += " AND name LIKE ?"
            parameters.append(f"%{name}%")

        if course:
            query += " AND course LIKE ?"
            parameters.append(f"%{course}%")

        query += " ORDER BY id"

        students = connection.execute(
            query,
            parameters,
        ).fetchall()

        return [dict(student) for student in students]

    finally:
        connection.close()



# Get one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    connection = get_connection()

    try:
        student = connection.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found.",
            )

        return dict(student)

    finally:
        connection.close()
    
# Update an existing student
@app.patch("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    updates = student.model_dump(exclude_unset=True)

    if not updates:
        raise HTTPException(
            status_code=400,
            detail="Provide at least one field to update.",
        )

    for field in ("name", "dob", "email"):
        if field in updates and updates[field] is None:
            raise HTTPException(
                status_code=422,
                detail=f"{field} cannot be empty.",
            )

    if "dob" in updates and updates["dob"] is not None:
        updates["dob"] = updates["dob"].isoformat()

    connection = get_connection()

    try:
        existing = connection.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()

        if existing is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found.",
            )

        set_clause = ", ".join(
            f"{field} = ?" for field in updates
        )
        values = list(updates.values()) + [student_id]

        try:
            connection.execute(
                f"UPDATE students SET {set_clause} WHERE id = ?",
                values,
            )
            connection.commit()

        except sqlite3.IntegrityError:
            raise HTTPException(
                status_code=409,
                detail="A student with this email already exists.",
            )

        updated = connection.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()

        return dict(updated)

    finally:
        connection.close()
    
# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    connection = get_connection()

    try:
        student = connection.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,),
        ).fetchone()

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found.",
            )

        connection.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,),
        )
        connection.commit()

        return {
            "message": "Student deleted successfully.",
            "student_id": student_id,
        }

    finally:
        connection.close()





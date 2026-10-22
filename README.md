# Student Database CRUD API

A lightweight REST API built with **Python, FastAPI, and SQLite** to manage student records through standard CRUD (Create, Read, Update, Delete) operations.

This project demonstrates practical backend development concepts, including REST API design, request validation, database integration, error handling, and search functionality.

## Overview

The Student Database CRUD API provides endpoints to create, retrieve, update, delete, and search student records. Student information is stored in an SQLite database, allowing records to persist between application runs.

The API includes input validation, duplicate email prevention, and appropriate error responses for common situations.

## Features Implemented

- **Create student records** with validated student information.
- **Retrieve student records** individually or as a complete list.
- **Update student information** using partial updates.
- **Delete student records** by their unique ID.
- **Search and filter students** by name, course, or both.
- **Validate input data** using Pydantic and email validation.
- **Prevent duplicate email addresses** through database constraints and error handling.
- **Handle common errors**, including missing records, duplicate emails, invalid input, and empty update requests.
- **Persist data** using SQLite.
- **Explore and test endpoints** through FastAPI's interactive Swagger UI.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11+ | Core programming language |
| FastAPI | REST API framework |
| SQLite | Database for persistent storage |
| Pydantic | Request data validation |
| Uvicorn | ASGI server |
| Email Validator | Email address validation |
| Swagger UI | Interactive API documentation and manual testing |

## Project Structure

```text
student_management/
├── main.py
├── database.py
├── schemas.py
├── requirements.txt
├── README.md
└── .gitignore
```

The `students.db` database file is created locally when the application runs. It is excluded from version control, so each fresh setup can generate its own database.

## Getting Started

### Prerequisites

- Python 3.11 or later
- pip
- Visual Studio Code or another code editor

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd student_management
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Start the API server

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Documentation

Once the server is running, open the interactive documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Swagger UI allows you to send requests to the API and inspect the responses directly from your browser.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/students` | Create a student |
| `GET` | `/students` | Retrieve all students |
| `GET` | `/students/{student_id}` | Retrieve a student by ID |
| `PATCH` | `/students/{student_id}` | Partially update a student |
| `DELETE` | `/students/{student_id}` | Delete a student |
| `GET` | `/students?name=Ananya` | Filter students by name |
| `GET` | `/students?course=B.Tech` | Filter students by course |
| `GET` | `/students?name=Ananya&course=B.Tech` | Combine name and course filters |

## Student Data Model

A student record can contain the following fields:

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Unique, automatically generated student ID |
| `name` | String | Student's name |
| `dob` | Date | Date of birth |
| `email` | String | Required, valid, unique email address |
| `phone` | String or null | Optional phone number |
| `course` | String or null | Optional course name |
| `address` | String or null | Optional address |

## Example API Request

### Create a student

**Request**

`POST /students`

```json
{
  "name": "Ananya Sharma",
  "dob": "2003-05-14",
  "email": "ananya.test@example.com",
  "phone": "9876543210",
  "course": "B.Tech",
  "address": "Patna, Bihar"
}
```

**Example response**

```json
{
  "id": 3,
  "name": "Ananya Sharma",
  "dob": "2003-05-14",
  "email": "ananya.test@example.com",
  "phone": "9876543210",
  "course": "B.Tech",
  "address": "Patna, Bihar"
}
```

The returned ID is illustrative and depends on the records already present in your database. Use a unique email address when testing creation requests.

### Search and filter students

Retrieve students whose names match a search term:

```http
GET /students?name=Ananya
```

Filter students by course:

```http
GET /students?course=B.Tech
```

Combine both filters:

```http
GET /students?name=Ananya&course=B.Tech
```

If no students match the supplied filters, the API returns an empty list.

## Error Handling

The API implements responses for common request and database errors.

| Status code | Meaning |
|---|---|
| `200 OK` | Request completed successfully |
| `201 Created` | Student record created successfully |
| `400 Bad Request` | Update request contains no fields to update |
| `404 Not Found` | Student record does not exist |
| `409 Conflict` | Email address already exists |
| `422 Unprocessable Entity` | Request data fails validation |

## Database and Persistence

The application uses SQLite to store student records. The database table is created automatically when the application starts, if it does not already exist.

The database logic is separated into `database.py`, while `schemas.py` defines the request validation models. The API routes and application logic are maintained in `main.py`.

This separation helps keep the project organized and easier to maintain.

## Testing and Verification

During development, the API was tested manually through FastAPI's Swagger UI.

The following functionality was tested:

- Creating and retrieving student records.
- Searching by student name and course.
- Applying name and course filters together.
- Returning an empty list when no records match.
- Handling duplicate email addresses.
- Testing CRUD operations during development.

**Testing note:** Automated unit and integration tests have not yet been added. The testing described above refers to manual API testing.

## Future Improvements

The current version focuses on the core student database API. Potential improvements include:

- Automated unit and integration tests using `pytest`.
- Pagination and sorting for larger student lists.
- Authentication and role-based authorization.
- A frontend interface for managing student records.
- Database migrations and additional database options.
- Deployment to a cloud platform.
- An optional AI-powered extension, if required by the project scope.

These are planned improvements and are not claimed as completed features.

## Conclusion

This project provides a practical foundation in backend development using Python, FastAPI, and SQLite. It demonstrates the implementation of CRUD operations, data validation, database persistence, search and filtering, and error handling through a structured REST API.

It also provides a foundation for extending the application with automated testing, authentication, and deployment in future iterations.
# FastAPI Configuration Management API

## Overview

This project implements a FastAPI-based API for managing configurations using SQLAlchemy with PostgreSQL as the database backend. It provides CRUD (Create, Read, Update, Delete) operations for configurations stored in the database.

## NOTE: Please checkout the master branch for the main code since the code on the other branch is deprecated.

## Screenshots

![image](https://github.com/DhruvDua1105/cogoport_backend/assets/86777191/e54ca903-f78f-4a2f-97db-7efe80b09bf9)
![image](https://github.com/DhruvDua1105/cogoport_backend/assets/86777191/60ab6cbf-1edf-4997-b21e-1515cca32f91)



## Project Structure

```plaintext
config_management/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── crud.py
    │   ├── database.py
    │   ├── models.py
    │   └── schemas.py
    ├── .env
    ├── requirements.txt
    └── .gitignore
```

- **app/**: Contains the main application files.
  - `main.py`: FastAPI application setup and endpoints.
  - `crud.py`: Implements CRUD operations using SQLAlchemy.
  - `database.py`: Configures the database connection and session management.
  - `models.py`: Defines SQLAlchemy ORM models for the application.
  - `schemas.py`: Defines Pydantic schemas for request and response validation.
- `.env`: Lists all the environment variables required for the project.
- `requirements.txt`: Lists all Python dependencies required for the project.

## Installation and Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7+
- PostgreSQL database (ensure `psycopg2` is installed)
- pip package manager

### Setup Instructions

1. **Clone the repository and navigate to the project directory:**

   ```bash
   git clone https://github.com/DhruvDua1105/cogoport_backend.git
   cd configurationManagement_dhruv
   ```
2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**

   ```bash
   pip install -r app/requirements.txt
   ```
   
4. **Database Configuration:**

Open .env and replace DATABASE_URL with your PostgreSQL connection URL:

   ```bash
   DATABASE_URL = "postgresql://your_username:your_password@localhost:5432/your_database_name"
   ```
5. **Start the FastAPI application:**

   ```bash
   uvicorn app.main:app --reload
   ```
The application will start, and you can access it at http://localhost:8000.

## Explore the API documentation:

Open your web browser and go to http://localhost:8000/docs to view the interactive API documentation (Swagger UI). Here, you can explore the available API endpoints, send requests, and view responses.


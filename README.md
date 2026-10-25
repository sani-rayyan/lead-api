# Lead API 

A clean, layered REST API for managing leads, built with FastAPI and SQLite.

## Features

- Full CRUD (create, read, update, delete)
- Input validation with pydantic (email format, phone digits only, minimum name length)
- Layered structure: routes, CRUD logic, schemas, database

## Setup
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to try the API.


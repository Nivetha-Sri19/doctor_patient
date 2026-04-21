FastAPI Doctor–Patient API

Project Overview

This is a simple REST API built using FastAPI to manage doctors and patients.
I created this project mainly to practice API design, request validation, and basic error handling.
The API lets you create and retrieve doctors and patients, and it uses in-memory storage, so it’s lightweight and easy to run.

Setup Instructions:

Clone the repository

Install dependencies:

pip install -r requirements.txt

Run the server:

python -m uvicorn app.main:app --reload

API Documentation:

Once the server is running, you can explore the API using Swagger UI:
http://127.0.0.1:8000/docs

Features:

Doctor APIs

  Create doctor

  Get all doctors

  Get doctor by ID


Patient APIs

  Create patient

  Get all patients


Request validation using Pydantic:

Error handling using HTTP exceptions

Simple in-memory data storage



Validation Rules

Email must be in a valid format

Age must be greater than 0


Error Handling

Invalid email → handled automatically by Pydantic

Invalid age → returns a proper error using HTTPException

Resource not found → returns a 404 response


Tech Stack

Python

FastAPI

Pydantic

Uvicorn


Notes


This project uses in-memory storage, so all data will be lost when the server restarts.

Built mainly for learning and practice purpose.


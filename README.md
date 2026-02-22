<<<<<<< HEAD

Healthcare Backend API
Run:
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Healthcare Backend API

This project is a healthcare backend system built using Django REST Framework and JWT authentication.

## Features

- User Registration
- JWT Authentication Login
- Patient Management (CRUD)
- Doctor Management (CRUD)
- Patient-Doctor Mapping

## Technologies Used
=======
# Healthcare-Backend
Healthcare Backend API built using Django REST Framework with JWT authentication. Supports user registration, login, patient management, doctor management, and patient-doctor mapping with secure RESTful endpoints.

# Healthcare Backend API (Django REST Framework)

This project is a secure and scalable Healthcare Backend API developed using Django REST Framework. It provides RESTful endpoints for user authentication, patient management, doctor management, and patient-doctor mapping.

The system uses JWT (JSON Web Token) authentication to ensure secure access and allows authenticated users to manage healthcare records efficiently.

This project was built as part of a Backend Developer assignment and follows best practices for API development, authentication, and database management.

---

## Key Features

- JWT-based user authentication (Register & Login)
- Patient management (Create, View, Update, Delete)
- Doctor management (Create, View, Update, Delete)
- Patient-Doctor mapping system
- Secure endpoints with authentication permissions
- RESTful API architecture
- Database integration using Django ORM
- Tested using Postman

---

## Tech Stack
>>>>>>> 37a3dee7fe3db833555116411233a9876f985b11

- Python
- Django
- Django REST Framework
<<<<<<< HEAD
- JWT Authentication
- SQLite (can be configured for PostgreSQL)
- Postman for API testing

## Installation

1. Clone repository

2. Create virtual environment
python -m venv venv

3. Activate environment
venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Run migrations
python manage.py migrate

6. Run server
python manage.py runserver

## API Endpoints

POST /api/auth/register/  
POST /api/auth/login/  

POST /api/patients/  
GET /api/patients/  

POST /api/doctors/  
GET /api/doctors/  

POST /api/mappings/  
GET /api/mappings/  


=======
- JWT Authentication (SimpleJWT)
- SQLite (can be configured with PostgreSQL)
- Postman (API Testing)
>>>>>>> 37a3dee7fe3db833555116411233a9876f985b11

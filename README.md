
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

- Python
- Django
- Django REST Framework
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



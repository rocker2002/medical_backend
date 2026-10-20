# Medical Backend

A robust Django REST API for managing medical records, doctors, patients, and appointment scheduling.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/Django-6.0.7-green?style=for-the-badge&logo=django" alt="Django" />
  <img src="https://img.shields.io/badge/DRF-3.17.1-red?style=for-the-badge&logo=django" alt="Django REST Framework" />
  <img src="https://img.shields.io/badge/PostgreSQL-15+-blue?style=for-the-badge&logo=postgresql" alt="PostgreSQL" />
</p>

## Overview

Medical Backend is a backend service built with Django and Django REST Framework to support a clinic or hospital workflow. It includes:

- Doctor management
- Patient record management
- Appointment booking and scheduling
- JWT-based authentication
- Role-aware access control
- Filtering for appointment queries

This project is designed to act as a clean API foundation for a frontend application or admin dashboard.

## Features

- Secure authentication with JSON Web Tokens
- Doctor and patient relationship modeling
- Appointment validation to prevent double-booking
- Protected routes and role-based authorization
- PostgreSQL-ready configuration
- Easy integration with frontend apps

## Project Structure

```text
medical_backend/
├── medical_backend/
│   ├── medical_backend/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── patients/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Tech Stack

- Python 3.12+
- Django 6.0.7
- Django REST Framework
- djangorestframework-simplejwt
- django-filter
- PostgreSQL
- python-dotenv

## Core Models

### Doctor
- ID (UUID)
- Name
- Specialization
- Email
- Active status

### Patient
- ID (UUID)
- Name
- Date of birth
- Contact details
- Assigned doctor

### Appointment
- ID (UUID)
- Patient
- Doctor
- Scheduled time
- Status
- Notes

### Profile
- User relationship
- Role selection:
  - Doctor
  - Patient
  - Receptionist

## Authentication

This API uses JWT authentication via `djangorestframework_simplejwt`.

### Token endpoints

- `POST /api/token/` — obtain JWT access and refresh tokens
- `POST /api/token/refresh/` — refresh access token

### API endpoints

- `GET /api/doctors/`
- `POST /api/doctors/`
- `GET /api/doctors/<id>/`
- `PUT /api/doctors/<id>/`
- `DELETE /api/doctors/<id>/`

- `GET /api/patients/`
- `POST /api/patients/`
- `GET /api/patients/<id>/`
- `PUT /api/patients/<id>/`
- `DELETE /api/patients/<id>/`

- `GET /api/appointments/`
- `POST /api/appointments/`
- `GET /api/appointments/<id>/`
- `PUT /api/appointments/<id>/`
- `DELETE /api/appointments/<id>/`

Appointments can be filtered by:

- `status`
- `doctor`

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.12+
- PostgreSQL
- pip
- virtualenv (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/rocker2002/medical_backend.git
cd medical_backend
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
# .venv\Scripts\activate   # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root or in the working environment with values similar to:

```env
SECRET_KEY=your_secret_key_here
DB_NAME=medical_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Create the database

Make sure PostgreSQL is running and create the database:

```sql
CREATE DATABASE medical_db;
```

### 6. Run migrations

```bash
python medical_backend/manage.py migrate
```

### 7. Start the development server

```bash
python medical_backend/manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/api/
```

## Admin Panel

Django admin is enabled and available at:

```text
http://127.0.0.1:8000/admin/
```

Create a superuser with:

```bash
python medical_backend/manage.py createsuperuser
```

## Validation Rules

The backend includes several validation checks:

- Appointment scheduled time must not be in the past
- A doctor cannot have two appointments at the exact same time
- Patient actions are restricted via custom permission logic

## Security Notes

- JWT authentication is enabled for API access
- Sensitive configuration is expected to be kept in environment variables
- `DEBUG` is currently enabled in the settings and should be disabled in production
- `ALLOWED_HOSTS` is set to `*` for local development convenience and should be tightened in deployment

## Future Enhancements

Potential next steps for this project include:

- Role-based dashboards for doctors and receptionists
- Appointment reminders via email or SMS
- Patient medical history tracking
- File uploads for prescriptions and reports
- Swagger/OpenAPI documentation
- CI/CD pipeline and automated tests

## License

This project does not currently include a license file. If you intend to publish or distribute it publicly, consider adding an appropriate open-source license.

## Contributing

Contributions are welcome. If you want to improve the API, add tests, or extend functionality:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## Contact

For questions or collaboration, use the repository's GitHub issues or contact the project maintainer.

---

Built with Django and designed for medical workflow automation.

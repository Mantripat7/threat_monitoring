+# Threat Monitoring & Alert Management Backend

## Overview
This project is a backend REST API built using Django and Django REST Framework for ingesting security events and automatically generating alerts based on severity.

The system is designed with a security-first mindset and supports role-based access control using JWT authentication.

## Features
- JWT-based authentication
- Role-based access (Admin, Analyst)
- Security event ingestion
- Automatic alert generation for High/Critical events
- Alert filtering and status management
- Optimized database queries
- Swagger API documentation

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite
- JWT (SimpleJWT)

## Setup Instructions
```bash
git clone <repo-url>
cd threat_monitoring
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
+++++++++++++++++++++++
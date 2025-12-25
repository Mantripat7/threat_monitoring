# Threat Monitoring & Alert Management Backend

This project is a backend REST API built using **Django + Django REST Framework** for ingesting security events and automatically generating alerts based on severity.

It is designed with a security-first mindset, supports role-based access control, and follows clean, production-oriented backend practices.
The system is designed with a security-first mindset and supports role-based access control using JWT authentication.


##   Features
- JWT authentication (access + refresh tokens)
- Role-based access (Admin / Analyst)
- Security event ingestion API
- Automatic alert generation for **High / Critical** events
- Alert filtering by severity & status
- Alert status updates (Admin only)
- Pagination, validation & permissions
- Swagger documentation
- Basic logging & throttling


## Tech Stack
- Django
- Django REST Framework
- SQLite
- JWT (SimpleJWT)
- drf-yasg (Swagger)

## Setup Instructions
 ```bash
git clone <https://github.com/Mantripat7/threat_monitoring.git>
cd threat_monitoring
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Testing
A Postman collection is included in the repository:
postman/Threat-Monitoring-API.postman_collection.json
It can be imported directly into Postman for testing all endpoints.
 

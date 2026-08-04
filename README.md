# Podcast Manager API

A RESTful backend API for managing podcasts and episodes built with Django REST Framework.

This project provides a backend service for podcast management, including user authentication, podcast data handling, and automatic parsing of RSS feeds to collect podcast information.

---

## Features

- JWT-based authentication
- User registration and login
- Podcast management API
- Episode management
- RSS feed parsing
- Automatic extraction of podcast information
- RESTful API architecture
- Docker and Docker Compose support
- SQLite database support (default)
- PostgreSQL compatibility

---

## Tech Stack

### Backend

- Python
- Django
- Django REST Framework

### Authentication

- JWT Authentication

### Database

- SQLite (Default)
- PostgreSQL (Supported)

### Parsing

- BeautifulSoup4

### Deployment

- Docker
- Docker Compose

---

## Project Overview

Podcast Manager API is designed to provide backend services for managing podcast content.

The system can parse podcast RSS feeds and extract available information such as podcast metadata and episode data, then store and manage them through REST APIs.

---

## Architecture

```

Client
|
|
REST API
|
Django REST Framework
|
Database
(SQLite / PostgreSQL)

RSS Feed
|
BeautifulSoup Parser
|
Podcast Data Processing
|
Database Storage

```

---

## Authentication

The project uses JWT authentication for securing API endpoints.

Authentication flow:

```

User Registration
|
|
User Login
|
|
JWT Token Generation
|
|
Authenticated API Requests

```

---

## Project Structure

```

podcast_manager/

├── apps/
│
├── serializers/
│
├── views/
│
├── models/
│
├── urls.py
│
├── settings.py
│
├── Dockerfile
│
├── docker-compose.yml
│
└── manage.py

````

---

## Installation

### Clone Repository

```bash
git clone https://github.com/nima-mojarradi/podcast_manager.git

cd podcast_manager
````

---

## Run With Docker

Build containers:

```bash
docker compose build
```

Run project:

```bash
docker compose up
```

The API will be available at:

```
http://localhost:8000
```

---

## Local Development

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

Run server:

```bash
python manage.py runserver
```

---

## Environment Variables

Create a `.env` file:

```
SECRET_KEY=your_secret_key
DEBUG=True
```



## RSS Parser

The project includes an RSS parsing module that extracts podcast information from RSS feeds.

Workflow:

```
RSS Feed URL

      ↓

BeautifulSoup Parser

      ↓

Data Extraction

      ↓

Database Storage

      ↓

REST API Access
```

---

## Future Improvements

* API documentation with Swagger/OpenAPI
* Background RSS synchronization using Celery
* Cloud media storage integration
* Automated testing
* Advanced search and filtering

---

## Author

Nima Mojarradi

GitHub:

[https://github.com/nima-mojarradi](https://github.com/nima-mojarradi)

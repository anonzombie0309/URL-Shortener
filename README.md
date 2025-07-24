# URL Shortener Service

## Overview

A simple URL shortening service inspired by bit.ly/tinyurl, built with Python and Flask as specified in the assignment. This project allows users to shorten URLs, redirect using a short code, and view analytics — all with in-memory storage and a clean API.

## Getting Started

### Prerequisites

- Python 3.8+  
- pip installed

### Setup

Clone/download this repository
git clone https://github.com/anonzombie0309/URL-shortener.git
```
cd url-shortener
```
Install dependencies
```
pip install -r requirements.txt
```
Start the application
```
python -m flask --app app.main run
```
The API will be available at http://localhost:5000
Run tests with:
pytest


## Features

- **Shorten any valid HTTP/HTTPS URL**
- **Redirection using a 6-character alphanumeric short code**
- **Click count and creation timestamp analytics**
- **In-memory data store (lost on server restart)**
- **Basic error handling and validation**
- **Modular code (separate files for models, utils, routes)**

## API Endpoints

### 1. Health Check

- **GET /**  
  Returns service status:

{
"status": "healthy",
"service": "URL Shortener API"
}

### 2. Shorten URL

- **POST /api/shorten**
- Request (JSON):

- Response (JSON):
{
"short_code": "abc123",
"short_url": "http://localhost:5000/abc123"

}

- Returns 400 on invalid input or missing URL.

### 3. Redirect

- **GET /<short_code>**
- Redirects to original URL and increments click count.
- Returns 404 and an error message if code does not exist.

### 4. Analytics

- **GET /api/stats/<short_code>**
- Response (JSON):
{
"url": "https://www.example.com/some/long/path",
"clicks": 5,
"created_at": "2025-07-24T10:00:00"

}

- Returns 404 if code not found.


## Error Handling

- 400 Bad Request for missing/invalid URL on POST
- 404 Not Found for invalid or missing short code
- All errors return meaningful JSON messages

## Testing

- Tests use `pytest` (see `tests/test_basic.py` for examples)
- To run tests from the project root:


## Notes & Limitations

- Data is stored **in-memory**: All codes and analytics reset if the server stops.
- **No web UI**, authentication, or custom short codes (per assignment).
- No external databases or rate limiting are implemented.

## Implementation Guidelines Met

- Clean, modular code and clear separation of concerns
- All endpoints and requirements from assignment README fulfilled
- Validates URLs and handles edge/error cases
- Supports multiple concurrent requests (Flask's default WSGI server)
- **No features beyond assignment requirements**


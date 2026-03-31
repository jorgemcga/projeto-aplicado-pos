# Health API

A minimal FastAPI application that provides a health check endpoint for monitoring API status and database connectivity.

## Overview

This project implements a simple REST API with a single endpoint that returns the operational status of the system. It's designed to be used for health checks in containerized deployments, load balancer monitoring, or service availability verification.

## Project Structure

```
.
├── spec/
│   └── api.yaml           # OpenAPI 3.0.3 specification
├── tests/
│   └── test_health.py     # Unit tests
├── main.py                # FastAPI application
├── CLAUDE.md              # Implementation details
└── README.md              # This file
```

## Technology Stack

- **Python**: 3.11
- **Framework**: FastAPI
- **ASGI Server**: Uvicorn
- **Specification**: OpenAPI 3.0.3

## Installation

1. **Create and activate virtual environment:**

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

2. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn requests pytest
   ```

## Running the Application

Start the development server:

```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check

- **Endpoint**: `GET /health`
- **Description**: Check if API is running and database is connected
- **Response (200 OK)**:
  ```json
  {
    "status": "running",
    "database": "connected"
  }
  ```

## API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Testing

Run the test suite:

```bash
pytest tests/
```

To run with verbose output:

```bash
pytest tests/ -v
```

## Development

The application supports hot-reload during development:

```bash
uvicorn main:app --reload
```

This will automatically restart the server when code changes are detected.

## License

MIT

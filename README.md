# File Manager API

A Django REST Framework-based file management system with JWT authentication. Users can create folders, upload files (PDF, JPG, JPEG, PNG), and manage their files securely.

## Features

- User registration and authentication using JWT tokens
- Create and manage folders
- Upload files (PDF, JPG, JPEG, PNG)
- Download files
- User-specific file and folder management
- RESTful API design

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd filemanager
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**On Linux/Mac:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Environment Variables Setup

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` file and set your configuration:
   - `SECRET_KEY`: Generate a new Django secret key (you can use `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
   - `DEBUG`: Set to `True` for development, `False` for production
   - `ALLOWED_HOSTS`: Comma-separated list of allowed hosts (e.g., `localhost,127.0.0.1,yourdomain.com`)

### 6. Database Migration

```bash
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication

- **POST** `/api/auth/register/` - Register a new user
  - Body: `{"username": "user123", "password": "password123"}`
  
- **POST** `/api/auth/login/` - Login and get JWT tokens
  - Body: `{"username": "user123", "password": "password123"}`
  - Response: `{"refresh": "...", "access": "..."}`

- **POST** `/api/auth/refresh/` - Refresh access token
  - Body: `{"refresh": "your_refresh_token"}`

### Folders

- **GET** `/api/folders/` - List all folders (requires authentication)
- **POST** `/api/folders/` - Create a new folder (requires authentication)
  - Body: `{"name": "My Folder"}`

### Files

- **GET** `/api/files/` - List all files (requires authentication)
- **POST** `/api/files/` - Upload a file (requires authentication)
  - Body: Form-data with `folder` (folder ID) and `file` (file to upload)
- **GET** `/api/files/<id>/download/` - Download a file (requires authentication)

## Authentication

All endpoints except registration and login require JWT authentication. Include the access token in the Authorization header:

```
Authorization: Bearer <your_access_token>
```

## File Upload Restrictions

Only the following file types are allowed:
- PDF (.pdf)
- JPEG (.jpg, .jpeg)
- PNG (.png)

## Postman Collection

Import the `postman_collection.json` file into Postman to test all API endpoints. The collection includes:
- Pre-configured requests for all endpoints
- Environment variables for easy token management
- Example requests and responses

## Project Structure

```
filemanager/
├── core_app/          # Main application
│   ├── models.py      # Folder and File models
│   ├── views.py       # API views
│   ├── serializers.py # DRF serializers
│   └── urls.py        # URL routing
├── filemanager/       # Django project settings
│   ├── settings.py    # Project settings
│   └── urls.py        # Root URL configuration
├── media/             # Uploaded files storage
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variables template
└── README.md          # This file
```

## Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Production Deployment

Before deploying to production:

1. Set `DEBUG=False` in your `.env` file
2. Set a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS` with your domain
4. Use a production database (PostgreSQL recommended)
5. Configure static files serving
6. Set up proper media file storage (e.g., AWS S3)
7. Use HTTPS
8. Configure CORS if needed

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


# Signature Pad Django

A simple Django application that integrates a vanilla JavaScript signature pad with a Django backend.

The project demonstrates how a browser-based signature can be captured as a Base64-encoded PNG, submitted through an HTML form, processed by Django, and displayed on a result page.

The signature pad is based on the standalone [Signature Pad JS](https://github.com/ronnieboy2k/signature-pad-js) library developed separately as a reusable vanilla JavaScript component.

## Overview

The application provides a simple eSignature workflow:

1. The user enters their name.
2. The user draws a signature using the signature pad.
3. The signature is exported as a PNG Data URL.
4. The Base64-encoded image is submitted to Django through an HTML form.
5. Django processes the submitted data.
6. The Base64 data is decoded into binary image data.
7. A PNG signature image is generated and saved.
8. The result page displays the generated signature image.

If no signature is submitted, the application removes the existing signature image and displays a message indicating that no signature is available.

## Features

* Django-based web application
* Vanilla JavaScript signature pad integration
* Mouse, touch, and stylus support through Pointer Events
* Smooth signature strokes
* HTML form submission
* CSRF protection
* Base64 Data URL processing
* PNG image generation
* Generated signature image display
* Handling of missing signatures
* Django automated tests
* GitHub Actions CI
* Black for Python code formatting

## Tech Stack

### Backend

* Python
* Django 5
* Django TemplateView
* Python `base64`
* Python `pathlib`

### Frontend

* HTML5
* CSS3
* Vanilla JavaScript
* HTML Canvas API
* Pointer Events API

### Development

* Git
* GitHub
* GitHub Actions
* Black
* Django Test Framework

## Project Structure

```text
signature-pad-django/
├── .github/
│   └── workflows/
│       └── tests.yml
├── signature_pad/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── signatures/
│   ├── services/
│   │   ├── __init__.py
│   │   └── signature.py
│   ├── static/
│   │   └── signatures/
│   │       ├── images/
│   │       │   └── signature.png
│   │       └── js/
│   │           └── signature-pad-js.js
│   ├── templates/
│   │   └── signatures/
│   │       ├── signature_form.html
│   │       └── signature_result.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── css/
│       └── base.css
├── templates/
│   └── base.html
├── .gitignore
├── manage.py
├── pyproject.toml
├── README.md
└── requirements-dev.txt
```

## Application Flow

```text
User
 │
 │ Draws signature
 ▼
Signature Pad JS
 │
 │ PNG Data URL
 ▼
HTML Form
 │
 │ POST
 ▼
Django View
 │
 │ Base64 data
 ▼
Signature Service
 │
 │ Decode Base64
 ▼
PNG Image
 │
 │ Save
 ▼
Signature Result Page
 │
 ▼
Generated Signature
```

## URLs

| URL                  | Method | Description                                               |
| -------------------- | ------ | --------------------------------------------------------- |
| `/signature/`        | GET    | Displays the signature form                               |
| `/signature/result/` | POST   | Processes the submitted signature and displays the result |
| `/signature/result/` | GET    | Displays the result page                                  |

The `/api/signature/` endpoint is intentionally reserved for a future React-based implementation.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ronnieboy2k/signature-pad-django.git
cd signature-pad-django
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment.

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### 3. Install development dependencies

```bash
python -m pip install -r requirements-dev.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

The project currently does not define custom database models. The migration step initializes Django's built-in applications.

### 5. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/signature/
```

## Using the Signature Pad

On the signature form:

1. Enter a name.
2. Draw a signature.
3. Click **Clear** to remove the signature if necessary.
4. Click **Submit**.
5. Django processes the submitted signature.
6. The result page displays the generated signature image.

The signature pad itself is implemented as a reusable vanilla JavaScript library and integrated into this Django application.

## Signature Processing

The signature pad generates a PNG Data URL similar to:

```text
data:image/png;base64,iVBORw0KGgo...
```

The Django backend receives this value from the submitted form.

The signature service:

1. Separates the Base64 data from the Data URL prefix.
2. Decodes the Base64 data.
3. Writes the resulting binary data to a PNG file.

The image-processing logic is separated into:

```text
signatures/services/signature.py
```

This keeps the view focused on handling the request and response while the service handles the image-processing operation.

## Static Files

The project uses Django's static-file structure to organize application assets.

Project-wide CSS is stored under:

```text
static/
└── css/
    └── base.css
```

Signature-specific static files are stored under the `signatures` application:

```text
signatures/
└── static/
    └── signatures/
        ├── images/
        │   └── signature.png
        └── js/
            └── signature-pad-js.js
```

The signature pad JavaScript library is loaded using Django's `{% static %}` template tag.

The generated `signature.png` file contains the processed signature image produced by the Django backend.

## Generated Signature Image

The current implementation generates:

```text
signatures/static/signatures/images/signature.png
```

When a valid signature is submitted, the existing image is overwritten with the newly generated PNG.

When no signature is submitted, the existing signature image is removed.

If no signature image exists, the result page displays:

```text
No signature available.
```

This implementation intentionally keeps file handling simple for the current project.

For a production application with multiple users and persistent signature records, generated files would normally be handled using Django's media-file system and associated with database records.

## Testing

The project uses Django's built-in test framework.

Run all tests with:

```bash
python manage.py test
```

The test suite covers the signature form and result page, including:

* URL availability
* Named URL resolution
* HTTP responses
* Template usage
* Submitted name content
* Result page behavior

The JavaScript signature-pad library has its own dedicated test suite in the separate repository.

## Code Formatting

Black is used to format Python code.

Run Black with:

```bash
black .
```

Black configuration is stored in:

```text
pyproject.toml
```

Current configuration:

```toml
[tool.black]
line-length = 88
```

## Continuous Integration

GitHub Actions automatically runs the Django test suite on pushes and pull requests.

Workflow:

```text
.github/workflows/tests.yml
```

The CI process:

1. Checks out the repository.
2. Sets up Python.
3. Installs development dependencies.
4. Runs the Django test suite.

This helps ensure that changes pushed to the repository continue to pass the automated tests.

## Design Goals

This project intentionally focuses on a small and understandable Django implementation rather than building a complete eSignature platform.

The primary goals are to demonstrate:

* Django project structure
* Class-based views
* Django templates
* HTML form handling
* CSRF protection
* Integration with a JavaScript library
* Base64 image processing
* File handling with Python
* Separation of service logic from views
* Automated testing
* Git-based development
* Continuous integration

Authentication, database persistence, user management, and a React frontend are outside the scope of this project.

## Future React Integration

A future project will extend this concept into a full-stack application using Django and React.

The planned architecture is:

```text
React
 │
 │ REST API
 ▼
Django
 │
 ▼
Database
 │
 ▼
Signature Records
```

The future implementation will focus on:

* React frontend
* Django REST API
* Database models
* Persistent signature records
* Signature image storage
* API-based communication
* Full-stack application architecture

The current project intentionally keeps these concerns out of scope so it can demonstrate a straightforward Django implementation first.

## Related Project

The signature pad used by this application is developed as a separate reusable JavaScript library:

**Signature Pad JS**

https://github.com/ronnieboy2k/signature-pad-js

The library is written in vanilla JavaScript and does not depend on Django, React, jQuery, or another frontend framework.

## AI Disclosure

AI tools were used as a development aid during this project, primarily for brainstorming, code review, debugging assistance, test-case suggestions, and documentation refinement.

All architectural decisions, implementation choices, testing, debugging, and final code validation were performed and reviewed by the author.

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

## Author

Ronnie Boy S. Altamira

```markdown
# URL Shortener API

This project implements a simple URL shortener API using Django and PostgreSQL. It provides endpoints to shorten long URLs and redirect users to the original URLs using short codes.

## Features

- Shorten a long URL and receive a short URL.
- Redirect to the original URL using the short code.
- Store the URL mappings in a PostgreSQL database.

## Endpoints

### POST `/shorten/`

- **Description**: Accepts a long URL and returns a shortened URL.
- **Request Body**:
  ```json
  {
    "long_url": "https://www.example.com/some/very/long/url"
  }
  ```
- **Response**:
  ```json
  {
    "short_url": "http://localhost:8000/abc123"
  }
  ```

### GET `/{short_code}`

- **Description**: Redirects to the original URL corresponding to the provided short code.
- **Response**: Redirects to the long URL or returns a 404 error if the short code does not exist.

## Project Structure

```
url_shortener/
├── manage.py
├── url_shortener/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
└── shortener/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

- `url_shortener/`: Main project directory.
- `manage.py`: Command-line utility for Django project management.
- `url_shortener/`: Directory containing project settings and configuration.
  - `settings.py`: Configuration settings, including database settings.
  - `urls.py`: URL routing for the project.
- `shortener/`: Django app for the URL shortener functionality.
  - `migrations/`: Directory for database migrations.
  - `models.py`: Database models for storing URL mappings.
  - `views.py`: Logic for handling API requests.
  - `urls.py`: URL routing for the shortener app.

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/url_shortener.git
   cd url_shortener
   ```

2. **Set Up a Virtual Environment (optional)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install django psycopg2
   ```

4. **Configure Database**:
   - Update the `DATABASES` setting in `url_shortener/settings.py` with your PostgreSQL credentials.

5. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Test the API**:
   - Use Postman or CURL to test the endpoints.

## Contribution

Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

You can save this content in a `.md` file for your project documentation. Let me know if you need any changes or additional sections!

Sources

# URL Shortener

A simple and efficient URL shortening service built with Python and Flask. This project allows users to convert long URLs into shorter, manageable links, making it easier to share and track URLs.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Shorten URLs**: Easily convert long URLs into short links.
- **Redirect**: Users can be redirected to the original URL using the shortened link.
- **Database Storage**: Stores shortened URLs and their corresponding original URLs in a database.
- **User-Friendly Interface**: Simple web interface for easy interaction.

## Technologies Used

- **Python**: Programming language used for backend development.
- **Flask**: Micro web framework for building the web application.
- **SQLite**: Lightweight database for storing URL mappings.
- **HTML/CSS**: For the frontend design.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yashovardhn/URLShortner.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd URLShortner
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**: Open your browser and go to `http://localhost:5000`.

## Usage

1. **Shortening a URL**:
   - Enter the long URL you wish to shorten in the input field.
   - Click the "Shorten" button.
   - Copy the generated short URL.

2. **Redirecting to the original URL**:
   - Paste the short URL into your browser's address bar.
   - You will be redirected to the original long URL.

## API Endpoints

- **POST /shorten**
  - **Description**: Shortens a given URL.
  - **Request Body**: 
    ```json
    {
      "long_url": "https://example.com/some/very/long/url"
    }
    ```
  - **Response**:
    ```json
    {
      "short_url": "http://localhost:5000/abc123"
    }
    ```

- **GET /<short_url>**
  - **Description**: Redirects to the original URL.
  - **Response**: Redirects to the long URL associated with the provided short URL.

## Database Schema

The database consists of a simple table to store the URL mappings:

| Column Name  | Data Type | Description                           |
|--------------|-----------|---------------------------------------|
| id           | INTEGER   | Primary key, auto-incremented        |
| long_url     | TEXT      | The original long URL                 |
| short_url    | TEXT      | The generated short URL               |
| created_at   | DATETIME  | Timestamp of when the URL was created|

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes. 

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Feel free to modify any sections as needed for your project! This README provides a thorough overview of the project, installation instructions, usage, API endpoints, and contribution guidelines.

Sources

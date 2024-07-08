# FastAPI User Management

This project is a simple FastAPI application for managing users. It allows you to create and read user information from a MySQL database.

## Features

- Create a new user
- Read user details by user ID

## Requirements

- Python 3.7+
- MySQL database

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-user-management.git
   cd fastapi-user-management
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:

   Update the `URL_DATABASE` variable in `database.py` with your MySQL database credentials.

   ```python
   URL_DATABASE = 'mysql+pymysql://<username>:<password>@<host>:<port>/<database>'
   ```

5. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

## Endpoints

### Create a new user

- **URL:** `/users/`
- **Method:** `POST`
- **Status Code:** `201 Created`
- **Request Body:**

  ```json
  {
    "username": "string"
  }
  ```

- **Response:**

  ```json
  {
    "id": 1,
    "username": "string"
  }
  ```

### Read user details

- **URL:** `/users/{user_id}`
- **Method:** `GET`
- **Status Code:** `200 OK`
- **Response:**

  ```json
  {
    "id": 1,
    "username": "string"
  }
  ```

- **Error Response:**

  ```json
  {
    "detail": "User Not Found"
  }
  ```

## Project Structure

- `main.py`: The main application file.
- `database.py`: Database configuration.
- `models.py`: Database models.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

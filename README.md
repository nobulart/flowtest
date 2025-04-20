# Flask Hello World API

## Description

This is a simple Flask REST API demonstrating a basic "Hello, World!" endpoint. It serves as a starting point for building more complex Flask applications.

## Prerequisites

*   **Python:** Version 3.6 or higher
*   **pip:** Python package installer

## Installation

1.  Clone the repository:

    ```bash
    git clone [repository URL]
    cd [project directory]
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\activate   # Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install flask
    ```

## Running the Application

1.  Save the `app.py` file (provided in this repository) to your project directory.

2.  Run the Flask application:

    ```bash
    python app.py
    ```

    This will start the development server, typically accessible at `http://localhost:5000/`.

## API Endpoint

*   **Endpoint:** `/hello`
*   **Method:** GET
*   **Response:**  The endpoint returns the string "Hello, World!".

You can test this endpoint using a web browser or tools like `curl`:

```bash
curl http://localhost:5000/hello
```

## Testing

Unit tests are provided using pytest. To run them:

1.  Install pytest:

    ```bash
    pip install pytest
    ```

2.  Run the tests from the project directory:

    ```bash
    pytest
    ```

## License

[Specify license here - e.g., MIT License]
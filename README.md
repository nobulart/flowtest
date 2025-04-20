# Flask Hello World API

## Description

This is a simple Flask REST API with a single endpoint, `/hello`, that returns the greeting "Hello, World!".  It serves as a basic example to demonstrate how to create and run a Flask application.

## Prerequisites

*   **Python:** Version 3.6 or higher
*   **pip:** Python package installer

## Installation

1.  Clone this repository:

    ```bash
    git clone [repository URL]
    cd [project directory]
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate   # On Windows
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

    This will start the development server, typically on `http://localhost:5000/`.

## API Endpoint

*   **Endpoint:** `/hello`
*   **Method:** GET
*   **Response:**

    ```json
    "Hello, World!"
    ```

You can test the endpoint by opening your web browser or using a tool like `curl`:

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

## Contributing

Contributions are welcome! Please submit pull requests with clear descriptions of your changes.

## License

[Specify license here - e.g., MIT License]
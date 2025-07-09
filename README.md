# Fibonacci Counter with Docker

A simple web application that displays Fibonacci numbers, containerized with Docker.

## Features
- Web interface to display Fibonacci numbers
- REST API endpoint to get Fibonacci sequences
- Responsive design
- Reset functionality

## Prerequisites
- Docker
- Docker Compose (optional)

## Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t fibonacci-counter .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 fibonacci-counter
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## API Endpoint

You can also get Fibonacci sequences via the API:
```
GET /api/fibonacci/<n>
```

Example:
```bash
curl http://localhost:5000/api/fibonacci/10
```

## Development

To run locally without Docker:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## License
MIT

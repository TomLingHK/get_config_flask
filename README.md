# add_log_flask

This is a simple Flask application that provides an API endpoint to get data from a config file. The application is designed to run in a Docker container and can be easily integrated into existing workflows for reading file.

## Features
- Return data from text file or json file.
- Configurable base path for log storage via environment variables.

## Simple setup locally
1. Install dependency:
```bash
pip install -r requirements.txt
```
2. Run the Flask application:
```bash
python app.py
```

## API Endpoint

### POST /run
This endpoint accepts a JSON payload to specify the `dir_name`, `file_name` to be added to the log file.
- `dir_name`(string): The directory where the log file is located (e.g., "logs/"). The directory will be created if it does not exist.
- `file_name`(string) (required): The name of the log file (e.g., "log_20260228.txt"). The log file will be created if it does not exist. If the file already exists, the new log entries will be appended to the existing file.

#### Request Body
```json
{
    "dir_name": "config/",
    "file_name": "default_prompt.txt",
}
```

#### Response
```json
[
  {
    "message": "Successfully retrieved config from config/default_prompt.txt",
    "data": "You are a customer service manager..."
  }
]
```
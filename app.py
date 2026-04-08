import os
from flask import Flask, jsonify, request

from get_config import get_config

app = Flask(__name__)

SERVICE_NAME = "add_log"
# BASE_PATH = "./test_log/"
BASE_PATH = os.getenv("BASE_PATH") or "/nas_data/"

if not (os.path.isdir(BASE_PATH) and os.access(BASE_PATH, os.R_OK)):
    BASE_PATH = "/app/nas_data/"

print('BASE_PATH: ', BASE_PATH)


APP_CONST = {
    'BASE_PATH': BASE_PATH,
}

@app.route("/run", methods=['GET'])
def main():
    """
        dir_name(string): "abc_project/debug/"
        file_name(string): "log_20260228.txt"
    """
    print(f"BACKGROUND TASK STARTED for endpoint: /")
    data = request.get_json(silent=True) or {}
    dir_name = data.get('dir_name', '')
    file_name = data.get('file_name', '')
    
    if (len(file_name) == 0):
        print(f"Empty file_name provided, returning error response.")
        return jsonify({"error": "No file_name provided. Expect file name with extension."}), 400
    
    return jsonify(get_config(APP_CONST, dir_name, file_name)), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
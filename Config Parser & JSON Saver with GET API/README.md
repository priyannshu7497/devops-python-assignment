# DevOps Python Assignment – Configuration File Parser with REST API

This project demonstrates a simple configuration management system using Python. It reads a `.ini` configuration file, parses key-value pairs from sections, stores them as a JSON file, and exposes the data via a REST API using Flask.

---

## 📁 Files in this Project

- `config_parser.py` — Main Python script that parses the config and runs the Flask server.
- `config.ini` — Sample configuration file.
- `output.json` — Auto-generated file storing the config data in JSON format (created after running the script).

---

## ⚙️ How it Works

1. The script reads a `config.ini` file.
2. It parses all sections and keys into a Python dictionary.
3. The dictionary is written to a `output.json` file.
4. A Flask server is started to serve this JSON data via an API.

---

## 🔧 Requirements

Install dependencies using:

```bash
pip install flask

How to Run
Make sure both config_parser.py and config.ini are in the same folder.

Run the script:

python config_parser.py

Output:

Configuration Parsed Successfully. Starting server...
 * Running on http://127.0.0.1:5000

API Endpoint
GET /get-config
Returns the parsed configuration in JSON format.

Example:

http://127.0.0.1:5000/get-config


Sample config.ini

[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080


Output output.json

{
    "Database": {
        "host": "localhost",
        "port": "3306",
        "username": "admin",
        "password": "secret"
    },
    "Server": {
        "address": "192.168.0.1",
        "port": "8080"
    }
}

Author PRIYANSHU GUPTA

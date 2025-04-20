import configparser
import json
import os
from flask import Flask, jsonify

CONFIG_FILE = "config.ini"
OUTPUT_FILE = "output.json"

app = Flask(__name__)

def parse_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Configuration file not found.")
    
    config = configparser.ConfigParser()
    config.read(file_path)

    result = {}
    for section in config.sections():
        result[section] = dict(config.items(section))

    with open(OUTPUT_FILE, "w") as f:
        json.dump(result, f, indent=4)

    return result

@app.route('/get-config', methods=['GET'])
def get_config():
    try:
        with open(OUTPUT_FILE, "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    try:
        config_data = parse_config(CONFIG_FILE)
        print("Configuration Parsed Successfully. Starting server...")
        app.run(debug=True)
    except Exception as e:
        print(f"Error: {e}")

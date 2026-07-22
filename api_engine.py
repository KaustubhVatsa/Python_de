import requests
import json
import time


def params_to_dict(params_str):
    if not params_str:
        return {}
    try:
        return json.loads(params_str)
    except json.JSONDecodeError:
        print("Invalid JSON format for parameters. Please provide a valid JSON string.")
        return {}


def call_api(url, params=None):
    # Added timeout for better error handling
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def retry_api_call(url, params=None, retries=3):
    for attempt in range(retries):
        try:
            return call_api(url, params=params)

        except requests.exceptions.RequestException:
            if attempt == retries - 1:
                raise  # Re-raise the original exception

            wait_time = 2 ** attempt
            print(f"Attempt {attempt + 1} failed. Retrying in {wait_time}s...")
            time.sleep(wait_time)

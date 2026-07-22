import requests

from api_engine import retry_api_call, params_to_dict
from destination import store_data

if __name__ == "__main__":
    base_url = input("Enter api url: ")
    params = input("Enter parameters : ")
    file_name = input("Enter filename to store data: ")
    params_dict = params_to_dict(params)

    try:
        response = retry_api_call(base_url, params=params_dict)
        store_data(response, file_name)
        print("Pipeline finished successfully")
    except requests.exceptions.RequestException as e:
        print(f"Pipeline failed: {e}")

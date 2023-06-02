import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

api_url = "https://localhost:60000/api/login"

test = {
  "User": {
    "login_id": "admin",
    "password": "Admin1234"
  }
}

def login():
    try:
        response = requests.post(api_url, json=test, verify=False)
        if response.status_code == 200:
            # data = response.json()
            data = response.headers["bs-session-id"]
            return data
            # print(data)
        else:
            print("Request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
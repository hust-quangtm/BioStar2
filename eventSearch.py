import requests
import urllib3
from login import *
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

api_url = "https://localhost:60000/api/events/search"

test = {
  "Query": {
    "limit": 150,
    "conditions": [
      {
        "column": "datetime",
        "operator": 5,
        "values": [
          "2023-05-31T10:00:00.000Z"
        ]
      },
      {
        "column": "event_type_id.code",
        "operator": 0,
        "values": [
          "4102"
        ]
      }
    ],
    "orders": [
      {
        "column": "datetime",
        "descending": False
      }
    ]
  }
}

try:
    bs_session_id = login()
    response = requests.post(api_url, headers={"bs-session-id": bs_session_id}, json=test, verify=False)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Request failed with status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
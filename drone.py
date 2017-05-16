import requests
from authentication_keys import *

url = "http://droneapi.ddns.net:1235/vehicle/8ce02f05"

headers = {
    'cache-control': "no-cache",
    'postman-token': postman_token
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
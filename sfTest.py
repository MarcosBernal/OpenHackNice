import requests
import json
from authentication_keys import *

url = "https://eu11.salesforce.com/services/apexrest/openAPI/customer"

headers = {
    'x-prettyprint': "1",
    'authorization': authorization,
    'cache-control': "no-cache",
    'postman-token': postman_token
    }

response = requests.request("GET", url, headers=headers)

# print(response.text)

# print response.status_code
jRep = json.loads(response.text)
for i in jRep:
	print i

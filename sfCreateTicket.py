import requests
import json
from authentication_keys import *

url = "https://eu11.salesforce.com/services/apexrest/openAPI/troubleTicket"

headers = {
    'x-prettyprint': "1",
    'content-type': "application/json",
    'authorization': authorization,
    'cache-control': "no-cache",
    'postman-token': postman_token
    }


def create_sf_ticket(handle, text, lat, lon):
	jPayload = {
		"subStatus": "Pending",
		"status": "Submitted",
		"twitterHandle": "%s" % handle,
		"subject": "%s" % text,
		"location_long": "%s" % lon,
		"location_lat": "%s" % lat,
		"asset": "02i0Y0000003nWtQAI"
	}

	response = requests.post(url, data=json.dumps(jPayload), headers=headers)

# Example
# create_sf_ticket("iveronar", "test report from twitter!", "1.23", "3.21")

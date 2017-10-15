import requests
import json
from authentication_keys import *

common_url = "https://eu11.salesforce.com/services/apexrest/openAPI/"
url_trouble_ticket = "troubleTicket"
url_customer_accounts = "customerAccount"

headers = {
    'x-prettyprint': "1",
    'content-type': "application/json",
    'authorization': "Bearer " + authorization
}


def unique_ticket(url, user, problem, location):
    reply = requests.request("GET", common_url + url_trouble_ticket, headers=headers)
    tickets = reply.json()
    ticket_similares = [ticket for ticket in tickets if
                        ticket['twitterhandler'] == user or ticket['location'] == location]
    return ticket_similares is []


def create_sf_ticket(handle, text, lat, lon):
    payload = {
        "subStatus": "Pending",
        "status": "Submitted",
        "twitterHandle": "%s" % handle,
        "subject": "%s" % text,
        "location_long": "%s" % lon,
        "location_lat": "%s" % lat,
        "asset": "02i0Y0000003nWtQAI"
    }

    response = requests.post(common_url + url_trouble_ticket, data=json.dumps(payload), headers=headers)

    print type(response)

    # Example
    # create_sf_ticket("iveronar", "test report from twitter!", "1.23", "3.21")

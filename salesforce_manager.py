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

class TroubleTicket:
    def __init__(self, json):
        self.user = json['twitterHandle'] # User that created the ticket
        self.reason = json['reason']      # The reason why the ticket was opened (water leaked or dry space)
        self.description = json['description']   # Additional text
        self.location = json['location']  # Dictionary that contains the lat and long of the place where the problem arised

    def equal(self, troubleticket):
        value = False
        message = ""

        if self.reason == troubleticket.reason and self.location['longitude']==troubleticket.location['longitude'] \
                and self.location['latitude'] == troubleticket.location['latitude']:
            value = True
            message = "Problem already detected, type and location"

        if self.user == troubleticket.user and self.reason == troubleticket.reason:
            value = True
            message = "Problem already sent by user"

        return value, message

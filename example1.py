#! /usr/bin/env python

from device_info import dnac
import requests
import json
import urllib3
import pprint

# Silence the insecure warning due to SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers = {'content-type': "application/json",
'x-auth-token': "" }

def dnac_login(dnac, port, username, password):
    """
    Use the REST API to Log into an DNA Center and retrieve ticket
    """
    url = "https://{}:{}/dna/system/api/v1/auth/token".format(dnac, port)

    # Make Login request and return the response body
    response = requests.request("POST", url,
                                auth = (username, password),
                                headers=headers, verify=False)
    return response.json()["Token"]


def site_list(host, token):
    """
    Use the REST API to retrieve the list of network devices
    """
    url = "https://{}/dna/intent/api/v1/site".format(host)
    headers["x-auth-token"] = token

    # Make API request and return the response body
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.json()["response"]
    
    

def JayController(host, token):

    """Check your controller 
    """

    url = "https://{}/dna/intent/api/v1/membership/fd3feea8-f0ca-41a4-aaef-e81a912f79b5".format(host)
    headers["x-auth-token"] = token
    response = requests.request("GET", url, headers=headers, verify= False)
    return response.json()["device"]


# Entry point for program
if __name__ == '__main__':
    # Log into the DNA Center Controller to get Ticket
    token = dnac_login(dnac["host"], dnac["port"], dnac["username"], dnac["password"])

    # Get the list of sites
    sites = site_list(dnac["host"], token)
    y = type(sites)
    print (y)
    floors = JayController(dnac["host"], token)

    x = type(floors)

   


    # Loop through the devices and print details
    for site in sites:
        print(" Floor Name: {}".format(site["name"]))
        print("  ID: {}".format(site["id"]))
        print(" NameSpace: {}".format(site["additionalInfo"]["namespace"]))
        print("")
   

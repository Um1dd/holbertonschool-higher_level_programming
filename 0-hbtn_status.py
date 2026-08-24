#!/usr/bin/python3
"""
This module fetches the status from https://intranet.hbtn.io/status
using urllib, including the required bypass header.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    headers = {'cfclearance': 'true'}

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

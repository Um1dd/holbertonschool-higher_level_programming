#!/usr/bin/python3
"""
This module fetches the status of a specific URL
using urllib package and displays response details.
"""
import urllib.request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = urllib.request.Request(url, headers={'cfclearance': 'true'})
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))

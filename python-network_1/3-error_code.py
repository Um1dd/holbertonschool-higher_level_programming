#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
It handles urllib.error.HTTPError exceptions.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url, headers={'cfclearance': 'true'})

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

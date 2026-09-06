#!/usr/bin/python3
"""
This module takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
Handles JSON responses and edge cases.
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        r = requests.post(url, data=payload)
        json_res = r.json()
        if json_res:
            user_id = json_res.get('id')
            user_name = json_res.get('name')
            if user_id is not None and user_name is not None:
                print("[{}] {}".format(user_id, user_name))
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

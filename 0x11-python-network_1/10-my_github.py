#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    # Define the GitHub API endpoint
    url = 'https://api.github.com/user'

    # Set the username and personal access token
    username = sys.argv[1]
    password = sys.argv[2]

    # Set the headers with the Basic Authentication credentials
    headers = {'Authorization': f'Basic {username}:{password}'}

    # Make the API request to get the user ID
    response = requests.get(url, headers=headers)

    # Print the user ID
    print(response.json().get('id'))

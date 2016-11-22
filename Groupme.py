import os
import time
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning, SNIMissingWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
requests.packages.urllib3.disable_warnings(SNIMissingWarning)

def _get_group_ID(group_name, access_token):
    request = requests.get('{}/groups?token={}.'.format('https://api.groupme.com/v3',access_token))
    response = request.json()['response']
    for group in response:
        name = ''.join([i if ord(i) < 128 else ' ' for i in group['name']])
        if group_name == name.strip():
            return group['id']

def main():
    required_info = {}
    required_info['Access Token'] = '8GzVc1uYiakhuRQELHHzgKUY7SjK4E8c8FdAPDXE'
    required_info['Group Name'] = 'BIG Data'
    #required_info['Group Members'] = 'Robby Fry:Robby_Fry'
    group_ID = 26254692
    #group_ID = _get_group_ID(required_info['Group Name'], required_info['Access Token'])
    request = requests.get('{}/groups/{}/messages?limit=100&token={}'.format('https://api.groupme.com/v3',group_ID, required_info['Access Token']))
    response = request.json()['response']
    with open('test.txt', 'w') as outfile:
        json.dump(response, outfile)

main()
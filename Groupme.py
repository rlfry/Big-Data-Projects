import os
import time
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning, SNIMissingWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
requests.packages.urllib3.disable_warnings(SNIMissingWarning)

def _get_messages(r_info, ID):
    request = requests.get('{}/groups/{}/messages?limit=100&token={}'.format('https://api.groupme.com/v3',ID, r_info['Access Token']))
    response = request.json()['response']
    retrieved = len(response['messages'])
    messages = _filter_messages(response['messages'])
    message_count = response['count']
    #print('Message Count: {}'.format(message_count))
    while retrieved < message_count:
        before_ID = messages[-1]['id']
        request = requests.get('{}/groups/{}/messages?limit=100&before_id={}&token={}'.format('https://api.groupme.com/v3',ID, before_ID, r_info['Access Token']))
             
        # Break if status code 304 (i.e. no data) is returned
        if (request.status_code == 304): break
        response = request.json()['response']
        retrieved += len(response['messages'])
        print('Retrieved: {}'.format(retrieved))
        messages += _filter_messages(response['messages'])
        #print('Messages length: {}'.format(len(messages)))


def _filter_messages(msgs):
	messages = []
	for message in msgs:
		if message['user_id'] != 'system':
			messages.append(message)
			with open('MVP.json', 'a+') as outfile:
				json.dump(message, outfile)
	return messages

def main():
    required_info = {}
    required_info['Access Token'] = #Insert access token here
    required_info['Group Name'] = 'MVPs'
    group_ID = #Insert group ID here
    _get_messages(required_info, group_ID)
    #with open('bigData.json', 'w') as outfile:
        #json.dump(messages, outfile)

main()

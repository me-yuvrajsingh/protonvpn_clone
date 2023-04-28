#aditya14yad

import requests
import json

url = 'https://api.protonmail.ch/vpn/logoutsessions'

headers = {
    'Accept': 'application/vnd.protonmail.v1+json',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
}

response = requests.delete(url, headers=headers)

if response.status_code == 204:
    print('Successfully logged out all VPN sessions')
else:
    print(f'Error: {response.status_code} - {response.reason}')

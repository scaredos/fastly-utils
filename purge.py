# scaredos / fastly-utils (2021)
# purge a specific uri or purge all
import sys
import requests

with open('api.txt', 'r') as file:
	key = file.read().strip("\n")

auth_h = {
"Fastly-Key": key
}

fastly_json = requests.get('https://api.fastly.com/services', headers=auth_h).json()
id = fastly_json["data"][0]["id"]

if len(sys.argv) != 2:
    print('fastly cache purge')
    print('usage: {} <domain (all for all domains)> <uri (optional)>'.format(sys.argv[0]))
    exit()


domain = sys.argv[1]
if domain == 'all':
    r = requests.post('https://api.fastly.com/service/{}/purge_all'.format(id), headers=auth_h)
    print(r.text)
    exit()
try:
    uri = sys.argv[2]
except:
    uri = ''
r = requests.post('https://api.fastly.com/purge/{}/{}'.format(domain, uri), headers=auth_h)
if 'ok' in r.text:
    print('purged {}{}'.format(domain, uri))
else:
    print(r.text)

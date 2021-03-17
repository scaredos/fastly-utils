# scaredos / fastly-utils (2021)
# used for whitelisting fastly ip ranges to backend (ACL)
# allows fastly ip ranges then blocks everything else to port 80
import os
import requests

r = requests.get("https://api.fastly.com/public-ip-list")
if r.status_code != 200:
	print("error")
	exit()

fjson = r.json()
for ip in fjson["addresses"]:
	print("whitelisting {}".format(ip))
	os.system('iptables -A INPUT -p tcp --dport 80 -s {} -j ACCEPT'.format(ip))


os.system('iptables -A INPUT -p tcp --dport 80 -j DROP')
print('done')

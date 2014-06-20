import requests
import json

Access_token = 'b0e86264e1b3dfb6d8f93c84eda09c2e42c82017'
api_url = "https://api.github.com/users"


def get_comments():
	usrname = raw_input("Enter the username:")
	url = api_url+usrname+"/events"
	req = requests.get(url)
	res = req.content
	# print res
	resp = json.loads(res)

	pload = [li['payload']for li in resp]
	payload = pload[0]
	# print payload

	for k,v in payload.items():
		print v['html_url']

if __name__ == '__main__':
	get_comments()

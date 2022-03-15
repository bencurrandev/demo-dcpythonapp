# import the REST library
import requests

base_url = "http://127.0.0.1:3000/startup"

resp = requests.get(base_url)

status = resp['headers']['status']

if status == '200' or status == '304':
    print(resp.json())
else:
    print('Error status code: ', status)

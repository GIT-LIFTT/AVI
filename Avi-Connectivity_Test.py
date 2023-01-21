# Test Connectivity from the controller the to the configured cloud

import requests
import pprint

url = "https://192.168.203.179/api/cloud"

payload={}
headers = {
  'Authorization': 'Basic [REMOVED]]',
  'Cookie': 'avi-sessionid=None; sessionid=None'  
}

response = requests.request("GET", url, headers=headers, data=payload ,verify=False)

print(response.text)


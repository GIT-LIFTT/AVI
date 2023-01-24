#This script is designed the retrive a list of vip and store them in a database 
import requests

url = "https://192.168.203.179/api/virtualservice"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46UGFzc3dvcmQxMTIh',
  'Cookie': 'avi-sessionid=None; sessionid=None'
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

data = (response.)

print(type(data))




#database connector 


#send data to database 
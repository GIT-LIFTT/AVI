#This script is designed the retrive a list of vip and store them in a database 
import requests

url = "https://192.168.203.179/api/virtualservice"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46UGFzc3dvcmQxMTIh',
  'Cookie': 'avi-sessionid=None; sessionid=None'
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

data = (response.json())

actual_results = (data["results"][0])

print(actual_results["name"])



actual_results2 = (data["results"][1])

print(actual_results2["name"])

#for i in actual_results:
#    print(i)




#database connector 


#send data to database 
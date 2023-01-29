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

actual_results = (data["results"])

vip_dict = {}

for eachvip in actual_results:
    
    vip_name = (eachvip["name"])
    vip_uuid = (eachvip["uuid"])
    vip_ipaddress = (eachvip["ip_address"]["addr"])
    vip_status = (eachvip["enabled"])
    vip_port = (eachvip["services"][0]["port"])
    vip_lastmodified =(eachvip["_last_modified"])
    vip_dict[eachvip["name"]] = {"vip_name": vip_name,"vip_uuid": vip_uuid,"vip_ipaddress": vip_ipaddress,"vip_status": vip_status,"vip_port": vip_port,"vip_lastmodified":vip_lastmodified}

##write the data to a dictionary data structure


print(vip_dict)

#database connector 


#send data to database 
# CRONTAB        */30 * * * * /usr/bin/python /PATH/TO/THIS/SCRIPT/dynBoto.py


import boto3
import json
import requests
import os
from pprint import pprint
root_path = os.path.dirname(os.path.realpath(__file__))

#Get list of subdomains from local file and parse them into an array
subdomains = open(root_path + "subdomains", "r")
subdomain_name=[]
for line in subdomains:
   subdomain_name.append(line.strip('\n'))
subdomains.close()

#Get the current local ip of this machine
findip = requests.get("http://ipinfo.io")
findip_response = json.loads(findip.text)
current_ip = str(findip_response["ip"])
#get AWS recordsets
client = boto3.client('route53')
response  = client.list_resource_record_sets(HostedZoneId='XXXXXXXXXXXXXX')
recordSets = response["ResourceRecordSets"]

for i in range(0, len(recordSets)):
        domainarray = recordSets[i]["Name"].split('.')   
        subdomain = domainarray[0]
        thisip = recordSets[i]["ResourceRecords"][0]["Value"]
        recordtype = recordSets[i]["Type"]
        if subdomain in subdomain_name:
          if thisip != current_ip:
          full_domain = subdomain + ".YOURURL.HERE"
          batchDict ={
                    "Comment": "COMMNETS GO HERE",
                    "Changes":
                    [
                          {
                              "Action": "UPSERT", #dont change this
                              "ResourceRecordSet":
                              {
                                    "Name": full_domain,
                                    "Type": "A",
                                    "ResourceRecords":
                                    [
                                        {
                                              "Value": current_ip 
                                        }
                                    ],
                    "TTL": 3600
                              }
                          }
                    ]
                }
          response = client.change_resource_record_sets(HostedZoneId='XXXXXXXXXXXXXX',ChangeBatch=batchDict)
          print(full_domain)

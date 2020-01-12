import json
import requests
import sys

with open('data.json') as json_file:
    datatosend = json.load(json_file)

head = {"Content-Type":"x-www-url-formurlencoded","Accept":"application/json"}
url = 'http://localhost:8000/inventory/58cbe2fe503cd85421779762'

def tryWithCatName(catname, data):
        data['general']['category'] = catname 
        payload = json.dumps(data)
        r = requests.patch(url, payload, headers=head)
        print("Schema " + data['general']['category'] + ":" ,r)

# loop through all schema items and try to send update to igneous
with open('schematitles_prod.json') as schemajson:
    schemadata = json.load(schemajson)

    fruits = schemadata['titles']
    for index in range(len(fruits)):
        print 'Current fruit :', fruits[index]['title']
        tryWithCatName(fruits[index]['title'], datatosend)


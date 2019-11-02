from flask import Flask, render_template, request, jsonify

import requests
import json


API_ENDPOINT= "http://1572655316.proxy.chainapp.live/"
  
data = {'sender':'x', 'receipient':'y', 'amount':1} 
#data= "{ \"sender\": \"x\", \"recipient\": \"y\", \"amount\": 1}"
headers = {'Content-Type': 'application/json'}
#response = requests.post(url=API_ENDPOINT+"transaction/new",json=data )

print(response.json())
response = requests.get(url=API_ENDPOINT+"chain")
print(response.json())
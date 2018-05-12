import json
from flask import Flask, abort, jsonify, request
import requests

url = "http://localhost:5001/api"
data = json.dumps({'max_inactive_days': 0.40405189, 
                   'neg_trans':  -0.05237904, 
                   'pos_trans':  0.88580542,  
                   'aum_change_pct': 0.43153082, 
                   'gross_amt_change': 0.54977195})
r = requests.post(url,data)
#print (r.json())
print(r.text)
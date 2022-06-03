#!/usr/bin/python3
print('Access-Control-Allow-Origin: *')
print('Access-Control-Allow-Headers: *')
print('Access-Control-Allow-Methods: *')
print()
from Classes import *
import sys

creds = Credentials()
method = Methods()
project = method.StablishConnection()
myjson = json.load(sys.stdin)
# print(json.dumps(myjson))
# file_name = myjson['filename']
files = myjson
file_names = []
for file in files:
    object = method.DeleteItems(project,file['filename'])
    file_names.append(file['filename'])
print(json.dumps({"message": ', '.join([str(x) for x in file_names]) + " has been deleted","status": 200}))
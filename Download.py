#!/usr/bin/python3
print('Access-Control-Allow-Origin:*')
print('Access-Control-Allow-Headers: *')
print('Access-Control-Allow-Methods: *')
print()
import sys
from Classes import *

creds = Credentials()
method = Methods() 

raw = json.load(sys.stdin)
file_name = raw['filename']
project = method.StablishConnection()
download_object = method.DownloadObject(project,file_name)



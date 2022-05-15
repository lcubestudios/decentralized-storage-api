#!/usr/bin/python3
print('Access-Control-Allow-Origin:*')
print('Access-Control-Allow-Headers: *')
print('Access-Control-Allow-Methods: *')
from Classes import *

creds = Credentials()
method = Methods()

project = method.StablishConnection()
buckets = method.EnlistAllBuckets(project)

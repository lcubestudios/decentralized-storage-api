#!/usr/bin/python3
from Classes import *

creds = Credentials()
method = Methods()

headers = {
    'Content-Type': 'application/json', 
    'Access-Control-Allow-Origin': 'http://localhost:5500', 
    'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, DELETE, OPTIONS',
    'Access-Control-Allow-Headers':'Content-Type, Authorization, Accept, Accept-Language, X-Authorization'
}
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
file_item = form.getvalue['filename']
print(file_item)
# project = method.StablishConnection()
# upload_object = method.UploadObject(project,file_item)




#!/usr/bin/python3
from Classes import *
creds = Credentials()
method = Methods()
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
file_item = form.getvalue['filename']
project = method.StablishConnection()
upload_object = method.UploadObject(project,file_item)




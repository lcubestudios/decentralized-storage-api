#!/usr/bin/python3
from Classes import *
creds = Credentials()
method = Methods()


# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get file path

# Get filename 
file_item = form['filename']
project = method.StablishConnection()
upload_object = method.UploadObject(project,file_item)




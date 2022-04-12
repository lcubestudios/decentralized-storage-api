#!/usr/bin/python3
from Classes import *
creds = Credentials()
method = Methods()
cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get filename 
file_item = form['filename']
project = method.StablishConnection()
upload_object = method.UploadObject(project,file_item)




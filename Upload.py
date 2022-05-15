#!/usr/bin/python3
print('Access-Control-Allow-Origin:*')
print('Access-Control-Allow-Headers: *')
print('Access-Control-Allow-Methods: *')
print()
from Classes import *
creds = Credentials()
method = Methods() 
form = cgi.FieldStorage()

fileitem = form['filename']
if fileitem.filename:
    fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
    open('/tmp/' + fn,'wb').write(fileitem.file.read())
    message = "File uploaded to server"
else:
    message = "Something failed"

project = method.StablishConnection()
upload_object = method.UploadObject(project,fileitem)
os.system("rm /tmp/"+fn)

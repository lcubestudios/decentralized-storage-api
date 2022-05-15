#!/usr/bin/python3
print('Access-Control-Allow-Origin:*')
print('Access-Control-Allow-Headers: *')
print('Access-Control-Allow-Methods: *')
# print("Content-type:text/html")
#print('Content-Type: application/octet-stream;')
#print('Content-Disposition: attachment; filename=Bro-aaron.jpeg')
print()
from Classes import *

creds = Credentials()
method = Methods()

myjson = json.load(sys.stdin)
file_name = myjson['filename']

# file_name = 'Bro-aaron.jpeg'
project = method.StablishConnection()
#file_name = 'Bro-aaron.jpeg'
download_object = method.DownloadObject(project,file_name)
dst_directory="/var/www/html/dev/dcs-api/tmp"
os.system('mv /tmp/'+file_name+' '+dst_directory)
file = dst_directory+'/'+ file_name
encode = base64.urlsafe_b64encode(file.encode("utf-8"))
encodedstr = str(encode, "utf-8")
print(json.dumps({'status': 200, 'base64': encodedstr, 'filename': file_name}))
# print ("<html>")
# print ("<a href='FILES/%s' download>" % file_name)
# print ("<p> %s </p>" % file_name)
# print ("</html>")

# shutil.move("/tmp/Bro-aaron.jpeg", "/var/www/html/dev/dcs-api/FILES/")
# print("Done")

# Actual File Content will go here.
#Bro-aaron.jpeg
# file = open('/tmp/Bro-aaron.jpeg', 'rb')
# data = file.read()
# print(data)
# base = base64.b64decode(data)
# print(base)
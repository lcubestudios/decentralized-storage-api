#!/usr/bin/python3
print('Access-Control-Allow-Origin:*')
print('Access-Control-Allow-Headers: *')
print('Access-Control-Allow-Methods: *')
print("Content-type:text/html")
#print('Content-Type: application/octet-stream;')
#print('Content-Disposition: attachment; filename=Bro-aaron.jpeg')
#print()
from Classes import *

creds = Credentials()
method = Methods()

# myjson = json.load(sys.stdin)
# file_name = myjson['filename']

file_name = 'Bro-aaron.jpeg'
project = method.StablishConnection()
#file_name = 'Bro-aaron.jpeg'
download_object = method.DownloadObject(project,file_name)
# dst_directory="/var/www/html/dev/dcs-api/tmp"
# os.system('mv /tmp/'+file_name+' '+dst_directory)
# file = dst_directory+'/'+ file_name
# encode = base64.urlsafe_b64dencode(file.encode("utf-8"))
# encodedstr = str(encode, "utf-8")
# print(json.dumps({'status': 200, 'base64': encodedstr, 'filename': file_name}))
# print ("<html>")
# print ("<a href='FILES/%s' download>" % file_name)
# print ("<p> %s </p>" % file_name)
# print ("</html>")

# shutil.move("/tmp/Bro-aaron.jpeg", "/var/www/html/dev/dcs-api/FILES/")
# print("Done")

# Actual File Content will go here.
#Bro-aaron.jpeg

#file = open('/tmp/Bro-aaron.jpeg', 'rb')
#data = file.read()
#decodedBytes = base64.b64decode(data)
#decodedStr = str(decodedBytes, "utf-8")
#print(decodedStr)   # hello world123!?$

# print(data)
# base = base64.b64decode(data)
# print(base)

with open('/tmp/Bro-aaron.jpeg', 'rb') as photo2code:
    coded_str = photo2code.read()
    encoded = base64.b64encode(coded_str)
    encoded_utf8 = encoded.decode('utf-8')   # print(coded_str)

#decoder=open('/tmp/Bro-aaron.jpeg', 'rb')
#read_b64 = decoder.read()
#print(base64.b64decode(read_b64))
# print(read_b64)

#image = Image.open('/tmp/Bro-aaron.jpeg')
#image.show()

#img = cv2.imread('/tmp/Bro-aaron.jpeg',0)
#cv2.imshow('/tmp/Bro-aaron.jpeg',img)

print('<html>')
# print('<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==" alt="Red dot" />')
print('<a href="data:image/jpeg;base64,'+encoded_utf8+'" download>Download</a>')
# print('<img src="data:image/jpeg;base64,'+encoded_utf8+'"/>')
print('</html>')
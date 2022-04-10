from distutils.command.upload import upload
from Classes import *


creds = Credentials()
method = Methods()

url = 'http://127.0.0.1:5500/'
headers = {
    "Content-Type":"text",
}
r = requests.post(url, headers=headers,allow_redirects=True)

project = method.StablishConnection()
file_item = form['filename']
upload_object = method.UploadObject(project,file_item)




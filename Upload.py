from distutils.command.upload import upload
from Classes import *

creds = Credentials()
method = Methods()

project = method.StablishConnection()
upload_object = method.UploadObject(project)
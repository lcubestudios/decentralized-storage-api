#!/usr/bin/python3
print("Content-Type:text/html;charset=utf-8")
print()
from Classes import *

creds = Credentials()
method = Methods()

project = method.StablishConnection()
download_object = method.DownloadObject(project)
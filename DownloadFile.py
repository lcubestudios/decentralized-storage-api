#!/usr/bin/python3
from Classes import *

creds = Credentials()
method = Methods()

project = method.StablishConnection()
download_object = method.DownloadObject(project)
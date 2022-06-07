#!/usr/bin/python3
print()
from array import array
from datetime import datetime
from uplink_python.errors import StorjException, BucketNotEmptyError, BucketNotFoundError
from uplink_python.module_classes import ListObjectsOptions, Permission, SharePrefix
from uplink_python.uplink import Uplink
from dotenv import load_dotenv
import os
import cgi
import cgitb; cgitb.enable()
import json

# LOAD CONTAINER VARIABLES
load_dotenv()

class Credentials():
    def __init__(self):
        # Storj configuration information
        global api_key, satellite, encryption_passphrase, bucket, domain
        api_key =  os.getenv('API_KEY')
        satellite = os.getenv('SATELLITE')
        encryption_passphrase = os.getenv('ENCRYPTION_PASSPHRASE')
        domain = os.getenv('DOWNLOAD_DIR')
        bucket = "uplink"

class Methods():

    def StablishConnection(self):
        try:
            # create an object of Uplink class
            uplink = Uplink()
            # request access using passphrase
            #print("\nRequesting Access using passphrase...")
            access = uplink.request_access_with_passphrase(satellite, api_key,
                                                            encryption_passphrase)
            #print("Request Access: SUCCESS!")
        
            # open Storj project
            #print("\nOpening the Storj project, corresponding to the parsed Access...")
            project = access.open_project()
            #print("Desired Storj project: OPENED!")
            return project
            #
        except StorjException as exception:
            print("Exception Caught: ", exception.details)

    def EnlistAllBuckets(self,project):
        try:
            # enlist all the buckets in given Storj project
            #print("\nListing bucket's names and creation time...")
            bucket_list = project.list_buckets()
            json_output = []
            for bucket in bucket_list:
                # as python class object
                # print(bucket.name, " | ", datetime.fromtimestamp(bucket.created))
                # # as python dictionary
                data = bucket.get_dict()
                json_output.append(data)
            print(json_output)
            #print("Buckets listing: COMPLETE!")
            #
        except StorjException as exception:
            print("Exception Caught: ", exception.details)

    def ListObject(self,project):
        try:
            # list objects in given bucket with above options or None
            #print("\nListing object's names...")
            objects_list = project.list_objects(bucket, ListObjectsOptions(recursive=True,
                                                                            system=True))
            # print all objects path
            json_output = []
            for obj in objects_list:
                # print(obj.key, " | ", obj.is_prefix)  # as python class object
                # print(obj.get_dict())  # as python dictionary
                data = obj.get_dict()
                json_output.append(data)
            print(json.dumps(json_output))
            #print("Objects listing: COMPLETE!")
            #
        except StorjException as exception:
            print("Exception Caught: ", exception.details)

    def UploadObject(self,project,file_item):
        try:
            if file_item.filename:
                # strip the leading path from the file name
                fn = os.path.basename(file_item.filename.replace("\\", "/" ))
                #
                # open read and write the file into the server
                file_handle = file_item.value
                # get upload handle to specified bucket and upload file path
                upload = project.upload_object(bucket, file_item.filename)
                #
                # upload file on storj
                upload.write_file(file_handle)
                #
                # commit the upload
                upload.commit()
                # close file handle
                #file_item.close()
                print("Upload: Complete!")
                
        except StorjException as exception:
            print(json.dumps({"status": 500, "message": exception.details}))
    
    def DownloadObject(self,project,file_name):
        try:
            #file_handle create file, donwload = binary data
            file_handle = open('tmp/' + file_name, mode="wb")
            #get download handle to specified bucket and object path to be downloaded
            download = project.download_object(bucket, file_name) #Bucket, filename inside bucket
            #
            # download data from storj to file
            download.read_file(file_handle)
            # 
            # close the download stream
            download.close()
            file_handle.close()
            #print(json.dumps("message: Download Complete"
            url = domain + file_name
            print(json.dumps({"status": 200, "url": url}))
            #
        except StorjException as exception:
            print("Exception Caught: ", exception.details)

    def DeleteItems(self,project,file_item):
        try:
            project.delete_object(bucket, file_item)
        except StorjException as exception:
            print(json.dumps({"status": 500, "message": exception.details}))

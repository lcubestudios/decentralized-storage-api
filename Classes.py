from datetime import datetime
from uplink_python.errors import StorjException, BucketNotEmptyError, BucketNotFoundError
from uplink_python.module_classes import ListObjectsOptions, Permission, SharePrefix
from uplink_python.uplink import Uplink
from dotenv import load_dotenv
import os

# LOAD CONTAINER VARIABLES
load_dotenv()

class Credentials():
    def __init__(self):
        # Storj configuration information
        global api_key, satellite, encryption_passphrase, bucket, storj_file_name, src_full_name, destination_full_filename
        api_key =  os.getenv('API_KEY')
        satellite = os.getenv('SATELLITE')
        encryption_passphrase = os.getenv('ENCRYPTION_PASSPHRASE')
        bucket = "uplink"
        storj_file_name = "luis/ipfs.png" # (path + filename) OR filename
        src_full_name = "/Users/cloudninja/Desktop/ipfs.png" # Source and destination path and file name for testing
        destination_full_filename ="/Users/cloudninja/Desktop/ipfs3.png "

class Methods():

    def StablishConnection(self):
        try:
            # create an object of Uplink class
            uplink = Uplink()
            # request access using passphrase
            print("\nRequesting Access using passphrase...")
            access = uplink.request_access_with_passphrase(satellite, api_key,
                                                            encryption_passphrase)
            print("Request Access: SUCCESS!")
        
            # open Storj project
            print("\nOpening the Storj project, corresponding to the parsed Access...")
            project = access.open_project()
            print("Desired Storj project: OPENED!")
            return project
            #
        except StorjException as exception:
            print("Exception Caught: ", exception.details)

    def EnlistAllBuckets(self,project):
        try:
            # enlist all the buckets in given Storj project
            print("\nListing bucket's names and creation time...")
            bucket_list = project.list_buckets()
            for bucket in bucket_list:
                # as python class object
                print(bucket.name, " | ", datetime.fromtimestamp(bucket.created))
                # as python dictionary
                print(bucket.get_dict())
            print("Buckets listing: COMPLETE!")
            #
        except StorjException as exception:
            print("Exception Caught: ", exception.details)
    
    def ListObject(self,project):
        try:
            # list objects in given bucket with above options or None
            print("\nListing object's names...")
            objects_list = project.list_objects(bucket, ListObjectsOptions(recursive=True,
                                                                            system=True))
            # print all objects path
            for obj in objects_list:
                print(obj.key, " | ", obj.is_prefix)  # as python class object
                print(obj.get_dict())  # as python dictionary
            print("Objects listing: COMPLETE!")
            #
        except StorjException as exception:
            print("Exception Caught: ", exception.details)

    def UploadObject(self,project):
        try:
            # upload file/object
            print("\nUploading data...")
            # get handle of file to be uploaded
            file_handle = open(src_full_name, 'r+b')
            # get upload handle to specified bucket and upload file path
            upload = project.upload_object(bucket, storj_file_name)
            #
            # upload file on storj
            upload.write_file(file_handle)
            #
            # commit the upload
            upload.commit()
            # close file handle
            file_handle.close()
            print("Upload: COMPLETE!")
            #
        except StorjException as exception:
            print("Exception Caught: ", exception.details)
    
    def DownloadObject(self,project):
        try:
             # download file/object
            print("\nDownloading data...")
            # get handle of file which data has to be downloaded
            file_handle = open(destination_full_filename, 'w+b')
            # get download handle to specified bucket and object path to be downloaded
            download = project.download_object(bucket, storj_file_name)
            #
            # download data from storj to file
            download.read_file(file_handle)
            #
            # close the download stream
            download.close()
            # close file handle
            file_handle.close()
            print("Download: COMPLETE!")
            #
        except StorjException as exception:
            print("Exception Caught: ", exception.details)
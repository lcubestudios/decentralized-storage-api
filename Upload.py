#!/usr/bin/python3
print('Access-Control-Allow-Origin:*')
print('Access-Control-Allow-Headers: *')
print('Access-Control-Allow-Methods: *')
# print("Content-type:text/html")
print()
from Classes import *
creds = Credentials()
method = Methods() 
form = cgi.FieldStorage()

fileitem = form['filename']
project = method.StablishConnection()
upload_object = method.UploadObject(project,fileitem)

# in_memory = io.BytesIO(b' hello', )
# #in_memory.seek(0, 2)
# in_memory.write(b' world')
# #in_memory.seek(0)
# print(in_memory.getvalue())

#fileitem = form['filename']
# def regular_io(fileitem):
#     with open(fileitem, mode="r", encoding="utf8") as file_obj:
#         text = file_obj.read()
#         print(text)

# regular_io("tmp/Bro-aaron.jpeg")

# fileitem = 'tmp/Bro-aaron.jpeg'
# with open(fileitem, mode="rb") as file_obj:
        #Read file line by line then loop
        # for line in file_obj:
        #     text = file_obj.readline()
        #     print(line, end='')
        #Read file in 100 characters then loop
        # size_to_read = 100
        # text = file_obj.read(size_to_read)
        # while len(text) > 0:
        #     print(text, end='')
        #     text = file_obj.read(size_to_read)
        #Read full file and print binary
        #text = file_obj.read()
        #print(text)
        #Make a copy of a filee
        # with open('tmp/Bro-aaron-copy.jpeg', mode="wb") as file:
        #     for line in file_obj:
        #         file.write(line)
        
# fileitem = form['filename']
# data = fileitem.value
# with open("tmp/copy.jpeg", mode="wb") as file:
#         file.write(data)

# if fileitem.filename:
#     fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
#     with open(fileitem.filename, mode="rb") as file_obj:
#         data = file_obj.read()
#         print(data)
# else:
#     message = "Something failed"


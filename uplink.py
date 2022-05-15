Download.py line 121        
        print('Content-Type:application/octet-stream; name = \"text.txt\"')
        print('Content-Disposition: attachment; filename = \"text.txt\"')
        if not buffer_size:
            buffer_size = COPY_BUFSIZE
        file_size = self.file_size()
        if buffer_size > file_size:
            buffer_size = file_size
        while file_size:
            buf, bytes_read = self.read(buffer_size)
            if buf:
                #file_handle.write(buf)
                print(buf)
            file_size -= bytes_read


upload.py line 109

  buf = file_handle
        self.write(buf, len(buf))



Classes.py line 99
file_handle = file_item.value

import zipfile

new = zipfile.ZipFile('/Users/anmunju/Documents/multicam_ds/pythonStudy/Day10/today_file_list.zip', 'w')
new.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
new.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
new.write('file3.txt', compress_type=zipfile.ZIP_DEFLATED)
new.close()
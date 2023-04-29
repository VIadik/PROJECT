import zipfile
import os

# https://realpython.com/python-zipfile/

os.chdir("documents")
file_name = max(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)

with zipfile.ZipFile("archive.zip", mode="w") as archive:
    archive.write(f"{file_name}")

# old_file = 'archive.zip'
# destination_file = 'files/archive.zip'
#
# os.rename(old_file, destination_file)

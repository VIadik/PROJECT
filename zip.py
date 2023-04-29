import zipfile
import os

# https://realpython.com/python-zipfile/

file_name = sorted(os.listdir("files/documents"))[-1]

with zipfile.ZipFile("archive.zip", mode="w") as archive:
    archive.write("files/documents/file_0.pdf")

old_file = 'archive.zip'
destination_file = 'files/archive.zip'

os.rename(old_file, destination_file)

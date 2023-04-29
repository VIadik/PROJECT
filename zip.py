import zipfile
import os

# https://realpython.com/python-zipfile/

file_name = sorted(os.listdir("files/documents"))[-1]

with zipfile.ZipFile("archive.zip", mode="w") as archive:
    archive.write("files/documents/file_0.pdf")

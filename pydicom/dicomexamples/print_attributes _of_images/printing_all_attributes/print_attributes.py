import pydicom
import os



insert_image_path  = str(input("insert_image_path"))

data_set = pydicom.read_file(insert_image_path)

print(data_set)

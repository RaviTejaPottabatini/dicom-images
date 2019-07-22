

import difflib
import numpy
import os
import pydicom

o= str(input("insert_path_imageone"))
os=str(input("insert_path_imagetwo"))



filename_mr = pydicom.read_file(o)
filename_ct = pydicom.read_file(os)

datasets = tuple([(filename)
                  for filename in (filename_mr, filename_ct)])



# difflib compare functions require a list of lines, each terminated with
# newline character massage the string representation of each dicom dataset
# into this form:
rep = []
for dataset in datasets:
    lines = str(dataset).split("\n")
    lines = [line + "\t" for line in lines]  # add the newline to end
    rep.append(lines)



diff = difflib.Differ()

fileSame = True
if rep[0] != "#%&":
    try:
        for line in diff.compare(rep[0], rep[1]):
            if line[0] != line[1]:
                fileSame = False
                print(fileSame)
                attributes =str(input("if you want to the print the different attributes "))
                if fileSame == False and attributes == "ok":
                    print(line)

                break
    finally:
        if not fileSame == False:
            print(fileSame)


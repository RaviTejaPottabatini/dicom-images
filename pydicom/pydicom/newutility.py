import pydicom
import os
import numpy as np
import difflib

insert_image_path_1 = input("link of the image 1")
insert_image_path_2 = input("link of the image 2")

"""ds is the dataset of image one 
   dss is the dataset of image two"""


ds = pydicom.read_file(insert_image_path_1)
dss = pydicom.read_file(insert_image_path_2)


def print_attributes1(ds):
    """Go through all items in the dataset and print them with custom format and printing them"""
    print(ds)





def print_attributes2(dss):
    """Go through all items in the dataset and print them with custom format and printing them"""
    print(dss)


def compare_images(ds,dss):


    reqatt = [ds[0x29,0x1023],ds[0x28,0x10],ds[0x28,0x011],ds[0x28,0x100],ds[0x28,0x101],ds[0x28,0x102],ds[0x28,0x08],ds[0x28,0x04],ds[0x28,0x02]]
    reqatt2 = [dss [0x29,0x1023],ds[0x28,0x10],ds[0x28,0x011],ds[0x28,0x100],ds[0x28,0x101],ds[0x28,0x102],ds[0x28,0x08],ds[0x28,0x04],ds[0x28,0x02]]

    datasets = tuple([(filename)
                      for filename in (reqatt, reqatt2)])

    # difflib compare functions require a list of lines, each terminated with
    # newline character massage the string representation of each dicom dataset
    # into this form:
    rep = []
    for dataset in datasets:
        lines = str(dataset).split("\n")
        lines = [line + " \n" for line in lines]  # add the newline to end
        rep.append(lines)

        """
        Variable diff  is  from difflib  import Differ """

    diff = difflib.Differ()

    """ Intializing filesame as true as default  """


    filesame = True
    if rep[0] != "$%^^%":
        try:

            """ In for loop from diff variable comparing two attributes"""

            for line in diff.compare(rep[0], rep[1]):
                if line[0] != line[1] and line[0] != "?":

                    """If attributes are noy equal the filesame turns to False"""

                    filesame = False
                    print(filesame)
                    attributes = str(input("if you want to the print the different attribute "))
                    if filesame == False and attributes == "yes":
                        print(line)
                        break
                    else:
                        break




        finally:
            """ If attributes are same then try loop breaks and prints True  """
            if not filesame == False:
                print(filesame)



requried_action = str(input("pleaseenterrequriedaction"))

if requried_action == "attributesofimageone":
    (print_attributes1(ds))

elif requried_action == "attributesofimagetwo":
    (print_attributes2(dss))

elif requried_action == "compare":
    (compare_images(ds,dss))





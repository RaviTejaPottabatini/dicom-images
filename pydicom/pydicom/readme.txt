This is the summary for contributing code, testing ,reading, and for issues. Please read it carrefully to help making the code.

  
 1. instal numpy for getting pixel data 
 
 2. install os for input link of the DICOM image,file from the user
 3. install pydicom for reading the images of dicom format
 4. install difflib for compare the dicom images 




   
  PYDICOM:
   pydicom is a pure python package for inspecting, modify,working with DICOM images, files and data in a easy way. As a pure python package, pydicom can run anywhere and we hae just install pydicom package and numpy package for pixel data.

   pydicom is not sever or anything it is just apackae for viewing DICOM images,files.We can manipulate data elemnts in DICOm files with python code.

   limitations --for files with compressed pixel data, but it can store pixel data. Files can read (including compressed pixel data).

difflib :
This is a class for comparing sequences of lines of text, and producing human-readable differences or deltas

os :The OS module in python provides functions for interacting with the operating system. OS, comes under Python’s standard utility modules. This module provides a portable way of using operating system dependent functionality.and helps to read the link we have given.


 utility.py



In this python file we used : pydicom
                              os
                              difflib
                              numpy
			      pandas
                              
 first we input both DICOM images link and we enter the requried action in
 1.attributesofimageone
   it prints the attributes of image one
 
2.attributesofimagetwo
  it prints the attributes of image two
3.compare

 in compare if you want to print the attributes which differ by "yes" we can print the requried attribute 
 
 
 
 
 in all dicom images som of them are important to be equal and the requried attributes are comapred in newutility.py
 



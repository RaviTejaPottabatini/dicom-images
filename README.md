

DICOM IMAGES:


1.Use python3 and Download pychram-community by jet-brains the latest version
2.install pip and install pydicom 

  PYDICOM:
   pydicom is a pure python package for inspecting, modify,working with DICOM images, files and data in a easy way. As a pure python package, pydicom can run anywhere and we hae just install pydicom package and numpy package for pixel data.

   pydicom is not sever or anything it is just apackae for viewing DICOM images,files.We can manipulate data elemnts in DICOm files with python code.

   limitations --for files with compressed pixel data, but it can store pixel data. Files can read (including compressed pixel data).

3.There are some additional libraries and packages for modifing and comparing DICOM files those are will be written in a new file in further.   
 
comparing two dicom images and format the output of data set of dicom images 

IF you are not using pycharm--jetbrains:----

DICOM IMAGES:
IN WINDOWS

1.download python3.7 or any python3 from python.org, download executable installer
  and run the installer and add python3 to path on dialog that appers 
  

2.  Navigate to the directory in which Python was installed on the system. 


In our case, it is C:\Users\Username\AppData\Local\Programs\Python\Python37 since we have installed the latest version.

 verify python was successfully, install by double click python.exe and the python terminal will open


3. first check if pip was installed in your windows.Pip is a powerful package management system for Python software packages. Thus, make sure that you have it installed.

4.open terminal or command prompt and enter pip -v in the console.If pip was installed , you should see the pip version 

Pip has not been installed yet if you get the following output:
    'pip' is not recognized as an internal or external command.

5. if it is not installed 
   STEP1:download PIP get-pip.py

 Before installing PIP, you’ll need to download get-pip.py: get-pip.py on pypa.io.

Download the file to a temporary folder in Windows or to the “Downloads” library of your Windows installation. You can download the file to anywhere but remember where it’s been saved.
 STEP2: Pip is a command line program.so open 
       open command prompt
   
       To install pip type python get-pip.py

   to check pip :
    type pip --version this will report pip version.

and configure the pip 
 On Windows, the configuration file is: %HOME%\pip\pip.ini.
or on %appdata% 

You can set a custom path location for this config file using the environment variable.PIP_CONFIG_FILE.

6. add python path to the environment variables 

   open  system properties window and navigate advanced tab                      
   and select enviorment variables.
   edit the path variables 
  Select the Variable value field. Add the path to the python.exe file preceded with a semicolon (;). and select ok

By setting this up, you can execute Python scripts like this: Python script.py

Instead of this: C:/Python34/Python script.py


7. install numpy and matplotlib
   open a cmd window like before. Use the next set of commands to install NumPy and Matplotlib:

python - pip install numpy 
python -m pip install matplotlib
 
after installing check version (matplotlib is optinal)

8. install os 
  os is standard library so we need to download it and add to python 
 or 
 if it is the latest version, you have os already

9. install difflib 
  you can use 
              apt-get install npm

              npm install difflib
if you are using latest it maybe comes in it. 

 or 
  http://pydicom.readthedocs.org/en/latest/getting_started.html

Download pydicom-master.zip source code. 
Run: python setup.py install.  In python: import pydicom


10 install pydicom 
   you can use 
     python -m pip install pydicom 




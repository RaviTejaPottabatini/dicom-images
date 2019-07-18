In LINUX:

here is a very good chance your Linux distribution has Python installed already, but it probably won’t be the latest version, and it may be Python 2 instead of Python 3.


depending on the ubuntu version the python 3 or python 2 is installed 

Ubuntu 17.10, Ubuntu 18.04 (and above) come with Python 3.6 by default. You should be able to invoke it with the command python3.

Ubuntu 16.10 and 17.04 do not come with Python 3.6 by default, but it is in the Universe repository.
so,
$ sudo apt-get update
$ sudo apt-get install python3.
you can invoke it.

but, for Ubuntu 14.04 or 16.04, Python 3.6 is not in the Universe repository, and you need to get it from a Personal Package Archive

$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.6

1. install pip 
Start by updating the package list using 
$sudo apt update

2.you can use this to install pip :
$sudo apt install python3-pip
and check the verison of pip.
 you can install packages by pip.

3. you can pydicom by 
sudo aptitude install mercurial
hg clone https://code.google.com/p/pydicom/
cd pydicom/source/; sudo python setup.py install


It will be installed into /usr/local/lib/python2.7/dist-packages/pydicom-1.0.0a-py2.7.egg 


4. how to run python in ubuntu :
       you have to go to the directiory for run the python file.
run -- python3 in terminal
    --  check the dir for getting the pyhon file 
and -- python3 test.py 
   then the requried file will run on the terminal
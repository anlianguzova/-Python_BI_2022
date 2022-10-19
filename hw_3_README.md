# Python_BI_2022


This repository contains the homeworks for the Python course (September-December, 2022) in the Bioinformatics Institute.


## Homework_3: ultraviolence


This homework (launch of the file *ultraviolence.py*) was conducted using Ubuntu 20.04.01 (64-bit type) and python version 3.11.0rc2. 


### Instructions for use


#### Install/update prerelease of the suitable python version
The official release date of python ver 3.11 is 2022-10-24. Thus, first, we have to install the last prerelease of the python (which is 3.11.0rc2). The easiest way to update the python version on Ubuntu is through the terminal using following commands:


1. `sudo add-apt-repository ppa:deadsnakes/ppa`, `sudo apt update`, `sudo apt install python3.11` — updating/installing python 3.11;


2. `sudo apt install python3.11-dev` — development headers for building and compiling C++ extensions;


3. `sudo apt install python3.11-venv` — enable to create virtual environments.


#### Install required packages 


The next step is to launch your favourite software for Python (I have used PyCharm Professional). Note, that for correct processing of the script you should create a separate virtual environment in the folder where the script is located (in my case it was */media/al/TOSHIBA EXT/IB/Pyth_course/homeworks/homework_3*). In PyCharm it is created when you choose a Python interpreter (*Settings > Project > Add Interpreter > Add local interpreter > Virtualenv Environment: New: Base interpreter: python 3.11*).


Then you are able to install required packages using pip in the terminal (PyCharm has its own field for the terminal). Enter `<path_to_the_venv/bin/python> -m pip install -r requirements.txt` (requirements.txt is located in this branch, download it to the folder with *ultraviolence.py*). You can also install every package separately using the `<path_to_the_venv/bin/python> -m pip install <package name>` command or adding packages through the Settings > Python interpreter. 


<sup><sub>Remark: for some reason I couldn't install Biopython properly in the first place, however, everything became fine after I repeated commands for C compilers and virtual environments in the terminal.</sub></sup>


After that you can run the script and see the cute encouragement :)

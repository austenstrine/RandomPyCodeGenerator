# RandomPyCodeGenerator
A program that randomly generates Python code, and then filters based on the desired outcome

## Basic Function
  This is a code generation program. You can input a given integer, and input a desired output(also an integer). It will specifically test to make sure that the output changes with the input. It has a very simple GUI that lets you control the boundaries of code generation, and present the user with those files that successfully generate the desired output, given the input. Later on I would like to have it track which ‘decisions’ are better for generating the desired output, and alter the way it generates code, so it can ‘learn’ as it generates code how better to generate code.

## Purpose
  This program is aimed solely towards teaching myself about artificial intelligence development and machine learning, and in the short term it will just be geared towards quickly generating code at a level similar in quality to human code, but quicker. It has GUI designed to make it easy to use, requires less comprehension of the code, and more utility. If done properly, the ability to auto-generate code within specified boundaries is an extremely appealing tool for any programmer.
  
  I wanted it to be as fast as possible, because the more useful it is, the more complex it will be. I’m having the compiler do much of the work for me in terms of determining whether the generated code is functional by having it run the generated code in RAM. 

## Practical Aplication
  I don’t know of any GUI equipped program designed to generate code for developers, aside from certain GUI creation IDE’s. This would be, hopefully, more useful than that. Instead of generating code for widgets, it would generate code for logical problems, potentially allowing for a deeper level of abstraction than what the programming language in question provides without actually ‘hiding’ the code, allowing for less abstraction if desired.
  
  How useful this is will change as it is developed. As far as I've gotten, it’s not super useful, since I'm only working with converting one integer into another – a simple calculator can do as much. But as the program grows more advanced, and hopefully to a lesser degree more complex, it will be able to generate code that is comparatively very time consuming for a human to generate.
  
  This will be useful on two fronts: One, code that is easy to understand and write, but simply takes a long time, and Two, code that is difficult to understand and therefore write, and therefore takes a lot of time. Being able to plug in logic instead of variables, and having a program that, in the fastest, and most efficient way possible, generates the code for you is exciting. If done in a way that is intelligible to human eyes, possibly revolutionary(and extensive).

  Obviously, the more complex the math/processing required to get the desired output, the more difficult it is to program an algorithm that is able to track and understand the function and purpose of the elements it is manipulating for that purpose. To simplify the logic, I had it only deal with integer input and output. This is temporary.

## Dirty Code
  I use the built-in `exec()` function to have the compiler assess the code for me. Since it doesn't return an input, per se, yet allows printing to sys.stdout, I swap out sys.stdout for the duration of the code's run, and also have a print statement before every return statement. Then the object that was sys.stdout while the program was running has the result of the code.
  
  I initially was concerned about the scalability - I couldn't figure out how to get all the processing done in RAM instead of on the disk, but when I discovered that I could use `exec()`, that fixed that.
  
  It's a little messy for now, but it will continue to progress as I work on it. Feel free to tinker, and download/run! Should be compatible with any operating system that has Python 3. 
  
## Running the Program
### Windows
  Download .zip and unzip. Double-click the finalRunner, and it'll pop up - just make sure it's not opening it automatically in an IDE.
### Mac OS
#### Python Launcher
  Locate `finalRunner.py`. Right-click it, and open with Python Launcher. It should open immediately.
#### Terminal method for beginners:
  Open Terminal. It's in applications>utilities. Issue the `ls` command to display the names of all files/folders in the working directory(current folder). See if the working directory(current folder) contains `finalRunner.py`. If it doesn't, navigate until you get to the correct directory/folder. Use `cd folderName` to open a folder and make it the current working directory, where `folderName` is the name of the folder in the current directory you would like to navigate to. Use `cd ..` to navigate to the parent folder and make that the current working directory. (The parent folder is the folder your current working directory is in.) Every time you navigate to a new directory, enter `ls` again to get a list of the files and folders in that directory so you don't get lost. If you do get lost, just type in `cd ..` a few times until you see a falder name you recognize as the CWD.
  Once you're in the correct working directory, enter `pythonX.Y finalRunner.py` , where `X.Y` is the Python version on your computer. You cannot enter any other numbers than what your installed Python version is. Python 3.3 or higher is required, but 3.5 is recommended.  Once you've entered this command, the program will run!

Here's a sample of what it would look like when you successfully open the program:
```
Last login: Tue Dec 12 18:32:37 on ttys001
CSiMac1-40:~ student$ ls
Applications	Downloads	Music		Sites
Desktop		Library		Pictures	VirtualBox VMs
Documents	Movies		Public
CSiMac1-40:~ student$ cd Downloads
CSiMac1-40:Downloads student$ ls
Networking.rtf.docx			RandomPyCodeGenerator-master.zip
RandomPyCodeGenerator-master
CSiMac1-40:Downloads student$ cd RandomPyCodeGenerator-master
CSiMac1-40:RandomPyCodeGenerator-master student$ ls
GO.py		README.md	finalRunner.py	tester.py
LICENSE		__pycache__	pythonFinal.py
CSiMac1-40:RandomPyCodeGenerator-master student$ python --version
Python 2.7.11
CSiMac1-40:RandomPyCodeGenerator-master student$ **NOTE, the version it prints ^here^ is a lie because this school computer is weird. If yours is also weird, the open IDLE and go off of the version that IDLE gives**
-bash: **NOTE,: command not found
CSiMac1-40:RandomPyCodeGenerator-master student$ python3.5 finalRunner.py
```
  You can now celebrate! You've successfully opened the program! Yaaaayyy...
#### IDLE method
  Locate `finalRunner.py`. Right-click it, and open with IDLE. Once idle pops up, press f5 to run.
  
##### If any one of these methods do not work, definitely try all the others before giving up. Maybe even shoot me a message so I know what's working and what is not.

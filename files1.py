import os
import re
import shutil
from datetime import datetime
import sys


# logging all the commands given to a text file:
commandlog_path = "D:\Py4e\commandlog.txt"
fhand = open(commandlog_path,"a")

# logging all the commands given to a text file:
fhand.write("\n"+str(datetime.now())+"\n")
fhand.write("commands exec: "+"\n")
print("\n")

# pr function to print the data to terminal as well as the log file
def pr(p):
    print(p)
    fhand.write(p+"\n")

# checking for command line args passed to load the state
def cli():
    if len(sys.argv)>1:
        ar = sys.argv[1]
        if 'true' in ar.lower():
            ar = ar.split(",")
            curdir = ar[1][ar[1].index(':')+2:-2]
            pr(f"loading the state from command line arguments to {curdir}")
            return curdir
    else:
        pr("No command line args passed, continuing..")
        return None

# help-text function to print the usable commands in the program
def help_text():
    print("The actions that can be performed are: ")
    print("mkdir - create new directory use: 'mkdir folder_name'")
    print("cd - changes the current directory to mentioned directory if exists: 'cd folder_name'")
    print("ls - gets list of all files/folders in the current directory: 'ls' or 'ls folder_name'")
    print("grep - searches for a specific pattern in a file: 'grep file_name pattern")
    print("cat - prints the contents of a file: 'cat file_name'")
    print("touch - creates a new file: 'touch file_name'")
    print("echo - writes lines to a existing text file 'echo file_name' lines to be written can be entered when prompted")
    print("mv - moves specific file/folder to specified location: 'mv file_name/folder_name destination_path'")
    print("cp - copies the speccified file/folder to specified location: 'cp file_name/folder_name destination_path")
    print("rm - deletes the file/folder: 'rm file_name/folder_name'\n")

help_text()
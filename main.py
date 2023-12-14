from files1 import *

def file_mod():
    # variable to keep track of the no of commands executed
    i = 1

    # loop that runs until exit is given as a command
    while True:
        # tracking current directory each and every time, we are about to take a command
        current_dir = os.getcwd() # gets the current directory
        pr(f"We are now at: {current_dir}") # printing current directory

        #Input command
        command = input("Enter command: ").lower()
        # writing the command to the file commandlog
        fhand.write(f"{i}. {command} : ")
        command = command.split()

        #Handling stray space input
        if len(command)==0:
            pr("Stray spaces can't be treated as a command")
            help_text()
        #breaking the infinite loop
        elif command[0] == "exit":
            pr("Exiting the program\n")
            curr_state = os.getcwd()
            pr(curr_state)
            exit()
        #mkdir refers to creating a new folder, input is : "mkdir folder_name"
        elif command[0] == "mkdir":
            if os.path.exists(command[1]):
                pr("The folder with the given name already exists")
            else:
                os.mkdir(command[1])
                pr(f"New directory is created: {command[1]}")
        # cd refers to changing the current directory, 
        # input command: "cd folder"
        elif command[0] == "cd":
            if os.path.exists(command[1]):
                os.chdir(command[1])
                pr(f"The dir changed to {command[1]}")
            else:
                pr("The path doesnt exist")
        # ls refers to the listing all files, 
        #input command: "ls" returns list of files in current_directory
        # if input command is "ls folder" returns the list of files in that directory if exists
        elif command[0]=="ls":
            if len(command)>1:
                os.chdir(command[1])
            files = os.listdir()
            pr('The files in the directory are: '+','.join(files))
        # grep is to search for a particular pattern in a file
        # input command is: "grep myfile.txt"
        # Then it will ask about the pattern, enter to search
        elif command[0] == "grep":
            file_name = command[1]
            pattern = input(f"Enter pattern to search in the file {file_name}: ")
            # Open the file in read mode
            with open(file_name, "r") as f:
                # Read the file content line by line
                for line in f:
                    # Check if the line contains the pattern
                    if re.search(pattern, line):
                        # Print the line if it contains the pattern
                        print(line)
                else:
                    pr(f"{pattern} is not found in {file_name}")
        # cat is to print all the contents in the file name mentioned
        # input command should be, "cat myfile.txt"
        elif command[0] == "cat":
            file_path = command[1]
            # opening the file in read mode
            if os.path.exists(command[1]):
                with open(file_path,"r") as f:
                    # looping through lines of the file and printing them.
                    pr("File Opened and Printing lines in the file: ")
                    for line in f:
                        pr(line)
            else:
                pr(f"The file named {file_path} doesnt exist")
        # touch command is to create a new empty file,
        elif command[0] == "touch":
            if os.path.exists(command[1]):
                pr("Err- The file already exists")
            else:
                open(command[1],"w")
                pr(f"The file with name {command[1]} is created")
        # echo command is to write lines into a file
        # command should be: "echo myfile.txt"
        # then it will take input lines
        elif command[0] == "echo":
            # opening the file in append mode
            with open(command[1], "a") as f:
                # writes single line to the file
                f.write(input("Enter a line to write to the file:\n")+"\n")
            pr(f"Written a line to the file: {command[1]}")
        # mv command is to move files from one path to the other
        # command should be, "mv source_path destination_path"
        elif command[0] == "mv":
            #shutil.move(source_path,destination_path)
            file_path = f"{current_dir}\{command[1]}"
            shutil.move(file_path, command[2])
            pr(f"successfully moved {file_path} to {command[2]}")
        # cp command is to copy current directory to the other
        elif command[0] == "cp":
            file_path = f"{current_dir}\{command[1]}"
            shutil.copy2(file_path,command[2])
            if os.path.exists(f"{command[2]}\{command[1]}"):
                pr(f"successfully copied {file_path} to {command[2]}")
            else:
                pr("Error")
        # rm command is to delete the specific file or folder
        # command should be, "rm myfile.txt" or "rm folder"
        elif command[0] == "rm":
            file_path = f"{current_dir}\{command[1]}"
            # Check if the file exists
            if os.path.exists(file_path):
                # deleting the file
                os.remove(file_path)
                pr(f"File '{file_path}' removed successfully.")
            else:
                pr(f"File path '{file_path}' does not exist.")
        elif command[0] == "help":
            pr("Asked for help")
            help_text()
        else:
            pr("Incorrect command entered")
        i += 1
        print()


#driver code
if __name__ == "__main__":
    
    # checking for command line args and changing the current directory
    curr = cli() # a function in files1.py file

    if curr is not None:
        os.chdir(curr)

    # loads from where you have left off
    print("Do you want to load directory from where you have left of last time, y/n?")
    if(input().lower()=="y"):
        with open(commandlog_path, 'r') as file:
            lines = file.readlines()
            # Retrieve lines in reverse order starting from the last line
            lines.reverse()
            for line in lines:
                if line.startswith('D:'):
                    currdir = line.rstrip()
                    os.chdir(currdir)
                    pr(f"The directory is loaded to the where left last time: {currdir}")
                    break
    else:
        pr("Continuing with the program default directory: ")

    file_mod()
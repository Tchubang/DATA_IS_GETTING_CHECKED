import os
import time
import sys
import subprocess
# Function to search for a given string in a text file and print the entire line that contains the match


def search_and_print_line(file_path, search_string):
    # Open the file in read mode
    with open(file_path, "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Check if the search string is present in the line
            if search_string in line:
                # Print the entire line
                print('matched:', line)


def list_text_files(folder_path):
    # Get the list of all files in the given folder
    files = os.listdir(folder_path)
    # Iterate through the list of files
    for file in files:
        # Get the file path
        file_path = os.path.join(folder_path, file)
        # Check if the file is a text file
        if file.endswith(".txt"):
            # Print the file name

            print(file)


def restart_program():
    subprocess.call([sys.executable, __file__])
    sys.exit()


a = input("what do you want to be found? ", )


# Test the function
print("These files are available ")
list_text_files("D:\coding\python\FINAL PROGRAM\DATA_IS_MINE")
b = input("choose text file ")
print("file is ready for search")


a = a.removeprefix("0")

a = a.removeprefix("+92")
a = a.replace("-","")


# Test the function


search_and_print_line(b, a)

c = input("Press 0 for exit or Press 1 to continue and then hit Enter ")
if c > "0":
    restart_program()
else:
    sys.exit()

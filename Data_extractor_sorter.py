import os

word_to_search = "FN"
file_name =input("Please put your contacts file name in which you are going to extract data (dont forget to add extention .txt) ") 
output_file = input("Enter the name of output file (dont forget to add extention .txt) ")


try:
    with open(file_name, "r") as f:
        

        with open(output_file, "w") as f_out:
            line = f.readline()
            while line:
                if word_to_search in line:
                    f_out.write(line.rstrip() + "\n")
                    next_line = f.readline()
                    f_out.write(next_line.rstrip() + "\n")
                    line = f.readline()
except FileNotFoundError:
    print(f"{file_name} not found")

with open(output_file, "r") as file:
    # Read the contents of the file
    filedata = file.read()

# Replace the target string
filedata = filedata.replace("-", "")

# Write the file out again
with open(output_file, "w") as file:
    file.write(filedata)  

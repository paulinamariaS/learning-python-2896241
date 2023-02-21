

import os
from os import path


#def main():
# get a directory
#src = path.realpath("challenge_start.py")    
#root_dir, tail = path.split(src)

files_list = os.listdir()  # or just () if we want to do it in a current directory
onlyfiles = [f for f in files_list if os.path.isfile(os.path.join(root_dir, f))]

# loop to count total bytes in all the files:
totalbytes = 0
for i, filename in enumerate(onlyfiles):
    filepath = os.path.join(root_dir, filename)
    totalbytes += path.getsize(filepath)
    print(totalbytes)

# make a new folder
newpath = os.path.join(root_dir, "results")
if not os.path.exists(newpath):
    os.makedirs(newpath)

# make a new .txt files (for results), if it doesnt exist yet
#resultsfile = open(os.path.join(newpath, "results.txt"), "w+")
resultsfile = open("results/results.txt", "w+")

# Open the file for appending text to the end
resultsfile = open(os.path.join(newpath, "results.txt"), "a+" )    

# Write total amount of bytes into the files:
#Line1 = ["Totatl bytecount:", str(totalbytes), "\n"]
#resultsfile.writelines(Line1)  # writing multiple strings at a time
resultsfile.write("Total bytecount: " + str(totalbytes) + "\n")
resultsfile.write("Files list: \n______________ \n")
    
# Write the list of files names:
for i, filename in enumerate(onlyfiles):
    LineNext = [filename, "\n"]
    resultsfile.writelines(LineNext)

# # close the file when done
resultsfile.close() 

#if __name__ == "__main__":
#   main()






import os
from os import path


def main():
    # get a directory
    src = path.realpath("textfile.txt")    
    root_dir, tail = path.split(src)
    print("New folders path is:", root_dir)
    
    # make a new folder
    newpath = os.path.join(root_dir, "results")
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        # make a new .txt files (for results), if it doesnt exist yet
    
    #resultsfile = open("results.txt", "w+" )
    resultsfile = open(os.path.join(newpath, "results.txt"), "w+")

    # read all the files names
    totalbytes = 0
    size = path.getsize(src)
    print("the bytes size of the file is:", str(size))

    files_list = os.listdir(root_dir)
    #print(os.listdir(root_dir))
    #print(files_list[1])
    onlyfiles = [f for f in files_list if os.path.isfile(os.path.join(root_dir, f))]
    print(onlyfiles)

    # loop to count total bytes in all the files:
    totalbytes = 0
    for i, filename in enumerate(onlyfiles):
        filepath = os.path.join(root_dir, filename)
        totalbytes = totalbytes + path.getsize(filepath)
        print(totalbytes)

    # Open the file for appending text to the end
    resultsfile = open(os.path.join(newpath, "results.txt"), "a+" )    

    # Write total amount of bytes into the files:
    Line1 = ["Totatl bytecount:", str(totalbytes), "\n"]
    resultsfile.writelines(Line1)  # writing multiple strings at a time
    resultsfile.write("Files list: \n______________ \n")
    
    # Write the list of files names:
    for i, filename in enumerate(onlyfiles):
        LineNext = [filename, "\n"]
        resultsfile.writelines(LineNext)

    # # close the file when done
    resultsfile.close() 



if __name__ == "__main__":
   main()

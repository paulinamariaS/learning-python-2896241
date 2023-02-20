#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil        # use shell utilities for copying and archiving files
from shutil import make_archive 
from zipfile import ZipFile       # module which gives control over all zip archives  


def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt.bak"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt") # source variable
        
        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"  # destination variable,
                            # ".bak" is a filename extension signifies a backup copy of a file
        shutil.copy(src, dst)

        # rename the original file
        os.rename("textfile.txt", "newfile.txt")

        # now put things into a ZIP archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        # more fine-grained control over ZIP files
        # 'with' creates a local scope which simplifies working with objects
        with ZipFile("testzip.zip","w") as newzip:   
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")

      
if __name__ == "__main__":
    main()



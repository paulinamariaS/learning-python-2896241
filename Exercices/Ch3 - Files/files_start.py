#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#
# the classes to work with files are built into the python language


def main():  
    # Open a file for writing and create it if it doesn't exist
    myfile = open("textfile.txt", "w+" )  # open mode - this is the access that I want to the file
                                          # w - write, + - python should create the file if it already doesnt exist
    
    # Open the file for appending text to the end
    myfile = open("textfile.txt", "a+" )    # here we dont want to use 'w' because it will overright the file, we want to append the data so we use a

    # # write some lines of data to the file
    for i in range(10):
         myfile.write("This is some new text\n")
    
    # # close the file when done
    myfile.close() 
    
    # Open the file back up and read the contents
    myfile = open("textfile.txt", "r")
    if myfile.mode == 'r':
        contents = myfile.read()        # read function will just read entire contents at once
        print(contents)
        fl = myfile.readlines()       # hint, parameter inside parentheses, is the number of bytes to be red from the file
        print(fl)         # fl=file lines
        print(len(fl))
        for x in fl:
            print(x)

if __name__ == "__main__":
    main()

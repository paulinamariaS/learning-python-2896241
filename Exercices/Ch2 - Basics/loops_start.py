#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    # while(x < 5):
    #     print(x)
    #     x = x + 1

    # TODO: define a for loop
    # for x in range(5, 10):      # in python, unlike C or Matlab, rather than having an index variable, we have an iterator, in this case x 
    #     print(x)                # it excludes the last term, so '10' is not printed

    # TODO: use a for loop over a collection
    # days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    # for d in days:
    #     print(d)

    # TODO: use the break and continue statements
    # for x in range(5, 10):      # in python, unlike C or Matlab, rather than having an index variable, we have an iterator, in this case x 
    #     # if x ==7:
    #     #     break   # will cause for loop to terminate
    #     if x % 2 ==0:   # take x divide by two and continue
    #         continue    # skip the ones that dont meet the requirement
    #     print(x)        # this 'continue' statement will skip the print statement 

    # TODO: using the enumerate() function to get index 
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i,d in enumerate(days): # it is going to return the value of the index and days
        print(i ,d)
  
if __name__ == "__main__":
    main()

#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    # if x < y:
    #     result = "x is less than y"
    # elif x == y:
    #     result = "x is the same as y"        
    # else:
    #     result = "x is greater than y"

    # print(result)

    # conditional statements let you use "a if C else b"
    # result = "x is less than y" if x < y else "x is greater or equal to y"
    # print(result)

    # match-case makes it easy to compare multiple values
    value = "one"
    match value:  # list every possible case to match the values
        case "one":
            result=1
        case "two":
            result=2
        case "three"|"four":    # the vertival bar-> 'or' operator
            result=(3,4)
        case _:                 # this case will be handled in case any of the other cases was not executed
            result = -1
    print(result)

if __name__ == "__main__":
    main()
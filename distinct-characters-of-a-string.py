# Python3 program to print distinct
# characters of a string.
NO_OF_CHARS = 256
 
# Print duplicates present in the
# passed string
def printDistinct(str):
 
    # Create an array of size 256 and
    # count of every character in it
    count = [0] * NO_OF_CHARS
 
    # Count array with frequency of
    # characters
    for i in range (len(str)):
        if(str[i] != ' '):
            count[ord(str[i])] += 1
 
    # Print characters having count = 1
    for i in range(len(str)):
        if (count[ord(str[i])] == 1):
            print (str[i], end = "")
 
# Driver Code

str = "world Hello "
printDistinct(str)
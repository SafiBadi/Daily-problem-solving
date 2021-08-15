# Python3 program to find all distinct characters
# in a String
 
MAX_CHAR = 256
 
# Function to prdistinct characters in
# given Str[]
def printDistinct(Str):
 
    n = len(Str)
 
    # count[x] is going to store count of
    # character 'x' in Str. If x is not present,
    # then it is going to store 0.
    count = [0 for i in range(MAX_CHAR)]
 
    # index[x] is going to store index of character
    # 'x' in Str. If x is not present or x is
    # more than once, then it is going to store a value
    # (for example, length of String) that cannot be
    # a valid index in Str[]
    index = [n for i in range(MAX_CHAR)]
 
 
    # Traverse the input String
    for i in range(n):
         
        # Find current character and increment its
        # count
        x = ord(Str[i])
        count[x] += 1
 
        # If this is first occurrence, then set value
        # in index as index of it.
        if (count[x] == 1 and x !=' '):
            index[x] = i
 
        # If character repeats, then remove it from
        # index[]
        if (count[x] == 2):
            index[x] = n
 
 
    # Since size of index is constant, below operations
    # take constant time.
    index=sorted(index)
 
    for i in range(MAX_CHAR):
        if index[i] == n:
            break
        print(Str[index[i]],end="")
 
# Driver code
 
Str = "GeeksforGeeks"
printDistinct(Str)
 
# This code is contributed by mohit kumar 29
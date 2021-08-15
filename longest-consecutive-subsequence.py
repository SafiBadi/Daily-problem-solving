# Python program to find longest contiguous subsequence
 
def findLongestConseqSubseq(arr, n):
 
    ans = 0
 
    # check each possible sequence from the start
    # then update optimal length
    for i in range(n):
 
        # if current element is the starting
        # element of a sequence
        if (arr[i]-1) not in arr:
 
            # Then check for next elements in the
            # sequence
            j = arr[i]
            while(j in arr):
                j += 1
 
            # update  optimal length if this length
            # is more
            ans = max(ans, j-arr[i])
    return ans
 
 
# Driver code

n = 7
arr = [1, 9, 6, 10, 4, 20, 2, 5]

print ( "Length of the Longest contiguous subsequence is" )
print ( findLongestConseqSubseq(arr, n) )
 

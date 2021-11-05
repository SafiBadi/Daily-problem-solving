# Fierst thaught in mind is to applay brute force
# But this approach is time consuming when using bruteforce due to multiplication and dividion

class Solution:

    # Brute force
    # Here I run simple while loop and keep our coins decrementing on each step
    # Time complexity : O(n)
    # Space complexity : O(1)
    def arrangeCoins(self, n):
        k = 1
        while n>0:
            n = n-k
            k += 1

        if n == 0:
            return k-1
        else:
            return k-2

    # Applay Math
    # sum of 1,2,3....n = n(n+1)/2 
    # Here,
    # k(k+1)/2 <= n
    # Solve the equation using compleate square technique
    # Time complexity : O(1)
    # Space complexity : O(1)
    def arrangeCoins2(self, n):
        k = int( ( (2*n + 0.25)**0.5) - 0.5 ) #Here we use int() for finding floor value of k. We can use floor() function instead.
        return k

ans = Solution()

print( ans.arrangeCoins2(1) )

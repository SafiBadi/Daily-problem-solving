class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
        n = A

        pd = 0

        while(n>0):
            pd = (pd*10) + (n%10)
            n //= 10

        if A-pd == 0:
            return 1
        else:
            return 0
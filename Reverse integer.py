class Solution:
	# @param A : integer
	# @return an integer
	def reverse(self, A):
        if A<0:
            A = A*(-1)

            n = 0
            while A>0:
                n = n*10 + (A%10)
                A = A//10

            if -n < -2147483647:
                return 0
            else:
                return -n

        else:
            n = 0
            while A>0:
                n = n*10 + (A%10)
                A = A//10

            if n > 2147483647:
                return 0
            else:
                return n
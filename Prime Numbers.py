class Solution:
	# @param A : integer
	# @return a list of integers
	def sieve(self, A):
        if A<= 1:
            return

        lst = list()

        if A == 2:
            lst.append(2)
            return lst

        for i in range(2,A+1):
            prime = True
            for j in range(2, int( math.sqrt(i) ) + 1):
                if i%j == 0:
                    prime = False
                    break
            if prime is True:
                lst.append(i)

        return lst

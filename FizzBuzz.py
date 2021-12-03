class Solution:
	# @param A : integer
	# @return a list of strings
	def fizzBuzz(self, A):
        lst = list()

        for i in range (1,A+1):
            if i%3 == 0:
                if i%5 == 0:
                    lst.append('FizzBuzz')
                else:
                    lst.append('Fizz')
            elif i%5 == 0:
                lst.append('Buzz')
            else:
                lst.append(i)

        return lst

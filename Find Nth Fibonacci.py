class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1:
            return 1
        elif A == 2:
            return 1

        fib1 = 1
        fib2 = 1

        i = 3

        while(i<=A):
            fib = fib1 +fib2

            fib1 = fib2
            fib2 = fib

            i += 1

        return (fib % 1000000007)

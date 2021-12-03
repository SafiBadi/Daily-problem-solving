class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if A > B:
            used = B-C+1
            ans = (A - used) % B
            return ans
        else:
            ans = C+A-1

            if ans > B:
                return ans%B
            else:
                return ans
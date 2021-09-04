# ERROR in Answer
# https://leetcode.com/contest/biweekly-contest-60/problems/find-all-groups-of-farmland/

class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        m = len(land)
        n = len(land[0])
        
        r1=c1=r2=c2 = None
        answer = list()

        for i in range(m):
            for j in range(n):

                if land[i][j] == 1:
                    r1 = i
                    c1 = j
                    for k in range(m-i):
                        if land[k][j] != 1:
                            for l in range(n-j):
                                if land[k][l] != 1:
                                    r2 = k
                                    c2 = l-1
                                    break
                            break
                    answer.append([r1,c1,r2,c2])
        
        return answer



aa = Solution()
lst = [[1,0,0],[0,1,1],[0,1,1]]

ans = aa.findFarmland(lst)
print(ans)
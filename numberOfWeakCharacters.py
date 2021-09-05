# https://leetcode.com/contest/weekly-contest-257/problems/the-number-of-weak-characters-in-the-game/
# Work on TLE

class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:

        record = dict()

        for i in properties:
            if record.get(i[0],0) > 0:                
                if i[1] > record[i[0]]:
                    record[i[0]] = i[1]
            else:
                record[i[0]] = i[1]

        sortedrecord = (record.items())
        #print(sortedrecord)

        WEAK = 0
        for i in properties:
            for j in reversed(sortedrecord):
                if j[0] > i[0] and j[1] > i[1]:
                    WEAK +=1
                    break
        
        return(WEAK)



        







aa =Solution()
zz= [[1,5],[10,4],[4,3]]
ans = aa.numberOfWeakCharacters(zz)
print(ans)
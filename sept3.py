# https://leetcode.com/problems/erect-the-fence/
# Two point equation of line: https://www.cuemath.com/geometry/two-point-form/
# Point lies above or below the line: https://www.emathzone.com/tutorials/geometry/position-of-point-with-respect-to-line.html#:~:text=If%20y%20is%20the%20ordinate,equation%20of%20the%20line%2C%20i.e.&text=Next%20we%20consider%20the%20difference%20y1%E2%80%93y%2C%20i.e.&text=(a)%20If%20the%20point%20A,y1%E2%80%93y%3E0.

class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        temp = trees
        temp.sort()
        print(temp)

        fence = list()
        fence.append(temp[0])
        #print(fence)

        #upper fence building
        current = fence[-1][0]
        for i in range(len(temp)):
            if current == temp[i][0]:
                continue
            else:
                if fence[-1] != temp[i-1]:
                    fence.append(temp[i-1])
                    current = temp[i][0]
                
                while len(fence)>= 3:
                    x = fence[-2][0]
                    y = fence[-2][1]

                    x1 = fence[-3][0]
                    y1 = fence[-3][1]

                    x2 = fence[-1][0]
                    y2 = fence[-1][1]

                    a = y1 - y2
                    b = x2 - x1
                    c = x1*y2 - y1*x2

                    if ( a*x + b*y + c < 0 and b>0 ) or ( a*x + b*y + c > 0 and b<0 ):
                        del fence[-2]
                    else:
                        break
        fence.append(temp[-1])
        while len(fence)>= 3:
                    x = fence[-2][0]
                    y = fence[-2][1]

                    x1 = fence[-3][0]
                    y1 = fence[-3][1]

                    x2 = fence[-1][0]
                    y2 = fence[-1][1]

                    a = y1 - y2
                    b = x2 - x1
                    c = x1*y2 - y1*x2

                    if ( a*x + b*y + c < 0 and b>0 ) or ( a*x + b*y + c > 0 and b<0 ):
                        del fence[-2]
                    else:
                        break
        #print(fence) #see the result of upper fence buildng
        

        #upper fence building
        fb = list()
        fb.append(temp[0])
        for i in range(len(temp)):
            if fb[-1][0] == temp[i][0]:
                continue
            else:
                if fb[-1] != temp[i]:
                    fb.append(temp[i])
                
                while len(fb)>= 3:
                    x = fb[-2][0]
                    y = fb[-2][1]

                    x1 = fb[-3][0]
                    y1 = fb[-3][1]

                    x2 = fb[-1][0]
                    y2 = fb[-1][1]

                    a = y1 - y2
                    b = x2 - x1
                    c = x1*y2 - y1*x2

                    if ( a*x + b*y + c > 0 and b>0 ) or ( a*x + b*y + c < 0 and b<0 ):
                        del fb[-2]
                    else:
                        break
        del fb[0]
        #print(fb) # see the result of lower fence buildng

        # v1 = the point laying on vertical first line
        v1 = list()
        if fence[0][0] == fence[1][0]:
            t1 = 1
            t2 = temp.index(fence[1])           
            v1 = temp[t1:t2]

        # v2 = the point laying on vertical last line
        try:
            v2 = list()
            if fence[-1][0] == fb[-1][0]:
                t1 = temp.index(fb[-1])
                t2 = temp.index(fence[-1])
                v2 = temp[t1+1:t2]
        except:
            pass


        # Combining results
        mylist = list() 

        for item in fence:
            if item not in mylist:
                mylist.append(item)
        for item in fb:
            if item not in mylist:
                mylist.append(item) 
        
        for item in v1:
            if item not in mylist:
                mylist.append(item)
        for item in v2:
            if item not in mylist:
                mylist.append(item)

        return mylist



lst = [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
test = Solution()
ans = test.outerTrees(lst)
print(ans)

# Test cases

# 1) [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
# ans: [[7,4],[5,0],[7,3],[2,1],[5,5],[4,5],[3,5],[7,2],[1,2],[1,4],[4,0],[2,5],[6,1],[6,5],[0,3],[3,0]]

# 2) [[0,0],[0,100],[100,100],[100,0],[50,50]]
# ans: [[100,100],[0,0],[100,0],[0,100]]
class Solution:
    def setZeroes(self, matrix):
        rflag = False
        cflag = False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        rflag = True
                        matrix[0][j] = "True"
                    if j == 0:
                        cflag = True
                        matrix[i][0] = "True"
                    if i!=0 and j!=0: 
                        matrix[i][0] = "True"
                        matrix[0][j] = "True"

        #Populate all the rows with  zero except row 0. Because we need row 0 to populate colums with zero
        for i in range(1, len(matrix)):
            if matrix[i][0] == "True":
                for j in range(len(matrix[0])):
                    matrix [i][j] = 0

        for j in range(len(matrix[0])):
            if matrix[0][j] == "True":
                for i in range(len(matrix)):
                    matrix [i][j] = 0

        if rflag is True:
            for k in range(len(matrix[0])):
                    matrix[0][k] = 0

        if cflag is True:
            for k in range(len(matrix)):
                    matrix[k][0] = 0
                
        

ans = Solution()

matrix = [[1],[0],[3]]

ans.setZeroes(matrix)

print(matrix)

        

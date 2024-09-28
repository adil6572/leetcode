class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        rows = [0]*m
        cols= [0]*n

        for i in range(0,m):
            for j in range(0,n):
                if(matrix[i][j]==0):
                    rows[i]=cols[j]=1
    
        for i in range(0,m):
            for j in range(0,n):
                if(rows[i]==1 or cols[j]==1):
                    matrix[i][j]=0

         
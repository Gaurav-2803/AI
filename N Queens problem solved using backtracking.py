class NQueenAlgo:

    def __init__(self,n):
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.n = n

    def isSafe(self,row,col):
        i = 0
        while(i<row):
            if(self.board[i][col]==1):
                return False
            i+=1

        i = row-1
        j = col-1

        while(i>=0 and j>=0):
            if(self.board[i][j]==1):
                return False
            i-=1
            j-=1

        i = row-1
        j = col+1

        while(i>=0 and j<self.n):
            if(self.board[i][j]==1):
                return False
            i-=1
            j+=1

        return True

    def nQueen(self,row=0):

        if(row>=self.n):
            return True

        for col in range(0,self.n):

            if(self.isSafe(row,col)):

                self.board[row][col] = 1

                if(self.nQueen(row+1)):
                    return True

                self.board[row][col] = 0

        return False

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j],end=" ")
            print()

def main():

    n = 4
    nQ = NQueenAlgo(n)
    nQ.nQueen()
    nQ.display()

main()
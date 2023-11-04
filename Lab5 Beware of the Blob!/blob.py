"""
Lab 5 : Beware of the Blob!
Author: Bakhbyergyen Yerjan
Last Modified: 10/13/2022 1:50 PM
"""

class Blob:
    def __init__(self, file_name):
        self.file_name = file_name
        self.grid = []
        self.blobbed = self.grid
        self.people_blobbed = 0
        
        counter = 0

        #Reading the file
        file = open(self.file_name, 'r')
        for line in file:
            if counter == 0:
                self.max_rows = int(line.strip().split()[0])
                self.max_cols = int(line.strip().split()[1])
            elif counter == 1:
                self.starting_row = int(line.strip().split()[0])
                self.starting_col = int(line.strip().split()[1])
            else:
                new_row = []
                for i in range(int(self.max_cols)):
                    new_row.append(line[i])
                self.grid.append(new_row)
            counter+=1
        file.close()

        # Pre-Processing
        self.sewer_list =  []
        for i in range(self.max_rows):
            for j in range(self.max_cols):
                if self.grid[i][j] == '@':
                    self.sewer_list.append([i,j])

        # Main code
    def is_valid(self,row,col):
        if 0 <= row and row < self.max_rows and 0 <= col and col < self.max_cols:
            if self.grid[row][col] == '#' or self.blobbed[row][col] == 'B':
                return False
            else:
                return True

    def move(self,row,col):
        if self.grid[row][col] != '@':
            if self.grid[row][col] == 'P':
                self.people_blobbed += 1
            self.blobbed[row][col] = 'B'
        else:
            if len(self.sewer_list) > 1:
                rem = self.sewer_list.index([row,col])
                self.sewer_list.pop(rem)
                next = self.sewer_list[0]
                self.move(next[0],next[1])
                
        if self.is_valid(row-1,col) == True:
            self.move(row-1,col)
        if self.is_valid(row,col+1) == True:
            self.move(row,col+1)
        if self.is_valid(row+1,col) == True:
            self.move(row+1,col)
        if self.is_valid(row,col-1) == True:
            self.move(row,col-1)

    def run(self):
        self.move(self.starting_row, self.starting_col)
        for i in range(self.max_rows):
            cur_row = ""
            for j in range(self.max_cols):
                cur_row = cur_row + self.blobbed[i][j]
            print(cur_row)
        print('Total eaten:',self.people_blobbed)
# Sketch of the MazeWalking class

class MazeWalker:
    def __init__(self, maze):
        # the maze contents
        # the visited grid
        # current step
    def walk(row, col):
        self.mark(row,col)

        if self.is_exit(row,col):
            return True
        #If up is a valid move try it
        if self.is_valid_move(row-1,col): #moving up along the y -axis (y+ goes down, x+ goes right)
            up_worked = self.walk(row-1,col)
            if up_worked:
                return True
        #If right is a valid move try it
        if self.is_valid_move(row,col+1): #moving up along the y -axis (y+ goes down, x+ goes right)
            right_worked = self.walk(row,col+1)
            if right_worked:
                return True
        #If down is a valid move try it
        if self.is_valid_move(row+1,col): #moving up along the y -axis (y+ goes down, x+ goes right)
            down_worked = self.walk(row+1,col)
            if down_worked:
                return True
        #If left is a valid move try it
        if self.is_valid_move(row,col-1): #moving up along the y -axis (y+ goes down, x+ goes right)
            left_worked = self.walk(row,col-1)
            if left_worked:
                return True
        #Unmark (assume a helper method)
        self.unmark(row,col)
        #One last thing...
        return False

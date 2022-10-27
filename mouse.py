"""
File implementing the example of a mouse trying to find the cheese.

Properties of the problem:
    - Variable size of maze
    - Obstacles hindering the mouse (walls)
    - multiple block of cheese
"""

from typing import List, Tuple


# define constants
X = "X"
O = "O"
WALL = "#"
entities = [X, O, WALL]

class MouseCheeseProblem():
    def __init__(self, filename="standard_world.txt") -> None:
        """
        Creating the mouse-cheese problem.

        Parameters
        ----------
        filename: string of filename of prepared world. 
            # defines a wall
            X defines the initial position
            O defines the goal (cheese)
            example see standard_world.txt
        """
        
        self.filename = filename
        self.board, self.state, self.goal_states = self.initialize_problem()
    

    def read_file(self) -> List[List]:
        """
        Returns list of lines of given file
        """
        try:
            f = open(self.filename, 'r')
            lines = f.readlines()
            return lines
        except FileNotFoundError:
            print("File not found. Try again!")

    def initialize_problem(self) -> Tuple:
        """
        Returns initials maze as list with player position and placed cheese and walls
        and secondly the inital position of X
        """
        layout = self.read_file()
        board = []
        initial_position = None
        goal_states = []
        for i, layer in enumerate(layout):
            line = []
            for j, entity in enumerate(layer):
                if entity in entities:
                    if entity == X:
                        initial_position = (i, j)
                         # don't add it to the board representation
                    elif entity == O:
                        goal_states.append((i, j))
                    line.append(entity)
                elif entity != "\n": # ignore new line
                    line.append(None)
            board.append(line)
        
        if (not initial_position): 
            raise Exception("No Initial Position of X found.")

        return (board, initial_position, goal_states)
        
    def actions(self, state) -> List:
        """
        Returns actions a mouse can take in a given state
        example of possible actions = [(1,1), (2,1)]
        """
        actions = []
        
        y, x = state[0], state[1]

        # add all possible actions of neighbouring vertical and horizontal cells
        if self.board[y-1][x] != WALL:
            actions.append((y-1, x))
        if self.board[y+1][x] != WALL:
            actions.append((y+1, x))
        if self.board[y][x-1] != WALL:
            actions.append((y, x-1))
        if self.board[y][x+1] != WALL:
            actions.append((y, x+1))
        return actions

    def result(self, state, action):
        """
        Returns resulting state given a previous state and the action taken upon it
        Ever since state represention is a tuple of (y, x) coordination, the resulting state of
        the action is just the action itself
        Also: the internal respresentation of the board gets overwritten
        """
        self.state = action
        return self.state
    
    def goal_test(self, state):
        """
        Returns True in case it is a goal state, False otherwise
        A goal state is a state in which the cheese has been reached
        """
        if state in self.goal_states:
            return True
        else:
            return False

    def drawGame(self, node):
        """
        Uses command line to print board 
        """
        print(f"Depth: {node.depth}")
        for i, line in enumerate(self.board):
            for j, e in enumerate(line):
                if (i, j) == node.state:
                    print(X, end="")
                    
                if e == None:
                    e = " "
                print(e, end="")
                print(" ", end="")
            print()
        print()

"""
File implementing the example of a mouse trying to find the cheese.

Properties of the problem:
    - Variable size of maze
    - Obstacles hindering the mouse (walls)
    - multiple block of cheese
"""

from typing import List, Tuple
from termcolor import colored

from utils import bcolors


# define constants
X = "X"
O = "O"
WALL = "#"
EMPTY = " "
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
            lines = f.read().splitlines()
            return lines
        except FileNotFoundError:
            print("File not found. Try again!")
            raise FileNotFoundError

    def initialize_problem(self) -> Tuple:
        """
        Returns initials maze as list with player position and placed cheese and walls
        and secondly the inital position of X
        """
        layout = self.read_file()
        board = []
        initial_position = None
        goal_states = []
        for i, row in enumerate(layout):
            line = []
            for j, entity in enumerate(row):
                if entity == EMPTY:
                    line.append(None)
                elif entity == X:
                    initial_position = (i, j)
                    line.append(None)
                elif entity == O:
                    goal_states.append((i, j))
                    line.append(entity)
                else:
                    line.append(entity)
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

    def action_cost(self, action):
        """
        Returns path cost resulting from taking action in state1 to arrive at state 2
        c is the cost that it already took to get to state1
        Note: it required that the empty paths in your problem world need to be filled with a number for path cost
        empty squares cost 1
        """
        try:
            action_cost = int(self.board[action[0]][action[1]])
            return action_cost
        except:
            return 1

    def manhattan_distance(self, x1, y1):
        """
        Returns the manhattan distance of given state
        """
        md = min([abs(x1-x2) + abs(y1-y2) for y2, x2 in self.goal_states])
        return md

    def h(self, node):
        """
        Returns heuristic for a given node
        """
        h = self.manhattan_distance(node.state[1], node.state[0])
        return h

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
                    print(bcolors.OKGREEN + X + bcolors.ENDC, end="")
                elif e == None:
                    e = " "
                    print(e, end="")
                else:
                    print(e, end="")
                print(" ", end="")
            print()
        print()

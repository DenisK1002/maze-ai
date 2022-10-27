"""
File Implementing various algorithms to solve
the mouse-ai problem for a given world
"""
from mouse import MouseCheeseProblem
from utils import Node
from typing import Deque

class MouseAI():
    "AI solving the MouseCheeseProblem"

    def __init__(self, problem) -> None:
        self.problem = problem

    def BFS(self):
        """
        Operating BFS on Mouse-Cheese problem
        """
        node = Node(self.problem.state)

        frontier = Deque([node])
        explored = set()
        
        while frontier:
            node = frontier.popleft()
            self.problem.drawGame(node)
            explored.add(node.state)
            for child in node.expand(self.problem):
                if child.state not in explored and child not in frontier:
                    if problem.goal_test(child.state):
                        print(f"Solved and reached: {child.path()}")
                        self.problem.drawGame(child)
                        return child
                    frontier.append(child)

        print("No solution found")
        return None

    def DFS(self):
        """
        Operating DFS on Mouse-Cheese problem
        """
        node = Node(self.problem.state)
        frontier = [node] # stack
        explored = set()

        while frontier:
            node = frontier.pop(-1)
            explored.add(node.state)
            self.problem.drawGame(node)
            for child in node.expand(self.problem):
                if child.state not in explored and child not in frontier:
                    if problem.goal_test(child.state):
                        self.problem.drawGame(child)
                        return child
                    frontier.append(child)
        return None
    


if __name__ == '__main__':
    
    problem = MouseCheeseProblem(filename="standard_world.txt")
    ai = MouseAI(problem)
    ai.DFS()
    
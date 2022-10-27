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
        node = Node(problem.state)

        q = Deque([node])
        explored = []
        
        while q:
            node = q.popleft()
            problem.drawGame(node)
            explored.append(node.state)
            for child in node.expand(problem):
                if child.state not in explored and child not in q:
                    if problem.goal_test(child.state):
                        print(f"Solved and reached: {child.path()}")
                        problem.drawGame(child)
                        return child
                    q.append(child)

        print("No solution found")
        return None

    def DFS(self):
        """
        Operating DFS on Mouse-Cheese problem
        """
        raise NotImplementedError
    


if __name__ == '__main__':
    
    problem = MouseCheeseProblem(filename="standard_world.txt")
    ai = MouseAI(problem)
    ai.BFS()
    
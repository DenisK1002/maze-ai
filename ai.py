"""
File Implementing various algorithms to solve
the mouse-ai problem for a given world
"""
from mouse import MouseCheeseProblem
from utils import Node, PriorityQueue
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
    
    def UCS(self):
        """
        Operating Uniform-Cost-Search on MouseCheeseProblem
        """
        node = Node(self.problem.state)
        frontier = PriorityQueue(list=[])
        frontier.push(node)
        explored = set()

        while frontier:
            # select cheapest node
            node = frontier.pop()
            self.problem.drawGame(node)
            if problem.goal_test(node.state):
                print(node.path())
                return node
            explored.add(node.state)
            for child in node.expand(self.problem):
                if child.state not in explored and not frontier.in_queue(child):
                    frontier.push(child)
                elif frontier.in_queue_value(child) > child.path_cost:
                    frontier.replace(child)
        return None

    def ASTAR(self):
        """
        Operating A*-Search on MouseCheeseProblem
        """
        node = Node(self.problem.state)
        frontier = PriorityQueue()
        frontier.push(node, self.problem.h)
        explored = set()
        
        while frontier:
            node = frontier.pop()
            self.problem.drawGame(node)
            if problem.goal_test(node.state):
                print(node.path())
                return node
            explored.add(node.state)
            for child in node.expand(self.problem):
                if child.state not in explored and not frontier.in_queue(child):
                    frontier.push(child)
                elif child.path_cost + self.problem.h(child) < frontier.in_queue_value(child):
                    frontier.replace(child)

        return None

if __name__ == '__main__':
    
    problem = MouseCheeseProblem(filename="worlds/std_world_with_cost.txt")
    ai = MouseAI(problem)
    ai.ASTAR()
    
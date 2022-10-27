
from heapq import heapify, heappop
import heapq
import math


class Node:
    """
    Class representing Node in graph
    """

    def __init__(self, state, action=None, parent=None, path_cost=0):
        self.state = state
        self.action = action
        self.parent = parent
        self.path_cost = path_cost
        self.depth = 0 if not parent else parent.depth + 1

    def expand(self, problem):
        expandable_nodes = [self.child_node(problem, action) for action in problem.actions(self.state)]
        return expandable_nodes
    
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, action, self, self.path_cost + problem.action_cost(action))
        return next_node

    def __repr__(self):
        return f"<Node {self.state}>"

    def path(self):
        """
        Returns all nodes from start to finish
        """

        path = []
        node = self
        while node:
            path.append(node)
            node = node.parent
        path.reverse()
        return path

    def __eq__(self, other) -> bool:
        return self.state == other.state
    
    def __lt__(self, other) -> bool:
        return self.path_cost < other.path_cost
    
    def __gt__(self, other) -> bool:
        return self.path_cost > other.path_cost
    

class PriorityQueue:
    """
    Priority Queue utilizing heapq module
    """

    def __init__(self, list=[]):
        self.pq = list
        

    def pop(self):
        print(self.pq)
        return heappop(self.pq)[1]
    
    def push(self, node):
        heapq.heappush(self.pq, (node.path_cost, node))

    def in_queue_value(self, node) -> int:
        """
        Returns value of node in Priority Queue
        """
        for h in self.pq:
            if node == h[1]:
                return h[0]
        return math.inf

    def in_queue(self, node) -> bool:
        """
        Checks whether node is in q, returns their value
        """
        if node in [h[1] for h in self.pq]:
            return True

        return False

    def replace(self, node):
        """
        replaces node in queue with given node
        """
        for i, h in enumerate(self.pq.copy()):
            if node == h[1]:
                self.pq[i] = (node.path_cost, node)
        

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
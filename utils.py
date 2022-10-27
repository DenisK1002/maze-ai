
class Node:
    """
    Class representing Node in graph
    """

    def __init__(self, state, action=None, parent=None):
        self.state = state
        self.action = action
        self.parent = parent
        self.depth = 0 if not parent else parent.depth + 1

    def expand(self, problem):
        expandable_nodes = [self.child_node(problem, action) for action in problem.actions(self.state)]
        return expandable_nodes
    
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, action, self)
        return next_node

    def __repr__(self):
        return f"<Node {self.action}>"

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
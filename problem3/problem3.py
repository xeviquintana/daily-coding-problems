"""
[MEDIUM]
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which
serializes the tree into a string, and deserialize(s), which
deserializes the string back into the tree.

For example, given the following Node class:

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    DEFAULT_VAL_EXPR: str = '-'

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
    def Node(self) -> None:
        self.val = None
        self.left = None
        self.right = None    

    def set_left(self, n: Node) -> None:
        self.left = n
    
    def set_right(self, n: Node) -> None:
        self.right = n

    def __str__(self) -> str:
        if not self.left and not self.right:
            return "Node({})".format(self.val)
        elif self.left and not self.right:
            return "Node({}, {})".format(self.val, self.left)
        else:
            return "Node({}, {}, {})".format(self.val, self.left or self.DEFAULT_VAL_EXPR, self.right)

    @staticmethod
    def recursive_deserialize(node_str: str, i: int) -> (Node, int):
        """
        @param node_str: the original string to deserialize as Node
        @param i: position of char currently processed
        """
        # skipping empty chars...
        while i < len(node_str) and node_str[i] == ' ':
            i += 1

        # "Node" is a decorator, so skip those chars, they don't bring valuable info
        if node_str[i:i+5] == "Node(":
            i += len("Node(")
        
        val: str = ""
        while node_str[i] != ')' and node_str[i] != ',':
            val += node_str[i]
            i += 1
        
        if val == Node.DEFAULT_VAL_EXPR:
            return None, i+1
        
        n: Node = Node(val if val else Node.DEFAULT_VAL_EXPR)
        
        if node_str[i] == ',':
            left, i = Node.recursive_deserialize(node_str, i+1)
            n.set_left(left)
        if node_str[i] == ',':
            right, i = Node.recursive_deserialize(node_str, i+1) 
            n.set_right(right)

        return n, i+1

    @staticmethod
    def serialize(n: Node) -> str:
        return n.__str__()

    @staticmethod
    def deserialize(node_str: str) -> Node:
        tree: Node = None
        (tree, _) = Node.recursive_deserialize(node_str, 0)
        return tree
    
    @staticmethod
    def get_left_nodes(n: Node) -> int:
        if n is None:
            return 0
        elif n.left is not None:
            return 1 + Node.get_left_nodes(n.left) + Node.get_left_nodes(n.right)
        elif n.right is not None:
            return Node.get_left_nodes(n.right)
        else:
            return 0
    
    @staticmethod
    def get_right_nodes(n: Node) -> int:
        if n is None:
            return 0
        elif n.right is not None:
            return 1 + Node.get_right_nodes(n.right) + Node.get_right_nodes(n.left)
        elif n.left is not None:
            return Node.get_right_nodes(n.left)
        else:
            return 0


if __name__ == '__main__':
    tree1: Node = Node('root', Node('left', Node('left.left')), Node('right'))   
    assert Node.deserialize(Node.serialize(tree1)).left.left.val == 'left.left'
    assert Node.get_left_nodes(tree1) == 2
    assert Node.get_right_nodes(tree1) == 1

    tree2: Node = Node('root', Node('left', Node('left.left'), Node('left.right')))
    assert Node.deserialize(Node.serialize(tree2)).left.right.val == 'left.right'
    assert Node.get_left_nodes(tree2) == 2
    assert Node.get_right_nodes(tree2) == 1
    
    tree3: Node = Node('root', \
        Node('left', \
            Node('left.left'), \
            Node('left.right', \
                Node('left.right.left', \
                    Node('left.right.left.left'), \
                    Node('left.right.left.right', \
                        Node('left.right.left.right.left'))))))
    # tree3:
    #                   root
    #                    /
    #                  left
    #                 /    \
    #         left.left     left.right
    #                         /
    #                     left.right.left
    #                       /       \
    #      left.right.left.left   left.right.left.right
    #                                  /
    #                          left.right.left.right.left
    assert Node.get_left_nodes(tree3) == 5
    assert Node.get_right_nodes(tree3) == 2
    assert Node.deserialize(Node.serialize(tree3)).right == None
    assert Node.deserialize(Node.serialize(tree3)).left.right.left.val == 'left.right.left'
    assert Node.deserialize(Node.serialize(tree3)).left.right.left.right.val == 'left.right.left.right'
    assert Node.deserialize(Node.serialize(tree3)).left.right.left.right.left.val == 'left.right.left.right.left'
    
    print("Succesfully tested.")

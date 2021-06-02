"""
# PROBLEM #8 [EASY]

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
from typing import Any


class Node:
    def __init__(self, val: Any, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right
    # /def

    def unival_subtrees(self) -> int:
        (unival_subtrees, _) = self.immerse_unival()
        return unival_subtrees
    # /def

    def immerse_unival(self) -> (int, bool):
        """
        Reach the leafs in postorder traversal.
        For a leaf, the subtree is considered to be True, so:
            - leaf_node = Node(any, None, None)
            - is_subtree(leaf_node) is True
        
        Then move back to parent Node and check if the subtree is kept.
        A node is a subtree if:
            - leafs are None, or
            - leafs hold the same value as parent node

        O(2^n) in time, O(n) in space being n the number of nodes in the tree
        """
        ret_left: int = 0
        ret_right: int = 0
        is_subtree_left: bool = True
        is_subtree_right: bool = True

        if self.left is not None:
            (ret_left, is_subtree_left) = self.left.immerse_unival()
        
        if self.right is not None:
            (ret_right, is_subtree_right) = self.right.immerse_unival()
        
        root_equals_childs: bool = self == self.left and self == self.right

        is_root_subtree = is_subtree_left and is_subtree_right and root_equals_childs
        
        return ret_left + ret_right + int(is_root_subtree), root_equals_childs
    # /def

    def __eq__(self, value):
        if value is None:  # that might be dirty in any other use case...
            return True
        else:
            return isinstance(value, Node) and self.val == value.val
        # /if
    # /def
# /class


if __name__ == "__main__":
    """tree:
       0
      / \
     1   0
        / \
       1   0
      / \
     1   1
    """
    tree: Node = \
        Node(
            val=0,
            left=Node(1),
            right=Node(
                val=0,
                left=Node(
                    val=1,
                    left=Node(1),
                    right=Node(1)
                ),
                right=Node(0)
            )
        )
    assert tree.unival_subtrees() == 5

    """ tree2:
     0
    / \
    """
    tree2: Node = Node(0) 
    assert tree2.unival_subtrees() == 1

    """ tree3:
        0
       / \
      1   1
    """
    tree3: Node = Node(0, Node(1), Node(1))
    assert tree3.unival_subtrees() == 2
    
    """ tree4:
        a
       / \
      c   b
         / \
        b   b
             \
              b   
    """
    tree4: Node = \
        Node(
            val='a',
            left=Node('c'),
            right=Node(
                val='b',
                left=Node('b'),
                right=Node(
                    val='b',
                    right=Node('b')
                )
            )
        )
    assert tree4.unival_subtrees() == 5

    print("Successfully tested.")

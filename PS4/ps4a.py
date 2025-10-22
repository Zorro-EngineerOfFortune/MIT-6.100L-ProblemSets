# Problem Set 4A
# Name:
# Collaborators:

from tree import Node  # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))  # TODO
tree2 = Node(
    7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10))
)  # TODO
tree3 = Node(
    5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26)))
)  # TODO


def find_tree_height(tree):
    """
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    """
    # TODO: Remove pass and write your code here
    if tree is None:
        # Height of an empty tree is -1
        return -1
    else:
        # Recursively find the height of the left and right subtrees
        height_left = find_tree_height(tree.get_left_child())
        height_right = find_tree_height(tree.get_right_child())
        # The height of the current tree is 1 (for the current node) plus the max height of its children
        return max(height_left, height_right) + 1


def is_heap(tree, compare_func):
    """
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    """
    # TODO: Remove pass and write your code here
    # Base Case: An empty tree is always considered a valid heap.
    if tree is None:
        return True
    parent_value = tree.get_value()
    left_child = tree.get_left_child()
    right_child = tree.get_right_child()
    # Check the local heap property with the left child
    if left_child != None:
        child_value = left_child.get_value()
        # If the comparison fails (e.g., child is greater than parent in a max heap check)
        if compare_func(child_value, parent_value) == False:
            return False
    # Check the local heap property with the right child
    if right_child != None:
        child_value = right_child.get_value()
        # If the comparison fails
        if compare_func(child_value, parent_value) == False:
            return False
    # Check the global heap property recursively on both subtrees
    return is_heap(left_child, compare_func) and is_heap(right_child, compare_func)


def compare_func(child_value, parent_value):
    """
    Defines the comparison for a MAX HEAP.
    Returns True if the parent is larger than or equal to the child (child <= parent).
    """
    if child_value < parent_value:
        return True
    return False


is_heap(tree1, compare_func)

if __name__ == "__main__":
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass

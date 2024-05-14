class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

# Create the root node
root = Node(1)

# Create the second level of nodes
root.left = Node(2)
root.right = Node(3)

# Create the third level of nodes
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level=level+1)
        print("    " * level + str(node.value))
        print_tree(node.left, level=level+1)

# Call the function with the root node to print the tree
print_tree(root)

print ("----------")

# find all nodes in a tree 
def get_all_nodes(root):
    if root is None:
        return []
    
    stack = [root]
    nodes = []
    
    while stack:
        node = stack.pop()
        nodes.append(node.value)
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return nodes

#find subtree

def identify_subtrees(root):
    nodes = []
    subtrees = []

    def find_subtree(node):
        if node is None:
            return None
        
        # Recursively find subtrees in the children nodes
        left_subtree = find_subtree(node.left)
        right_subtree = find_subtree(node.right)
        
        # Create a subtree including the current node and its children
        subtree = Node(node.value)
        subtree.left = left_subtree
        subtree.right = right_subtree
        
        # Append the subtree to the list of subtrees
        subtrees.append(subtree)
        
        return subtree

    # Call the recursive function to find subtrees starting from the root node
    find_subtree(root)
    
    return subtrees

subtrees = identify_subtrees(root)

# print_tree(subtrees, 3)

for tree in subtrees:
    print_tree(tree)
    print("-------")

print(get_all_nodes(root))

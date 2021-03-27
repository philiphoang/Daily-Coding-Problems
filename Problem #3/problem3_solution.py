class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = ""
def serialize(node, tree=""):
    """Serialize a binary tree into a string 
    Since it is a binary tree, the tree can have empty (Null) children. Mark these with '#'.

    Parameters: 
    argument1 Node: A node containing either children or nothing (Null)

    Return:
    String: The node serialized into a string format
    """
    
  
    if (not node): #Base case
        tree += "# "
        return tree
    tree += (str(node.val) + " ")
    tree = serialize(node.left, tree)
    tree = serialize(node.right, tree)

    return tree

i = 0
def deserialize(stringTree):
    """Deserialize a string into a binary tree. 
    Nodes with empty children (Null) are marked with #

    Parameters: 
    argument1 s: A list of strings containing the tree

    Return:
    Node: A binary tree 
    """
    global i #Global shared index 

    if (stringTree[i] == "#"): #Empty node
        return None 

    else:
        node = Node(stringTree[i]) #Create node of current index
        i+=1
        node.left = deserialize(stringTree) #Check left child
        i+=1
        node.right = deserialize(stringTree) #Check right child
        return node


node = Node('root', Node('left', Node('left.left')), Node('right'))

assert deserialize(serialize(node).split()).left.left.val == 'left.left'

#Original
#assert deserialize(serialize(node)).left.left.val == 'left.left'
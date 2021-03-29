class Node {
    constructor(val, left, right) {
        this.val = val
        this.left = left
        this.right = right
    }
}

/**
 * Serialize a binary tree into a string 
 * Since it is a binary tree, the tree can have empty (Null) children. Mark these with '#'.
 * 
 * @param {Node} node A node with either children or nothing
 * 
 * @return {String} The binary in String format
 */
function serialize(node) {
   var s = ""

    if (node === undefined) {
        s += "# "
    }
    else {
        s += String(node.val) + " "
        s += serialize(node.left)
        s += serialize(node.right)
    }

    return s
}

/**
 * Deserialize a string into a binary tree. 
 * Nodes with empty children (Null) are marked with #
 * 
 * @param {List} stringTree A list of strings containing the tree
 * 
 * @return {Node} A binary tree 
 */
function deserialize(stringTree) {
    var val = stringTree.shift()
    if (val === '#') {
        return
    }
    else {
        node = new Node(val, deserialize(stringTree), deserialize(stringTree))
    }

    return node
 
}

var node = new Node('root', new Node('left', new Node('left.left')), new Node('right'))

var assert = require("assert")

assert(deserialize(serialize(node).split(" ")).left.left.val == 'left.left')

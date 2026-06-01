class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    
    inorder = []
    preorder = []
    postorder = []
    
    def traverse(node):
        if node is None:
            return
        
        preorder.append(node.data)
        
        traverse(node.left)
        
        inorder.append(node.data)
        
        traverse(node.right)
        
        postorder.append(node.data)
    
    traverse(root)
    
    return [inorder, preorder, postorder]
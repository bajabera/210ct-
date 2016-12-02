class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 






def in_order(tree):
    '''
    Uses the stack method to sort the elements in the tree in ascending order
    Returns the elements of the tree in ascending order
    '''
    s=[]#empty stack
    while len(s)!=0 or tree!=None:
        if tree != None:
            s.append(tree)#append current node to stack
            tree=tree.left#sets current node to left node
        else:
            if len(s)!=0:
                tree=s.pop()#removes the value from the stack
                print (tree.value)
                tree=tree.right#sets current node to the right node
            else:
                break
                

    
if __name__ == '__main__':
    A = [2,6,1,8,3]
    t=tree_insert(None,A[0])#inserts first value, initiates the tree
    for i in range(1,len(A)):
        tree_insert(t,A[i])#inserts values into the tree
    in_order(t)#orders them according to the inorder rules

  

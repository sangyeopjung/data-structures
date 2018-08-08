
# coding: utf-8

# In[1]:


from Queue import Queue

class Node(object):
    def __init__(self, value, left=None, right=None):
        if value < 0:
            raise ValueError('value cannot be negative')
        
        self.value = value
        self.left = left
        self.right = right
        
    
    def setValue(self, value):
        if value < 0:
            raise ValueError('value cannot be negative')
            
        self.value = value
        
    
    def getValue(self):
        return self.value
    
    
    def setLeft(self, left):
        self.left = left
    
    
    def getLeft(self):
        return self.left
    
    
    def setRight(self, right):
        self.right = right
        
    
    def getRight(self):
        return self.right
    
    
    def insert(self, value, depth=0):
        if self.value < value:
            if self.right:
                return self.right.insert(value, depth+1)
            else:
                self.right = Node(value)
                return depth+1
        elif self.value > value:
            if self.left:
                return self.left.insert(value, depth+1)
            else:
                self.left = Node(value)
                return depth+1
        else:
            return depth
    
    
    def delete(self, parent, value):
        if self.value < value:
            if self.right:
                return self.right.delete(self, value)
            else:
                return False
        elif self.value > value:
            if self.left:
                return self.left.delete(self, value)
            else:
                return False
        else:
            if self.right and self.left:
                # both right and left
                self.value = self.right.getMin()
                self.right.delete(self, self.value)
            elif self.right:
                # only right
                if self == parent.getRight():
                    parent.setRight(self.right)
                else:
                    parent.setLeft(self.right)
            elif self.left:
                # only left
                if self == parent.getRight():
                    parent.setRight(self.left)
                else:
                    parent.setLeft(self.left)
            else:
                # none
                if self == parent.getRight():
                    parent.setRight(None)
                else:
                    parent.setLeft(None)
            return True
                
    def getMin(self):
        if not self.left:
            return self.value
        return self.left.getMin()
    
    
    def getMax(self):
        if not self.right:
            return self.value
        return self.right.getMax()
    
    
    def traversePreOrder(self):
        if not self:
            return
        
        print(self.value, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()
        
        
    def traverseInOrder(self):
        if not self:
            return
        
        if self.left:
            self.left.traverseInOrder()
        print(self.value, end=' ')
        if self.right:
            self.right.traverseInOrder()
        
        
    def traversePostOrder(self):
        if not self:
            return
        
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.value, end=' ')
    

class BinarySearchTree(object):
    """
    getRoot()
    
    search(value)
    insert(value)
    delete(value)
    
    getMin()
    getMax()
    
    traversePreOrder()
    traverseInOrder()
    traversePostOrder()
    """
    def __init__(self, root=None):
        self.root = root
    
    
    def getRoot(self):
        return self.root
    
    
    def search(self, value):
        curr = self.root
        if not curr:
            return -1
        
        depth = -1
        while curr:
            depth += 1
            if curr.getValue() < value:
                curr = curr.getRight()
            elif curr.getValue() > value:
                curr = curr.getLeft()
            else:
                return depth
        
        return -1
    
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return 0
        
        return self.root.insert(value)
    
    
    def delete(self, value):
        if not self.root:
            return False
        if self.root.getValue() == value:
            if self.root.getRight() and self.root.getLeft():
                # both right and left
                self.root.setValue(self.root.getRight().getMin())
                self.root.getRight().delete(self.root, self.root.getValue())
            elif self.right:
                # only right
                self.root = self.root.getRight()
            elif self.left:
                # only left
                self.root = self.root.getLeft()
            else:
                # none
                self.root = None
            return True
        
        return self.root.delete(None, value)
    
    
    def getMin(self):
        if not self.root:
            return -1
        
        return self.root.getMin()
    
        
    def getMax(self):
        if not self.root:
            return -1
        
        return self.root.getMax()
    
    
    def traversePreOrder(self):
        print('Pre order:')
        if self.root:
            self.root.traversePreOrder()
        print()
        
        
    def traverseInOrder(self):
        print('In order:')
        if self.root:
            self.root.traverseInOrder()
        print()
            
            
    def traversePostOrder(self):
        print('Post order:')
        if self.root:
            self.root.traversePostOrder()
        print()
            
    
    def traverseBreadthFirst(self):
        print('Breadth first:')
        q = Queue()
        if self.root:
            q.enqueue(self.root)
        
        while q.getLength():
            curr = q.dequeue()
            print(curr.getValue(), end=' ')
            if curr.getLeft():
                q.enqueue(curr.getLeft())
            if curr.getRight():
                q.enqueue(curr.getRight())
        print()


# In[2]:


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(1)
    tree.insert(20)
    tree.insert(30)
    tree.insert(9)
    tree.insert(6)
    tree.insert(15)
    tree.insert(16)
    tree.insert(13)
    print(tree.search(1))
    print(tree.search(16))
    '''
            10
        /        \
       5          12
      / \           \
    1     9          20
         /          /  \
        6         15    30
                 /  \
               13    16
    '''

    tree.traversePreOrder()
    tree.traverseInOrder()
    tree.traversePostOrder()
    tree.traverseBreadthFirst()
    print('After deleting 20')
    tree.delete(20)
    tree.traverseInOrder()
    print('After deleting 10')
    tree.delete(10)
    tree.traverseInOrder()


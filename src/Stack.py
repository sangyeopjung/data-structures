
# coding: utf-8

# In[1]:


from LinkedList import LinkedList

class Stack(object):
    def __init__(self, arr=[]):
        self.stack = LinkedList(arr)
        
    
    def __str__(self):
        return self.stack.__str__()
        
    
    def getSize(self):
        return self.stack.getLength()
    
    
    def push(self, val):
        self.stack.push(val)
        
    
    def pop(self):
        return self.stack.pop()
    
    
    def peek(self):
        return self.stack.get(0)


# In[2]:


if __name__ == '__main__':
    print("Initialising stack [1, 2, 3]")
    s = Stack([1, 2, 3])
    print(s)
    print("push 4")
    s.push(4)
    print(s)
    print("peek")
    print(s.peek())
    print("pop 2 times")
    print(s.pop())
    print(s.pop())
    print(s)


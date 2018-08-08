
# coding: utf-8

# In[1]:


from Heap import Heap

class PriorityQueue(object):
    def __init__(self, q=[]):
        self.pq = Heap(q)
        
    
    def __str__(self):
        return self.pq.__str__()
    
    
    def insert(self, value):
        self.pq.insert(value)
    
    
    def pop(self):
        return self.pq.deleteMin()
    
    
    def peek(self):
        return self.pq.peek()


# In[2]:


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.insert(10)
    pq.insert(100)
    pq.insert(1000)
    pq.insert(1)
    pq.insert(11)
    print(pq)
    pq.pop()
    print(pq)


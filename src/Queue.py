
# coding: utf-8

# In[8]:


from DoublyLinkedList import DoublyLinkedList

class Queue(object):
    def __init__(self, arr=[]):
        self.queue = DoublyLinkedList(arr)
        
    
    def __str__(self):
        return self.queue.__str__()
        
        
    def enqueue(self, value):
        self.queue.append(value)
        
    
    def dequeue(self):
        return self.queue.pop()
    
    
    def peek(self):
        return self.queue.get(self.queue.getLength()-1)


# In[10]:


if __name__ == '__main__':
    print("Initialising stack [1, 2, 3]")
    q = Queue([1, 2, 3])
    print(q)
    print("enqueue 4")
    q.enqueue(4)
    print(q)
    print("peek")
    print(q.peek())
    print("dequeue 2 times")
    print(q.dequeue())
    print(q.dequeue())
    print(q)


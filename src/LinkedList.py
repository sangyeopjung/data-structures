
# coding: utf-8

# In[1]:


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
        
    def setValue(self, value):
        self.value = value
        
        
    def getValue(self):
        return self.value
    
    
    def setNext(self, next):
        self.next = next
    
    
    def getNext(self):
        return self.next
    
    
class LinkedList(object):
    """
    getLength()
    toArray()
    push(value, index)
    pushLinkedList(linkedList, index)
    pop(index)
    get(index)
    find(value)
    remove(value)
    reverse()
    getMiddle()
    """
    def __init__(self, array=[]):
        self.length = len(array)
        
        if array:
            self.head = Node(array[0])
            curr = self.head
            for i in range(1, self.length):
                curr.setNext(Node(array[i]))
                curr = curr.getNext()
        else:
            self.head = None
    
    
    def __str__(self):
        s = '['
        curr = self.head
        while curr:
            s += str(curr.getValue())
            curr = curr.getNext()
            if curr:
                s += ', '
        s += ']'
        return s
    
    
    def getHead(self):
        return self.head
    
    
    def setHead(self, head):
        self.head = head
    
    
    def getLength(self):
        return self.length
    
    
    def toArray(self):
        l = []
        curr = self.head
        while curr:
            l.append(curr.getValue())
            curr = curr.getNext()
        return l
    
    
    def push(self, value, index=0):
        if index > self.length:
            raise IndexError('Index out of range')
        
        if not index:
            self.head = Node(value, self.head)
            self.length += 1
            return
            
        curr = self.head
        for _ in range(index-1):
            curr = curr.getNext()
        curr.setNext(Node(value, curr.getNext()))
        self.length += 1
        
        
    def pushLinkedList(self, linkedList, index=0):
        if index > self.length:
            raise IndexError('Index out of range')
        
        if not linkedList.getLength():
            return
        
        if not index:
            curr = linkedList.getHead()
            while curr.getNext():
                curr = curr.getNext()
            curr.setNext(self.head)
            self.head = linkedList.getHead()
            self.length += linkedList.getLength()
            return
            
        curr = self.head
        for _ in range(index-1):
            curr = curr.getNext()
            
        curr2 = linkedList.getHead()
        while curr2.getNext():
            curr2 = curr2.getNext()
        curr2.setNext(curr.getNext()) 
        
        curr.setNext(linkedList.getHead())
        self.length += linkedList.getLength()
        
        
    def pop(self, index=0):
        if index >= self.length:
            raise IndexError('Index out of range')
        
        if not index:
            out = self.head.getValue()
            self.head = self.head.getNext()
            self.length -= 1
            return out
            
        curr = self.head
        for _ in range(index):
            prev = curr
            curr = curr.getNext()
        out = curr.getValue()
        prev.setNext(curr.getNext())
        self.length -= 1
        return out
    
    
    def get(self, index):
        if index >= self.length:
            raise IndexError('Index out of range')
        
        if not index:
            return self.head.getValue()
            
        curr = self.head
        for _ in range(index):
            prev = curr
            curr = curr.getNext()
        return curr.getValue()
    
    
    def find(self, value):
        if not self.length:
            return -1
        
        curr = self.head
        for i in range(self.length):
            if curr.getValue() == value:
                return i
            curr = curr.getNext()
        return -1
          
        
    def remove(self, value):
        if not self.length:
            return -1
        
        prev = None
        curr = self.head
        for i in range(self.length):
            if curr.getValue() == value:
                if not prev:
                    self.head = curr.getNext()
                else:
                    prev.setNext(curr.getNext())
                self.length -= 1
                return i
            prev = curr
            curr = curr.getNext()
        return -1
          
        
    def removeAll(self, value):
        if not self.length:
            return
        
        prev = None
        curr = self.head
        while curr:
            if curr.getValue() == value:
                if not prev:
                    self.head = curr.getNext()
                else:
                    prev.setNext(curr.getNext())
                curr = curr.getNext()
                self.length -= 1
                continue
            prev = curr
            curr = curr.getNext()
    
    
    def reverse(self):
        if not self.length:
            return
        
        prev = None
        curr = self.head
        next = curr.getNext()
        while(next):
            curr.setNext(prev)
            prev = curr
            curr = next
            next = next.getNext()
        curr.setNext(prev)
        self.head = curr
        
        
    def getMiddle(self):
        if not self.length:
            return []
        
        slow = self.head
        fast = self.head
        while fast.getNext():
            fast = fast.getNext()
            if fast.getNext():
                fast = fast.getNext()
            else:
                return [slow, slow.getNext()]
            slow = slow.next
        return [slow]


# In[9]:


if __name__ == '__main__':
    print("Creating new list [1, 2, 4, 3]")
    l = LinkedList([1, 2, 4, 3])
    print(l)
    print("pushing nodes: 3, 1")
    l.push(3)
    l.push(1)
    print(l)
    print("Pushing node 5 at pos 4")
    l.push(5, 4)
    print(l)
    print("removing first node")
    l.pop()
    print(l)
    print("removing node at pos 3")
    l.pop(3)
    print(l)
    print("finding node with val=3")
    print(l.find(3))
    print("removing first node with val=3")
    print(l.remove(3))
    print(l)
    print("pushing nodes 6, 7")
    l.push(6)
    l.push(7)
    print(l)
    print("reversing list")
    l.reverse()
    print(l)
    print("creating empty list and pushing nodes 1, 2")
    m = LinkedList()
    m.push(1)
    m.push(2)
    print(m)
    print("pushing list onto another list at pos 1")
    l.pushLinkedList(m, 1)
    print(l)
    print("getting middle nodes")
    print(l.getMiddle()[0].getValue(), l.getMiddle()[1].getValue())
    print("pushing val=7")
    l.push(7)
    print(l)
    print("getting middle node")
    print(l.getMiddle()[0].getValue())
    print("getting length of list")
    print(l.getLength())
    print("removing all nodes with val=7")
    l.removeAll(7)
    print(l)
    print("creating array from linked list")
    l2 = l.toArray()
    print(type(l2), l2)
    print("creating linked list from array")
    l3 = LinkedList(l2)
    print(type(l3), l3)


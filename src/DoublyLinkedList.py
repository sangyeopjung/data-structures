
# coding: utf-8

# In[15]:


class Node(object):
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
        
    def setValue(self, value):
        self.value = value
        
        
    def getValue(self):
        return self.value
    
    
    def setPrev(self, prev):
        self.prev = prev
    
    
    def getPrev(self):
        return self.prev
    
    
    def setNext(self, next):
        self.next = next
    
    
    def getNext(self):
        return self.next
    
    
class DoublyLinkedList(object):
    """
    getLength()
    toArray()
    push(value, index)
    append(value)
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
                curr.getNext().setPrev(curr)
                curr = curr.getNext()
            self.tail = curr
        else:
            self.head = None
            self.tail = None
    
    
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
    
    
    def getTail(self):
        return self.tail
    
    
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
        
        if not index and 0 == self.length:
            self.head = Node(value, None, None)
            self.tail = self.head
            self.length += 1
            return

        elif not index:
            self.head = Node(value, None, self.head)
            self.head.getNext().setPrev(self.head)
            self.length += 1
            return
        
        elif index == self.length:
            self.tail = Node(value, self.tail, None)
            self.tail.getPrev().setNext(self.tail)
            self.length += 1
            return
            
        elif index < self.length/2:
            curr = self.head
            for _ in range(index-1):
                curr = curr.getNext()
            curr.setNext(Node(value, curr, curr.getNext()))
            curr = curr.getNext()
            curr.getNext().setPrev(curr)
            self.length += 1
            
        else:
            curr = self.tail
            for _ in range(self.length-index-1):
                curr = curr.getPrev()
            curr.setPrev(Node(value, curr.getPrev(), curr))
            curr = curr.getPrev()
            curr.getPrev().setNext(curr)
            self.length += 1
            
    
    def append(self, value):
        self.push(value, self.length)
        
        
    def pop(self, index=0):
        if index >= self.length:
            raise IndexError('Index out of range')
        
        if not index:
            out = self.head.getValue()
            self.head = self.head.getNext()
            self.length -= 1
            return out
        
        
        if index == self.length-1:
            out = self.tail.getValue()
            self.tail = self.tail.getNext()
            self.length -= 1
            return out
            
        
        if index < self.length/2:
            curr = self.head
            for _ in range(index):
                prev = curr
                curr = curr.getNext()
            out = curr.getValue()
            next = curr.getNext()
            prev.setNext(next)
            next.setPrev(prev)
            self.length -= 1
            return out
        else:
            curr = self.tail
            for _ in range(self.length-index-1):
                next = curr
                curr = curr.getPrev()
            out = curr.getValue()
            prev = curr.getPrev()
            next.setPrev(prev)
            prev.setNext(next)
            self.length -= 1
            return out
            
    
    
    def get(self, index):
        if index >= self.length:
            raise IndexError('Index out of range')
        
        if not index:
            return self.head.getValue()
        
        if index == self.length-1:
            return self.tail.getValue()
        
        if index < self.length/2:
            curr = self.head
            for _ in range(index):
                prev = curr
                curr = curr.getNext()
            return curr.getValue()
        else:
            curr = self.tail
            for _ in range(self.length-index-1):
                next = curr
                curr = curr.getPrev()
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
                    curr.getNext().setPrev(None)
                else:
                    prev.setNext(curr.getNext())
                    if not curr.getNext():
                        self.tail = prev
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
                    curr.getNext().setPrev(None)
                else:
                    prev.setNext(curr.getNext())
                    if not curr.getNext():
                        self.tail = prev
                curr = curr.getNext()
                self.length -= 1
                continue
            prev = curr
            curr = curr.getNext()
    
    
    def reverse(self):
        if not self.length:
            return
        
        self.tail = self.head
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


# In[17]:


if __name__ == '__main__':
    print("Creating new doubly linked list [1, 2, 4, 3]")
    l = DoublyLinkedList([1, 2, 4, 3])
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
    print("appending nodes 6, 7")
    l.append(6)
    l.append(7)
    print(l)
    print("reversing list")
    l.reverse()
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
    print("creating array from doubly linked list")
    l2 = l.toArray()
    print(type(l2), l2)
    print("creating doubly linked list from array")
    l3 = DoublyLinkedList(l2)
    print(type(l3), l3)


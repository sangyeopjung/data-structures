
# coding: utf-8

# In[1]:


class Heap(object):
    '''
    min heap
    '''
    def __init__(self, l=[]):
        self.heap = l
        i = len(self.heap) // 2 - 1
        while i >= 0:
            self._siftDown(i)
            i -= 1
            
    
    def __str__(self):
        return self.heap.__str__()
    
    
    def getSize(self):
        return len(self.heap)
    
    
    def insert(self, value):
        self.heap.append(value)
        self._siftUp(len(self.heap)-1)
    
    
    def deleteMin(self):
        if 0 == len(self.heap):
            return None
        
        if 1 == len(self.heap):
            return self.heap.pop()
        
        deleted = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._siftDown(0)
        return deleted
    
    
    def peek(self):
        if not len(self.heap):
            return None
        return self.heap[0]
    
    
    def _siftUp(self, i):
        while i:
            if self.heap[i] > self.heap[(i-1) // 2]:
                self.heap[i], self.heap[(i-1) // 2] = self.heap[(i-1) // 2], self.heap[i]
            i = (i-1) // 2

    
    def _siftDown(self, i):
        while i * 2 + 2 < len(self.heap):
            mc = self._maxChild(i)
            if self.heap[i] < self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc


    def _maxChild(self, i):
        if i * 2 + 2 > len(self.heap):
            return i * 2 + 1
        else:
            if self.heap[i*2+1] > self.heap[i*2+2]:
                return i * 2 + 1
            else:
                return i * 2 + 2
            
    
    def heapSort(self):
        heap = Heap(self.heap[:])
        out = []
        while len(heap.heap):
            out.append(heap.deleteMin())
        return out


# In[2]:


if __name__ == '__main__':
    heap = Heap([5, 1, 99, 2, 4])
    print(heap)
    heap.insert(3)
    print(heap)
    heap.insert(10)
    print(heap)
    heap.deleteMin()
    print(heap)
    heap.deleteMin()
    print(heap)
    print()
    heap2 = Heap()
    heap2.insert(5)
    heap2.insert(3)
    print(heap2)
    heap2.deleteMin()
    print(heap2)
    heap2.deleteMin()
    print(heap2)
    heap2.deleteMin()
    print(heap2)
    print()
    heap3 = Heap([24, 1, 74, 23, 12, 11, 55, 87, 63, 31])
    print('sorted: ', heap3.heapSort())
    print('not sorted: ', heap3)


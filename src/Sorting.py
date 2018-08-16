
# coding: utf-8

# In[1]:


def bubbleSort(array):
    operations = 0
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            operations += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return operations, array


def insertionSort(array):
    operations = 0
    for i in range(1, len(array)):
        current = array[i]
        j = i-1
        while array[j] > current and j >= 0:
            operations += 1
            array[j+1] = array[j]
            j-=1
        array[j+1] = current
    return operations, array


def selectionSort(array):
    operations = 0
    for i in range(len(array)-1):
        minid = i
        for j in range(i+1, len(array)):
            operations += 1
            if array[minid] > array[j]:
                minid = j
        array[i], array[minid] = array[minid], array[i]
    return operations, array

        
def mergeSort(array):
    if len(array) < 2:
        return 0, array
    
    mid = len(array) // 2
    oper_l, left = mergeSort(array[:mid])
    oper_r, right = mergeSort(array[mid:])
    oper_m, merged = _merge(left, right)
    
    return oper_l+oper_r+oper_m, merged


def _merge(left, right):
    operations = 0
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        operations += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if i == len(left):
        result.extend(right[j:])
        operations += 1
    elif j == len(right):
        result.extend(left[i:])
        operations += 1

    return operations, result


qsOper = 0
def quickSort(array, low=0, high=None):
    global qsOper
    
    if high is None:
        qsOper = 0
        high = len(array)-1
    
    if low < high:
        index = _partition(array, low, high)
        quickSort(array, low, index-1)
        quickSort(array, index+1, high)
    
    return qsOper, array


def _partition(array, low, high):
    global qsOper
    
    pivot = array[high]
    
    i = low-1
    for j in range(low, high):
        qsOper += 1
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
         
    i += 1   
    array[i], array[high] = array[high], array[i]
    return i


def binarySearch(array, value):
    low = 0
    high = len(array)-1
    
    while low <= high:
        mid = (low + high)//2
        if value < array[mid]:
            high = mid-1
        elif value > array[mid]:
            low = mid+1
        else:
            return mid
    
    return -1


# In[2]:


import random
array = [i for i in range(100)]
random.shuffle(array)
sortedArray = sorted(array)


# In[3]:


result = bubbleSort(array[:])
result[0], result[1]==sortedArray


# In[4]:


result = insertionSort(array[:])
result[0], result[1]==sortedArray


# In[5]:


result = selectionSort(array[:])
result[0], result[1]==sortedArray


# In[6]:


result = mergeSort(array[:])
result[0], result[1]==sortedArray


# In[7]:


result = quickSort(array[:])
result[0], result[1]==sortedArray


# In[8]:


rand = random.randint(1, 100)
rand, binarySearch(sortedArray, rand)


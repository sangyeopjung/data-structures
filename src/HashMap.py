
# coding: utf-8

# In[1]:


class HashMap(object):
    def __init__(self, size=100):
        self.size = size
        self.keys = [[] for i in range(self.size)]
        self.values = [[] for i in range(self.size)]
    
    
    def put(self, key, value):
        hashed = hash(key) % self.size
        
        try:
            index = self.keys[hashed].index(key)
        except ValueError:
            index = -1
        
        if index < 0:
            self.keys[hashed].append(key)
            self.values[hashed].append(value)
        else:
            self.values[hashed][index] = value
    
    
    def get(self, key):
        hashed = hash(key) % self.size
        
        try:
            index = self.keys[hashed].index(key)
        except ValueError:
            return None
        
        return self.values[hashed][index]
    

    def __getitem__(self,key):
        return self.get(key)

    
    def __setitem__(self,key,data):
        self.put(key,data)


# In[2]:


if __name__ == '__main__':
    hm = HashMap(10)
    hm.put('Amy', 20)
    hm['Bob'] = 30
    hm.put('Chad', 40)
    print(hm['Amy'])
    print(hm.get('Bob'))
    print(hm['David'])


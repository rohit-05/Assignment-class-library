#!/usr/bin/env python
# coding: utf-8

# In[105]:


class LCG:
    def __init__(self, seed, multiplier, increment, modulus, length):
        self.seed = seed
        # a = multiplier ; 0 < a < M
        self.multiplier = multiplier 
        
        # 0 <= c < m : c = increment 
        self.increment =  increment
        #
        self.modulus =  modulus
        self.length = length

    
    def initialize_generator(self) : 
        seed = ((self.multiplier * self.seed) + self.increment) % self.modulus
        print(seed)
        return seed
    
    def give_next_random_number(self) :
        seed = self.seed +1
        next_seed = ((self.multiplier*seed) + self.increment) % self.modulus
        self.seed = next_seed
        return next_seed
    
    def give_sequence(self) :
        list = []
        seed = self.seed
        for i in range(1, self.length):
            one = ((self.multiplier * seed) + self.increment) % self.modulus
            
            list.append(one)
            seed = seed + i
        
        return list
        


# In[ ]:





# In[106]:


inst = LCG(1, 1103515245, 12345, pow(2,32),10000)


# In[107]:


inst.initialize_generator()


# In[108]:


inst.give_next_random_number()


# In[111]:


print(inst.give_sequence())


# In[112]:



class SCG(LCG):
    
    def __init__(self,  seed, modulus):
        if seed % 4 != 2:
            raise ValueError("Seed is not correct")
        else :
            self.seed = seed
            self.modulus = modulus

    def next_ramdom_number(self):
        seed = self.seed + 1
        next_num = (self.seed* seed) % self.modulus
        return next_num


# In[99]:


y = SCG(2, pow(2,32))

print(y.next_ramdom_number())


# In[ ]:




# In[ ]:


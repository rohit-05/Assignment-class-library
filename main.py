#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np


# In[4]:


class Rectangular:
    def __init__(self, breadth, length):
        
        self.breadth = breadth
        self.length = length
        
    def cal_area(self):
        formula =  self.breadth * self.length
        return formula
    
    def cal_perimeter(self):
        formula = 2 * (self.breadth + self.length)
        return formula   


# In[11]:


# instance of class Rectangle
x1 = Rectangular(14,9)       
print('Area of rectangle      :', x1.cal_area())
print('Perimter of rectangle  :', x1.cal_perimeter())


# In[13]:


# inherited class
class Square(Rectangular):
    def __init__(self, length):
        
        Rectangular.__init__(self, length, length)
# instance of class Square        
x2 = Square(10)

print('Area of square      :', x2.cal_area())
print('Perimter of square  :', x2.cal_perimeter())


# In[15]:


# Question 1.2
# Part A
length_np = np.array( [ 23,25,27,29,31,33,35,37,39,41] ) 
width_np = np.array( [ 4,6,8,10,12,14,16,18,20,22] ) 


# In[19]:


# Question 1.2
# Part B
x3 = Rectangular(length_np,width_np)       
print('Area ' ,x3.cal_area())
print('Perimeter ' ,x3.cal_perimeter())


# In[ ]:





class Time:
    def __init__(self, h, m, s):
        self.hr = h
        self.min = m
        self.sec = s
        
    def displayTime(t0):
        return "({:02d}:{:02d}:{:02d})".format(t0.hr, t0.min, t0.sec)
    
    def DisplayMinute(t_sec):
        return t_sec.hr*3600 + t_sec.min*60 + t_sec.sec
        
    def addTime(t1, t2):
        
        a_min = 0
        a_hr = 0
        s_sec = 0
        s_hr = 0
        s_min = 0
        
        time = Time(0,0,0)
        
        s_sec = t1.sec + t2.sec
        
        if s_sec >= 60:
            a_min = s_sec // 60
            s_sec = s_sec - 60
            
            
        s_min = t1.min + t2.min + a_min
        
        if s_min >= 60:
            a_hr = s_min // 60
            s_min = s_min - 60
            
            
        s_hr = t1.hr + t2.hr + a_hr
        
        time.hr = s_hr
        time.min = s_min
        time.sec = s_sec
        
        return time
    

t1 = Time(3,24,19)

t2 = Time(1,29,58)

t3 = t1.addTime(t2)

print(t3.displayTime())

print(t3.DisplayMinute(), 'seconds')

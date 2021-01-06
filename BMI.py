#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BMI:
    
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        self.bmi=self.weight/(self.height*self.height)
    
    def get_name(self):
        #print(self.name)
        return self.name
    
    def get_bmi(self):
        
        return self.bmi
    
    def get_status(self):
        if self.bmi<18.5:
            self.status="偏瘦"
        elif self.bmi >= 18.5 and self.bmi < 24:
            self.status="正常"
        elif self.bmi >= 24 and self.bmi < 30:
            self.status="偏胖"
        return self.status


# In[2]:


bmi1=BMI("zhangsan",18,60,1.7) #实例化


# In[3]:


print("{}的bmi是：{}，身体状态是：{}".format(bmi1.get_name(),bmi1.get_bmi(),bmi1.get_status()))


# In[ ]:





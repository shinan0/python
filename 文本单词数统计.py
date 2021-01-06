#!/usr/bin/env python
# coding: utf-8

# In[6]:


f=open(r'C:\Users\Administrator\Desktop\Walden.txt','r')


# In[7]:


f.readlines()


# In[20]:


import string
with open(r'C:\Users\Administrator\Desktop\Walden.txt','r',encoding='utf-8') as text:
    raw_words=text.read().split()
    words_list=[word.strip(string.punctuation).lower()for word in raw_words]
    words_set=set(words_list)
    words_dict={keyword:words_list.count(keyword) for keyword in words_set}
for word in sorted(words_dict.items(),key = lambda word: word[1], reverse=True):
    print('{}--{} times'. format(word[0], word[1]))


# In[ ]:





# In[ ]:





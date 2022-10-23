#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import requests
import json
from bs4 import BeautifulSoup as bs


# In[13]:


r = requests.get('https://www.naturally-pam.com/products')
html = bs(r.content, 'html.parser')


# In[138]:


result = []
for i in html.select(".rowItem"):
    header = i.find("h3")
    href = 'https://www.naturally-pam.com'+[a['href'] for a in i.find_all('a', href=True)][0]
    config = i.find("label")
    price = i.find('div',class_='pricebox')
    price1 = price.find('label')
    price2 = price.find('span')
    price3 = i.find('span', class_='pricePerPortion')
    dt = {'Header':header.text, 
          'href': href, 
          'config':config.text, 
          "price":price1.text, 
          "price_val": price2.text, 
          "price_kg":price3.text}
    result.append(dt)

print(pd.DataFrame(result))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests 

download_url='https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv'

response= requests.get(download_url) 

with open('nba_all_elo.csv', 'wb') as f: 
    f.write(response.content)
    
nba= pd.read_csv('nba_all_elo.csv')
nba.head()


# In[2]:


Knicks_pts_by_year=nba[nba['fran_id']=='Knicks'].groupby('year_id')['pts'].sum()


# In[3]:


Knicks_pts_by_year


# In[4]:


Knicks_pts_by_year.plot()


# In[6]:


Knicks_pts_by_year.tail(10).plot(kind='bar')


# In[11]:


nba[ (nba['fran_id'] =='Knicks' ) & ( nba['year_id'] >2000 )].plot(kind='scatter', x='pts', y='opp_pts', s=0.5)


# In[12]:


nba[nba['pts']==nba['opp_pts']].empty


# In[16]:


heat_13_w1 = nba[(nba['fran_id'] == 'Heat') & (nba['year_id'] == 2013)]['game_result'].value_counts()
heat_13_w1


# In[21]:


heat_13_w1 = nba[(nba['fran_id'] == 'Heat') & (nba['year_id'] == 2013)].groupby('game_result')['game_result'].count()
heat_13_w1


# In[22]:


heat_13_w1.plot(kind='pie')


# In[ ]:





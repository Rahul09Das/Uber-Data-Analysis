
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')
import pandas
import seaborn
import numpy
import matplotlib


# In[2]:


#LOAD CSV


# In[5]:


data = pandas.read_csv('C:/ProgramData/Anaconda3/Scripts/uber-raw-data-apr14.csv')


# In[6]:


data.tail()


# In[7]:


data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)


# In[8]:


data.tail()


# In[9]:


def get_dom(dt):
    return dt.day

data['dom'] = data['Date/Time'].map(get_dom)


# In[10]:


data.tail()


# In[11]:


def get_weekday(dt):
    return dt.weekday()

data['weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour

data['hour'] = data['Date/Time'].map(get_hour)


# In[12]:


data.tail()


# In[ ]:


#ANALYSE THE DOM


# In[13]:


hist(data.dom, bins=30, rwidth=.8, range=(0.5, 30.5))
xlabel('date of the month')
ylabel('frequency')
title('Frequency by DoM - uber - Apr 2014')


# In[14]:


#for k, rows in data.groupby('dom'):
#    print((k, len(rows)))
 
def count_rows(rows):
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)
by_date


# In[15]:


bar(range(1, 31), by_date)


# In[18]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[19]:


bar(range(1, 31), by_date_sorted)
xticks(range(1,31), by_date_sorted.index)
xlabel('date of the month')
ylabel('frequency')
title('Frequency by DoM - uber - Apr 2014')
("")


# In[20]:


#ANALYSE BY HOUR


# In[21]:


hist(data.hour, bins=24, range=(.5, 24))


# In[22]:


#ANALYSE BY WEEKDAY


# In[23]:


hist(data.weekday, bins=7, range =(-.5,6.5), rwidth=.8, color='#AA6666', alpha=.4)
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())


# In[24]:


#CROSS ANALYSIS (hour,dow)


# In[25]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[26]:


seaborn.heatmap(by_cross)


# In[27]:


#BY LAT AND LON


# In[29]:


hist(data['Lat'], bins=100, range = (40.5, 41))
("")


# In[30]:


hist(data['Lon'], bins=100, range = (-74.1, -73.9));


# In[31]:


hist(data['Lon'], bins=100, range = (-74.1, -73.9), color='g', alpha=.5, label = 'longitude')
grid()
legend(loc='upper left')
twiny()
hist(data['Lat'], bins=100, range = (40.5, 41), color='r', alpha=.5, label = 'latitude')
legend(loc='best')
("")


# In[32]:


figure(figsize=(20, 20))
plot(data['Lon'], data['Lat'], '.', ms=1, alpha=.5)
xlim(-74.2, -73.7)
ylim(40.7, 41)


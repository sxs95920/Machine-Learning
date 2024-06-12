#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


#1. Read the provided CSV file ‘data.csv’

df = pd.read_csv("data.csv")


# In[4]:


df.head()


# In[5]:


#2. Show the basic statistical description about the data.
df.describe()


# In[7]:


#3. Check if the data has null values.
df.isnull().sum()


# In[10]:


#a. Replace the null values with the mean
x = df['Calories'].mean()
print(x)


# In[12]:


df['Calories'].fillna(x,inplace = True)


# In[14]:


df.isnull().sum()


# In[17]:


#4.Select at least two columns and aggregate the data using: min, max, count, mean.

selected_columns = ['Duration', 'Pulse']
aggregation = df[selected_columns].agg(['min','max','count','mean'])
print(aggregation)


# In[20]:


#5.Filter the dataframe to select the rows with calories values between 500 and 1000.

filtered_df = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]
print(filtered_df)


# In[22]:


#6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100

filter_df = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print(filter_df)


# In[23]:


#7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.

df_modified = df.drop(columns=['Maxpulse'])
print(df_modified)


# In[24]:


#8. Delete the “Maxpulse” column from the main df dataframe

df.drop(columns=['Maxpulse'], inplace=True)
print(df)


# In[28]:


#9. Convert the datatype of Calories column to int datatype.
df['Calories'] = df['Calories'].astype(int)
df.dtypes


# In[ ]:





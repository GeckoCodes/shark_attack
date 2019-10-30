#!/usr/bin/env python
# coding: utf-8

# # SQL Connection to Python using ODBC

# In[52]:


import pyodbc


# Three stages are:
# 1. Connection to server.
# 2. Cursor ( object that can hold the data - is iterable).
# 3. Execute a query - can iterate through rows of the data produced.

# In[64]:


connection = pyodbc.connect('DSN=kubricksql;UID=de14;PWD=password')


# In[65]:


cur = connection.cursor()


# In[67]:


#q = 'SELECT * FROM daniel.shark'
# Very hard with all single quotes
# q = 'INSERT INTO daniel.shark ([attack_date], [case_number], [country], [activity], [age], [gender], [is_fatal]) VALUES(\'2019-10-30', 'Test_number123', 'Australia', 'Swimming', \24, 'm', 0);

q = 'INSERT INTO daniel.shark ([attack_date], [case_number], [country], [activity], [age], [gender], [is_fatal]) VALUES (?,?,?,?,?,?,?)'




# In[28]:





# In[68]:



# # Shark Data Exercise

# In[1]:


import csv
from datetime import datetime, timedelta


# In[2]:


sharkfile = r'C:\data\Shark_attack_data.csv'


# In[3]:


# Initialise Lists
attack_date = []
case_num = []
country = []
activity = []
age = []
gender = []
is_fatal = []

with open(sharkfile) as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Append values to lists
        attack_date.append(row['Date'])
        case_num.append(row['Case Number'])
        country.append(row['Country'])
        activity.append(row['Activity'])
        age.append(row['Age'])
        gender.append(row['Sex '])
        is_fatal.append(row['Fatal (Y/N)'])


# In[4]:


# Zip the contents of the list together
data_zip = zip(attack_date, case_num, country, activity, age, gender, is_fatal)


# ## Populating SQL table

# In[5]:


import pyodbc


# In[6]:


connection = pyodbc.connect('DSN=kubricksql;UID=de14;PWD=password')


# In[7]:


cur = connection.cursor()


# In[ ]:


# Truncate - wipe and load
cur.execute('TRUNCATE TABLE daniel.shark')


# In[8]:


q = 'INSERT INTO daniel.shark ([attack_date], [case_number], [country], [activity], [age], [gender], [is_fatal]) VALUES (?,?,?,?,?,?,?)'


# In[9]:


for d in data_zip:
    try:
        cur.execute(q, d)
        connection.commit()
    except:
        connection.rollback()


# In[ ]:





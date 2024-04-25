#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


benin_data = pd.read_csv(r"C:\Users\Tsi\Desktop\10academy\Task 1\src\benin-malanville.csv")


# In[5]:


Togo_data = pd.read_csv(r"C:\Users\Tsi\Desktop\10academy\Task 1\src\togo-dapaong_qc.csv")


# In[31]:


sierraleone_data = pd.read_csv(r"C:\Users\Tsi\Desktop\10academy\Task 1\src\sierraleone-bumbuna.csv")


# Working on Benin Dataset

# In[5]:


benin_data.head()


# In[ ]:


benin_data.shape


# In[ ]:


#Clean the data check if their are null values in the data
benin_data.isnull().sum()


# In[19]:


# delete the last column since there is no data on the coments since we have a null value in the comment column
benin_data = benin_data.iloc[:, :-1]


# In[20]:


# Save the updated data to a new CSV file
benin_data.to_csv('updated_file.csv', index=False)


# In[ ]:


benin_data


# In[ ]:


benin_data.shape


# In[6]:


benin_data.describe()


# In[7]:


# Calculate statistical measures for each numeric column
numeric_columns = benin_data.select_dtypes(include='number')

statistics = {
    'Column': [],
    'Mean': [],
    'Median': [],
    'Standard Deviation': [],
    # Add more statistical measures if needed
}


# In[8]:


for column in numeric_columns:
    statistics['Column'].append(column)
    statistics['Mean'].append(numeric_columns[column].mean())
    statistics['Median'].append(numeric_columns[column].median())
    statistics['Standard Deviation'].append(numeric_columns[column].std())


# In[9]:


# Create a DataFrame from the statistics dictionary
statistics_df = pd.DataFrame(statistics)


# In[10]:


# Print the statistics benin
print(statistics_df)


# In[ ]:


#timeseries analysis
plt.plot(benin_data['Timestamp'], benin_data['Tamb'])
plt.xlabel('Timestamp')
plt.ylabel('Tamb')
plt.title('Line Chart')
plt.show()

plt.plot(benin_data['Timestamp'], benin_data['WD'])
plt.xlabel('Timestamp')
plt.ylabel('Tamb')
plt.title('Line Chart')
plt.show()


# In[22]:


#histogram analysis
fig, ax=plt.subplots(1,2, figsize=(20, 6))
sns.histplot(benin_data['Tamb'], ax=ax[0])
ax[0].set_title("Ambiant temp over time")
sns.histplot(benin_data['GHI'], ax=ax[1])
ax[1].set_title("GHI (W/m²) over time")
sns.histplot(benin_data['WS'], ax=ax[2])
ax[2].set_title("WS over time")
plt.ylim(0, 2500)


# In[ ]:


#scater plot analysis
a4_dims = (20, 7)
fig, axs = plt.subplots(ncols=3, figsize=a4_dims)
sns.scatterplot(x="Timestamp", y="Tamb", ax=axs[0], benin_data=benin_data)
sns.scatterplot(x="Timestamp", y="DNI", ax=axs[1], benin_data=benin_data)
sns.scatterplot(x="Timestamp", y="WSgust", ax=axs[2], benin_data=benin_data)
plt.show()


# In[43]:


#wind analysis
a4_dims = (20, 7)
fig, axs = plt.subplots(ncols=3, figsize=a4_dims)
sns.scatterplot(x="WS", y="WSgust", data=benin_data, ax=axs[2])
plt.show()


# Working for Togo

# In[23]:


Togo_data.head()


# In[9]:


Togo_data.shape


# In[24]:


#Clean the data check if their are null values in the data
Togo_data.isnull().sum()


# In[25]:


Togo_data = Togo_data.iloc[:, :-1]


# In[26]:


# Save the updated data to a new CSV file
Togo_data.to_csv('updated_file1.csv', index=False)


# In[27]:


Togo_data.shape


# In[28]:


Togo_data.describe()


# In[ ]:


#timeseries analysis
plt.plot(Togo_data['Timestamp'], Togo_data['Tamb'])
plt.xlabel('Timestamp')
plt.ylabel('Tamb')
plt.title('Line Chart - Togo Tamb')
plt.show()

plt.plot(Togo_data['Timestamp'], Togo_data['WD'])
plt.xlabel('Timestamp')
plt.ylabel('WD')
plt.title('Line Chart - Togo WD')
plt.show()


# In[30]:


#histogram analysis
fig, ax=plt.subplots(1,2, figsize=(20, 6))
sns.histplot(Togo_data['Tamb'], ax=ax[0])
ax[0].set_title("Ambiant temp over time")
sns.histplot(Togo_data['GHI'], ax=ax[1])
ax[1].set_title("GHI (W/m²) over time")
sns.histplot(Togo_data['WS'], ax=ax[2])
ax[2].set_title("WS over time")
plt.ylim(0, 2500)


# In[20]:


#scater plot analysis
a4_dims = (20, 7)
fig, axs = plt.subplots(ncols=3, figsize=a4_dims)
sns.scatterplot(x="Timestamp", y="Tamb", ax=axs[0], Togo_data=benin_data)
sns.scatterplot(x="Timestamp", y="DNI", ax=axs[1], Togo_data=benin_data)
sns.scatterplot(x="Timestamp", y="WSgust", ax=axs[2], Togo_data=benin_data)
plt.show()


# In[41]:


#wind analysis
a4_dims = (20, 7)
fig, axs = plt.subplots(ncols=3, figsize=a4_dims)
sns.scatterplot(x="WS", y="WSgust", data=Togo_data, ax=axs[2])
plt.show()


# Working with Sierra Leone 

# In[32]:


sierraleone_data.head()


# In[33]:


sierraleone_data.shape


# In[34]:


#Clean the data check if their are null values in the data
sierraleone_data.isnull().sum()


# In[35]:


sierraleone_data = sierraleone_data.iloc[:, :-1]


# In[36]:


# Save the updated data to a new CSV file
sierraleone_data.to_csv('updated_file1.csv', index=False)


# In[37]:


sierraleone_data.shape


# In[38]:


sierraleone_data.describe()


# In[ ]:


#timeseries analysis
plt.plot(Togo_data['Timestamp'], sierraleone_data['Tamb'])
plt.xlabel('Timestamp')
plt.ylabel('Tamb')
plt.title('Line Chart - sierraleone Tamb')
plt.show()

plt.plot(Togo_data['Timestamp'], sierraleone_data['WD'])
plt.xlabel('Timestamp')
plt.ylabel('WD')
plt.title('Line Chart - sierraleone WD')
plt.show()


# In[39]:


#histogram analysis
fig, ax=plt.subplots(1,2, figsize=(20, 6))
sns.histplot(sierraleone_data['Tamb'], ax=ax[0])
ax[0].set_title("Ambiant temp over time")
sns.histplot(sierraleone_data['GHI'], ax=ax[1])
ax[1].set_title("GHI (W/m²) over time")
sns.histplot(sierraleone_data['WS'], ax=ax[2])
ax[2].set_title("WS over time")
plt.ylim(0, 2500)


# In[ ]:


#scater plot analysis
a4_dims = (20, 7)
fig, axs = plt.subplots(ncols=3, figsize=a4_dims)
sns.scatterplot(x="Timestamp", y="Tamb", ax=axs[0], sierraleone_data=sierraleone_data)
sns.scatterplot(x="Timestamp", y="DNI", ax=axs[1], sierraleone_data=sierraleone_data)
sns.scatterplot(x="Timestamp", y="WSgust", ax=axs[2], sierraleone_data=sierraleone_data)
plt.show()


# In[40]:


#wind analysis
a4_dims = (20, 7)
fig, axs = plt.subplots(ncols=3, figsize=a4_dims)
sns.scatterplot(x="WS", y="WSgust", data=sierraleone_data, ax=axs[2])
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[2]:


data = pd.read_csv('Mobile_data_Flipkart.csv')  # Make sure to replace 'your_data.csv' with the actual file path

# Create the Streamlit web app
st.title('Product Information')

# Display the data in a table
st.dataframe(data)



# In[ ]:





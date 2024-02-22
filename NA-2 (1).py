#!/usr/bin/env python
# coding: utf-8

# Q1: Which type of data can be used while creating a series object in pandas?
# 
# The data types that can be used in a pandas Series include:
# Integer: int
# Float: float
# Complex: complex
# Boolean Type:
# bool
# Datetime Types:
# datetime64
# Timedelta Type:
# timedelta64
# String Type:
# object (though this allows mixed data types and is generally used for string data)
# Categorical Type:
# category (a pandas-specific data type for categorical data)
# Custom Objects:
# You can use custom objects or other data types, and pandas will try to infer the appropriate data type.

# Q2: Create a series having the month's number as data and assign name as their index values?

# In[4]:


import pandas as pd
years={"january": 1, "february": 2,"march":3, 
       "april":4,"may":5,"june":6, "july":7,"augest":8,
       "september":9,"october":10,"november":11,
       "december":12
    }
months=pd.Series(years)
print(months)


# Write a program to create a series object using the dictionary which store the number of students in fresh batch groups ( MatMIE, Mat DAIS, COMIE, COMEC)?

# In[1]:


import pandas as pd
group={"matmie":33, "matdais":30, "comse":28, "comie":25}
s=pd.Series(group)
print(s)


# Q4: Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
# 

# In[3]:


import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 

df = pd.DataFrame(exam_data, index=labels)

print(df)


# Q5: Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2

# In[4]:


import numpy as np
import pandas as pd
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

result = df[df['attempts'] > 2]

print(result)


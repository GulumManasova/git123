1- Which type of data can be used while creating a series object in pandas?

The data types that can be used in a pandas Series include:
Integer: int
Float: float
Complex: complex
Boolean Type:
bool
Datetime Types:
datetime64
Timedelta Type:
timedelta64
String Type:
object (though this allows mixed data types and is generally used for string data)
Categorical Type:
category (a pandas-specific data type for categorical data)
Custom Objects:
You can use custom objects or other data types, and pandas will try to infer the appropriate data type.

2- Create a series having the month's number as data and assign name as their index values? 

import pandas as pd
years={"january": 1, "february": 2,"march":3, 
       "april":4,"may":5,"june":6, "july":7,"augest":8,
       "september":9,"october":10,"november":11,
       "december":12
    }
months=pd.Series(years)
print(months)

3-Write a program to create a series object using the dictionary which store the number of students in fresh batch groups ( MatMIE, Mat DAIS, COMIE, COMEC)?

import pandas as pd
group={"matmie":33, "matdais":30, "comse":28, "comie":25}
s=pd.Series(group)
print(s)




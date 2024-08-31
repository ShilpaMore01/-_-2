# -*- coding: utf-8 -*-
"""Exploratory Data Analysis (EDA) on Retail Sales Data

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SGGciD4VXKX2d6lXlBKSzIalwieqI83k
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv("/content/Warehouse_and_Retail_Sales.csv")

data

data.head(50)

data.tail(50)

data.describe()

data.info()

print(data.isnull().sum())

data1 = data.dropna()
data1.reset_index(drop=True, inplace=True)

data1 = data[(data['RETAIL SALES'] >= 0) & (data1['RETAIL TRANSFERS'] >= 0) & (data1['WAREHOUSE SALES'] >= 0)]

data.describe()

plt.figure(figsize = (8,6))
sns.barplot(x = data["YEAR"] , y = data["RETAIL SALES"], data = data)
plt.show()

plt.figure(figsize = (8,6))
sns.barplot(x = data["MONTH"] , y = data["RETAIL SALES"], data = data)
plt.show()

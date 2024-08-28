# -*- coding: utf-8 -*-
"""Ridge,lasso regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G1eHMakREjbno7NAoj4lu5SBkN3uGFCk
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

dataset=pd.read_csv("/content/Algerian_forest_fires_dataset.csv")

dataset.head()

dataset.info()

# data cleaning

dataset.isnull().sum()

dataset[dataset.isnull().any(axis=1)]

dataset.loc[:122,'Region']=0
dataset.loc[122:,'Region']=1
df=dataset

df.info()

df['Region']=df[['Region']].astype(int)

df.head()

df.tail()

# remove the null value
df.drop(122,axis=0,inplace=True)

df.isnull().sum()

df.drop(125,axis=0,inplace=True)

df.info()

df.isnull().sum()

df.dropna(inplace=True)
df.reset_index(inplace=True)

df.head()

df.isnull().sum()

df.iloc[[122]]

df=df.drop(122).reset_index(drop=True)

df.iloc[[122]]

df.columns

# fixed spaces in coloumn name

df.columns=df.columns.str.strip()

df.columns

# change the requested coloumn as int
df['Temperature'] = df['Temperature'].astype(int)
df['month'] = df['month'].astype(int)
df['year'] = df['year'].astype(int)
df['day'] = df['day'].astype(int)
df['RH'] = df['RH'].astype(int)
df['Ws'] = df['Ws'].astype(int)

df.info()

# changing the other coloumn to float

objects=[features for features in df.columns if df[features].dtypes=='O']

for i in objects:
  if i!="Classes":
    df[i]=df[i].astype(float)

objects

df.describe()

# lets save clean data

df.to_csv("/content/Algerian_forest_fires_cleaned_dataset.csv",index=False)

df_copy=df.drop(['day','month','year'],axis=1)

df_copy.head()



df_copy.head()

df_copy['Classes'].value_counts()

# encoding categries in classes

# encoding categries in classes
# Check if 'Classes' column is of type string
if df_copy['Classes'].dtype == 'object':
    df_copy['Classes'] = np.where(df_copy['Classes'].str.contains('not'), 0, 1)
else:
    print("Warning: 'Classes' column is not of type string. Skipping encoding.")

df_copy['Classes'].value_counts()

df_copy.head()

# density plot

plt.style.use('seaborn')
df_copy.hist(bins=50,figsize=(20,15))
plt.show()


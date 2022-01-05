import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

# 1
# Manual

# 2
# Import and concat all files
import glob

files = glob.glob("states*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)
us_census.reset_index(drop=True, inplace=True)

# 3
# Examine datatypes

print(us_census.columns)
print(us_census.dtypes)

# 4
# Examine df

print(us_census.head())

# 5
# Convert Income column from object to numeric

us_census.Income = us_census.Income.str[1:]
us_census.Income = pd.to_numeric(us_census.Income)
print(us_census.dtypes)

# 6
# Split GenderPop

gender_split = us_census['GenderPop'].str.split("_")
us_census['Men'] = gender_split.str.get(0)
us_census['Women'] = gender_split.str.get(1)
print(us_census.head())

# 7
# Convert Men / Women to numeric

us_census.Men = us_census.Men.str.split('(\d+)', expand=True)[1]
us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = us_census.Women.str.split('(\d+)', expand=True)[1]
us_census.Women = pd.to_numeric(us_census.Women)
print(us_census)

# 8
# Scatterplot
# plt.scatter(us_census.Women, us_census.Income)
# plt.show()

# 9
# Fill Nan's
us_census.Women = us_census.Women.fillna(us_census.TotalPop - us_census.Men)
print(us_census.Women)

# 10
# Check for duplicates

print(us_census.duplicated())

# 11
# Drop duplicates
us_census.drop_duplicates()

# 12
# Scatterplot

# plt.scatter(us_census.Women, us_census.Income)
# plt.show()

# 13
# Columns for histograms

print(us_census.columns)

# 14
# Clean up for Histograms

us_census.Hispanic = us_census.Hispanic.str[0:-1]
us_census.Hispanic = pd.to_numeric(us_census.Hispanic)
us_census.White = us_census.White.str[0:-1]
us_census.White = pd.to_numeric(us_census.White)
us_census.Black = us_census.Black.str[0:-1]
us_census.Black = pd.to_numeric(us_census.Black)
us_census.Native = us_census.Native.str[0:-1]
us_census.Native = pd.to_numeric(us_census.Native)
us_census.Asian = us_census.Asian.str[0:-1]
us_census.Asian = pd.to_numeric(us_census.Asian)
us_census.Pacific = us_census.Pacific.str[0:-1]
us_census.Pacific = pd.to_numeric(us_census.Pacific)

us_census = us_census.fillna(value={"Pacific":us_census.Pacific.mean()})

us_census.drop_duplicates()

plt.hist(us_census.Hispanic, bins=10)
plt.hist(us_census.White, bins=10)
plt.show()

# print(us_census)

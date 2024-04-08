import pandas as pd
import numpy as np

# Creating a dummy dataset
data = {
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
'Age': [25, 30, 35, 40, 45],
'Salary': [50000, 60000, 70000, 80000, 90000],
'Department': ['HR', 'IT', 'Finance', 'HR', 'IT'],
'Start_Date': pd.to_datetime(['2020-01-01', '2019-03-15', '2021-05-20', '2018-09-10', '2022-02-28']),
'Experience': [5, 10, 3, 15, 2],
'Rating': [4.2, 3.8, 4.5, 4.0, 4.7]
}

df=pd.DataFrame(data)
# print(df)

# question 1:select the data whose age is greater then 30
subset1=df[df['Age']>30]
subset=pd.DataFrame(subset1)
# print(subset)

# question 3:  Summary the stats of dat
summary_stats=df[['Name','Age','Salary','Department','Start_Date','Experience','Rating']].describe()
# print(summary_stats)

# question 4:reshaping the data
"""reshape_data=df.melt(id_vars=['Name','Age','Start_Date','Experience','Rating','Salary'],
                     var_name='Department',value_name='Value')"""
# print(reshape_data)

# question 5:  Combining the data from two table
"""merge_data={'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Bonus':[5000,7000,4000,100000,8000]}
merge_data1=pd.DataFrame(merge_data)
print(merge_data1)
merge_data2=pd.merge(df,merge_data1,on='Name')
print(merge_data2)"""

# question 6:
"""df['new_col']=df['New_Name'].aaply(lambda x:len(x))
print(df)"""

# question 7:
"""filter_data=df[(df['Department']=='IT')&(df['Age']>30)]
print(filter_data)"""

# question 10:
sorted_data=df.sort_values(by="Age",
                           ascending=False)
print(sorted_data)
import urllib.request
from urllib.request import urlretrieve
import pandas

data = pandas.read_csv("C:\\Users\\Faisal\\Downloads\\covid_data.csv")
print(data.head())


# print(data.info())
# print(data.describe())
# print(data.iloc[3])
# print(data.loc[1])
# #print(data.explode('Country'))
# print(data.at[4, 'Country'])

data = pandas.read_csv("C:\\Users\\Faisal\\Downloads\\salesdata.csv")
# print(data.head())


# print(data.info())
# print(data.describe())
# print(data.iloc[3])
# print(data.loc[1])
# #print(data.explode('Country'))
# print(data.at[4, 'Product'])
# print(data["Sales"].idxmax())
print(data.iloc[[2,6,5],[1,3]])





































































































































































# a = 0
# b = 0
# data = pandas.read_csv("C:\\Users\\Faisal\\Downloads\\Tehsil Schools.csv")
# print(data.head())
# for i in range(86):
#     if data.at[i, 'No. of students passed in 10th Exam, 2014'] == 0:
#         print(data.at[i, 'Name of School'])
# for i in range(86):
#     if data.at[i, 'No. of Students  in 9th (2012) as per Registeration'] > 50:
#         a += 1   
# print('Percentage of large schools are', a/86*100)

# for i in range(86):
#     if data.at[i, 'No. of Students  in 9th (2012) as per Registeration'] > 20:
#         a=data.at[i, 'No. of students passed in 10th Exam, 2014']/data.at[i, 'No. of Students  in 9th (2012) as per Registeration']*100
#         if a > b:
#             b = a
#             c = i
# print('The best headmaster of the school is from', data.at[c, 'Name of School'], 'with', b, 'percent!')    
# print(c)
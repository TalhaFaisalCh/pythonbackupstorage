import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv("C:\\Users\\Faisal\\Downloads\\Ecommerce_Dataset.csv")
for i in range(500):
    x=data.at[i, 'Length of Membership']
    y=data.at[i, 'Yearly Amount Spent']
    plt.scatter(x,y)

plt.show()
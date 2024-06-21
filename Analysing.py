import pandas as pd #importing pandas
import numpy as np #importing numpy
import matplotlib.pyplot as plt #imporint matplotlib

#creating a variable that contains scores 
scores=pd.read_csv('Aim Traning.csv')

#calculating mean of 2nd coloum 
mean=scores['Smooth Strafe Sphere Easy'].mean()

#printing the scores & mean of Smooth Strafe Sphere Easy
print(scores)
print("The mean of Smooth Strafe Sphere Easy is: ", mean )

#printing data at 22nd may 2024
print (scores[scores["Date"]=="22nd May 2024"]

#creating a graph of Smooth Strafe Sphere Easy
x=np.array(scores[scores["Date"]])
y=np.array(scores[scores["Smooth Strafe Sphere Easy")
plt.plot(x,y)
plt.show()


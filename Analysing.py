import pandas as pd #importing pandas

#creating a variable that contains scores 
scores=pd.read_csv('Aim Traning.csv')

#calculating mean of 2nd coloum 
mean=scores['Smooth Strafe Sphere Easy'].mean()


#printing data at 22nd may 2024
print (scores[scores["Date"]=="22nd May 2024"]

#printing the scores
print(scores)
print("The mean of Smooth Strafe Sphere Easy is: ", mean )

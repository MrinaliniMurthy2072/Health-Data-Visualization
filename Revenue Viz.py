#Import all the necessary libraries 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
#Initializing an empty figure 
fig = plt.figure() 
#Creating a subplot within an empty figure 
fig,ax = plt.subplots(1,1) 
#Pre-setting the style of the plot 
plt.style.use('ggplot') 
#Using pandas to access and read the data frame 
df = pd.read_csv("C:\\Users\\Minnie\\Desktop\\bar chart lesggo.csv") 
#Preliminary exploration of the dataset 
print(df.head()) 
print(df.info()) 
#Cleaning up any missing values and duplicates 
df.drop_duplicates() 
df.dropna() 
#Selected the required columns and rows 
df = df[['Name','Revenue (USD millions)']] 
print(df) 
#Convert the dataframe into a matrix using numpy 
matrix = df.to_numpy() 
print(matrix) 
#Since the revenues are arranged from highest to lowest, simply select the first 10 rows and columns 
selection = matrix[:10,:10] 
#Initialize the x,y-axes by reversed their order 
x_axis = selection[:,1] 
print(x_axis) 
reversed_x = x_axis[::-1] 
print(reversed_x) 
y_axis = selection[:,0] 
print(y_axis)
reversed_y = y_axis[::-1] 
#To plot a horizontal bar chart (due to the presence of many labels) ax.barh(reversed_y ,reversed_x, alpha = 0.75) 
#Setting labels for the axes 
ax.set_title("Largest Companies in the USA Based on Annual Revenue (USD)") ax.set_xlabel('Revenue (USD)') 
ax.set_ylabel('Companies') 
#Resetting the starting point of the subplot to the origin(0,0) ax.set_xlim(0,max(reversed_y)) 
#Setting the parameters for the plot 
plt.tight_layout() 
plt.grid(False) 
plt.show() 



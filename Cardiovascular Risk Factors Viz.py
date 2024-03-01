#Import the necessary modules for the visualization 
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
plt.style.use('seaborn-v0_8-pastel') 
#Load the file in the program 
dataset = pd.read_csv(r'C:\Users\Minnie\Desktop\GBD DATA.csv') 
#Check for duplicates and NaN values 
#print(dataset.isnull()) 
#print(dataset.duplicated()) 
#Since there are no duplicates or NaN values in the dataset, we can proceed to selecting reqd. columns 
dataset_column = dataset[['val']] 
category_column = dataset[['rei_name']] 
selected_rows1 = category_column.iloc[0:8, :] 
selected_rows1_tuple = tuple(selected_rows1.to_numpy().flatten()) print(selected_rows1_tuple) 
selected_rows2 = dataset_column.iloc[0:8, :] 
selected_rows2_tuple = tuple(selected_rows2.to_numpy().flatten()) print(selected_rows2_tuple) 
#Lets us create a dictionary that connects each risk factor to their value. 
#Step 1 : Initialize an empty dictionary 
plotting_dict = {} 
for risk_factor, value in zip(selected_rows1_tuple, selected_rows2_tuple): plotting_dict[risk_factor] = value 
print(plotting_dict) 
#Now that we've selected the necessary rows and columns, lets proceed with our visualization 
#Let us plot a horizontal bar chart 
#First, let us define the x and y axis 
risk_factors_yaxis = list(plotting_dict.keys()) 
values_xaxis = list(plotting_dict.values())
plt.barh( risk_factors_yaxis, values_xaxis, color = '#B76e79') plt.title('Global Age-Standardized Percent of Deaths Attributable to Cardiovascular Risk Factors') 
plt.xlabel('Percent of Deaths Attributable to Risk Factor') plt.ylabel('Cardiovascular Risk Factors') 
#Reset the x-ticks labels to enhance readability 
#plt.xticks(labels = ['10%' , '20%', '30%', '40%', '50%']) #Setting the parameters for the plot 
plt.grid(False) 
plt.tight_layout() 
plt.show()
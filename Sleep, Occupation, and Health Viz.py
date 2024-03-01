import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
df = pd.read_csv("C:\\Users\\Minnie\\Desktop\\sleep_data.csv") 
#Select columns of importance 
df = df[['Sleep Duration','Occupation']] 
print(df) 
#for occupation in occupation_means: 
occupation_means = (df.groupby('Occupation')['Sleep 
Duration'].mean().reset_index()) 
print(occupation_means) 
#Initializing the x and y values 
plt.bar(occupation_means['Occupation'],occupation_means['Sleep Duration'], width = 0.6, color = 'k') 
#Titles 
plt.title('Occupations and Average Sleep Durations') 
plt.xlabel('Occupation') 
plt.ylabel('Avg. Sleep') 
#Setting the xticks 
plt.xticks(rotation = 50) 
plt.grid(False) 
plt.tight_layout 
plt.show() 


#import the necessary libraries for plotting and data cleaning from matplotlib import pyplot as plt 
import pandas as pd 
import numpy as np 
#To select the style for the subplots 
plt.style.use('bmh') 
#Load the dataset from the local directory and assign it to the variable 'df' 
df = pd.read_csv("C:\\Users\\Minnie\\Desktop\\Data set of scatter plot.csv") 
#Detecting outliers. 
#Step 1: Identify the outliers in both creatinine column using Tukey's IQR procedure 
creatinine_column = np.array(df['creatinine']) 
q1 = np.quantile(creatinine_column, 0.25) 
q3 = np.quantile(creatinine_column, 0.75) 
iqr = q3 - q1 
#inner_fence1 = q1 - 1.5 * iqr
outer_fence1 = q3 + 1.5 * iqr 
outlier_mask = (creatinine_column > outer_fence1) 
outliers = creatinine_column[outlier_mask] 
#Create a new one-dimensional matrix that contain the ranked order of the original creatinine list 
creatinine_new_matrix = np.sort(creatinine_column) 
#Define a function that removes all values that are <3 
def outlier_remover(matrix,threshold): 
mask = matrix <= threshold 
return matrix[mask] 
#Utilize the function on the creatinine_new_matrix 
data_creatinine = outlier_remover(creatinine_new_matrix,3) 
#Repeating the procedure for the TFF1 column 
TFF1_Column = np.array(df['TFF1']) 
Q1 = np.quantile(TFF1_Column,0.25) 
Q3 = np.quantile(TFF1_Column, 0.75) 
iqr2 = Q3-Q1 
inner_fence1 = Q1 - 1.5 * iqr2 
outer_fence2 = Q3 + 1.5 * iqr2 
outlier_mask2 = (TFF1_Column > outer_fence2) 
#outliers = TFF1_Column(outlier_mask2) 
outliers2 = TFF1_Column[outlier_mask2] 
#Converting the TFF1 column into a sorted numpy one-dimensional matrix TFF1_new_matrix = np.sort(TFF1_Column) 
#To remove outliers in the TFF1 distribution 
data_TFF1 = outlier_remover(TFF1_new_matrix, 4300) 
#Start by creating a figure with 2 subplots 
#Step 1: Initialize the variable 'fig' 
#Step 2: Create 2 subplots, and assign individual characteristics to each 
fig = plt.figure() 
ax1 = fig.add_subplot(2,3,1) 
ax2 = fig.add_subplot(2,3,2) 
ax3 = fig.add_subplot(2,3,3)
ax4 = fig.add_subplot(2,3,4) 
ax5 = fig.add_subplot(2,3,5) 
ax6 = fig.add_subplot(2,3,6) 
#Configuring the fonts for the entire figure 
plt.rc("font", family='monospace', style='normal', variant='normal', size=7, weight = 'bold') 
#Let the first subplot contain a box-and-whiskers plot to detect and visualize outliers 
#Invoke the boxplot() function in the library and apply it to separate subplots 
ax1.boxplot(df['creatinine']) 
ax2.boxplot(df['TFF1']) 
#To create a histogram of the creatinine column to observe the way the data is centered around the mean 
ax3.hist(df['creatinine'], bins = 50, color = 'black', alpha = 0.75) ax3.set_xlabel('Creatinine Levels') 
ax3.set_ylabel('Frequency') 
ax3.set_title('Distribution of Creatinine Levels in the Sample') 
#To create a histogram of the TFF1 column to observe broad distribution trends 
ax4.hist(df['TFF1'], bins = 50, color = 'black', alpha = 0.75) ax4.set_xlabel('TFF1 Levels') 
ax4.set_ylabel('Frequency') 
ax4.set_title('Distribution of TFF1 Levels in the Sample') 
#Set titles for the individual subplots 
ax1.set_title('Detecting Outliers (Creatinine Column)') ax2.set_title('Detecting Outliers (TFF1 Column)') 
#Plotting the outlier-less distribution for both creatinine and TFF1 ax5.hist(data_creatinine, bins = 50, color = 'black', alpha = 0.75) ax5.set_xlabel('Creatinine Levels') 
ax5.set_ylabel('Frequency') 
ax5.set_title('The Creatinine Distribution Without Outliers') ax6.hist(data_TFF1, bins = 50, color = 'black',alpha = 0.75)
ax6.set_xlabel('TFF1 Levels') 
ax6.set_ylabel('Frequency') 
#ax6.set_title('The TFF1 Distribution Without Outliers') 
#Creating a new figure object 
fig2 = plt.figure() 
ax7 = fig2.add_subplot(1,1,1) 
#Creating a scatter plot to measure the correlation between creatinine levels and TFF1 levels 
ax7.scatter(data_creatinine, data_TFF1, cmap = 'gist_heat', alpha = 0.75) 
#Labelling the scatterplot 
ax7.set_title('Relationship Between Creatinine and TFF1 ') ax7.set_xlabel('Creatinine Levels') 
ax7.set_ylabel('TFF1 Levels') 
#Adding additional customization to the subplots 
plt.tight_layout() 
fig2.tight_layout() 
#plt.grid(False) 
#To display the figure 
plt.show() 




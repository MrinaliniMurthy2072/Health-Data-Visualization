import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import xlrd 
plt.style.use('ggplot') 
df = pd.read_excel('cleaned_fertility_data.xlsx') 
df = df.drop(columns = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']) 
row_of_interest1 = df.loc[0] 
row_of_interest2 = df.loc[4] 
row_of_interest3 = df.loc[7] 
matrix1 = np.array(row_of_interest1) 
matrix2 = np.array(row_of_interest2) 
matrix3 = np.array(row_of_interest3) 
x_values = df.columns[:] 
print(x_values) 
y_values1 = matrix1 
y_values2 = matrix2 
y_values3 = matrix3 
plt.plot(x_values,y_values1,label = 'Aruba', color = 'red',linewidth = 1.5 ) 
plt.plot(x_values,y_values2,label='Albania',color = 'blue', linewidth = 1.5) 
plt.plot(x_values,y_values3,label='Armenia',color = 'green', linewidth = 1.5) 
plt.title('Trends in Fertility Rates (1960-2013)') 
plt.xlabel('Years') 
plt.ylabel('Fertility Rates') 
plt.xticks(['1960','1965','1970','1975','1980','1985','1990','1995','2000' ,'2005','2010','2015']) 
plt.xticks(rotation = 45)
plt.grid(True) 
plt.legend() 
plt.show() 

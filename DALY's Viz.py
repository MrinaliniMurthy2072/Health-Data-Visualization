#Import the necessary libraries for the visualizations 
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import seaborn as sns 
import geopandas as gpd 
#Read the desired file through pandas 
dataframe = pd.read_csv(r'C:\Users\Minnie\Desktop\DALYS For Figure 3.csv') 
#Import the GeoJSON file into the geopandas dataframe 
map_dataframe = 
gpd.read_file(r'C:\Users\Minnie\Downloads\custom.geo.json') print(map_dataframe.head())
#Select only the required columns and rows from the original dataframe and assign it into a new pandas dataframe 
revised_dataframe = dataframe.iloc[:, [1,7]] 
revised_dataframe = pd.DataFrame(revised_dataframe) 
#Let us rename the 'location' column in the revised_dataframe in order to enable merging between the GeoJSON file and the Pandas dataframe revised_dataframe = revised_dataframe.rename(columns = {'location' : 'sovereignt'}) 
print(revised_dataframe) 
#Let's merge the two dataframes containing the values and containing the map together 
merged_dataframe = map_dataframe.merge(revised_dataframe, on = 'sovereignt' ) 
#Start creating the chloropleth maps to map the DALY's accross the globe merged_dataframe.plot(column = 'val', 
cmap = 'viridis', 
figsize = (16,7), 
legend = True 
) 
#To enhance readability of the plot, let us superimpose the values from the revised dataset onto the chloropleth map 
#centroids = merged_dataframe.centroid 
#for idx, row in merged_dataframe.iterrows(): 
#value = row['val'] 
# x,y = centroids.iloc[idx].coords.xy 
#plt.annotate((f"{value: .2f}"), (x,y), ha = "center", va = "center", fontsize = 8) 
#Set the parameters for the plot 
plt.title("The Global Distribution of Cardiovascular Disease Burden in 2019 (DALY'S per 100,000)") 
plt.axis("off") 
plt.show()

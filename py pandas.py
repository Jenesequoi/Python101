import pandas as pd
import matplotlib.pyplot as plt #plot out the weather

#import file from working directory
df= pd.read_csv("seattle-weather.csv")

#df.info()  #returns the information of the dataframe including number of rows, columns, memory usage, and dtype

df[10:20] #returns columns 10-19 of the dataset using slicing

#Create a dataframe with select columns

weather= df[['date', 'weather']]

#count weather types
weather_types= weather['weather'].nunique()
print(f"There are {weather_types} unique weather types in the dataset")

#.describe() defines the numerical values in a dataset
df.describe()

#sort values by maximum temp
max_temp= df['temp_max'].sort_values(ascending=False)

real_hot= (df['temp_max']> 23).value_counts() #returns the number of days temp_max exceeded 23 as True and False otherwise
print(real_hot)

snowy= df['weather']== 'snowy'
precipitation= df['weather']== 'precipitation'

snowy_precipitation= df[snowy & precipitation] #returns a dataframe with both snowy and precipitation weather
print(snowy_precipitation)







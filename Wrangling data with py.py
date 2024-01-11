#Basic data wrangling with pandas
import pandas as pd

#2. Import dataset
url= "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv"
df= pd.read_csv(url)  #assign url to df

#Display the information of the dataset
print(df.info()) 

#3. Country with most consumption
max_consumption_country= df.groupby('country').sum().sort_values(by= 'consumption', ascending=False)
print(max_consumption_country)

#4. Which food is the biggest contributor to the above country's consumption total
max_consumed_food= df.query("country== 'Finland'").sort_values('consumption').tail(1)
print(max_consumed_food)

#5. What country produces the most kg CO2 per person per year
max_CO2= df.groupby('country').sum().sort_values('co2_emmission').tail(1)
print(max_CO2)

#6. Which food category is the biggest contributor to the above co2 
max_foodco2= df.query("country== 'Argentina'").sort_values('co2_emmission').tail(1)
print(max_foodco2)

#7. Which food category produces the most co2 per person per year (across all countries)
co2_food= df.groupby('food_category').sum().sort_values('co2_emmission', ascending=False)

print(co2_food)

#8. What food is consumed the most across all countries
## what food is consumed the least

food_total_consumption= df.groupby('food_category').sum().sort_values(by='consumption', ascending=False)
print(food_total_consumption)

#9. Make the dataset wide by pivoting on the food category column

wide_data= df.pivot(index='country', columns= 'food_category')

print(wide_data)



                                          ##END##
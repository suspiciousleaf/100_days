# c:/Users/David/Documents/Programming/Python/Code_list/Projects/100_days/day_25/day_25_env/Scripts/Activate.ps1

import pandas as pd
from pprint import pprint

# data = pandas.read_csv("day_25/day_25/weather_data.csv")

# temp_list = data["temp"].tolist()

# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print((monday.temp * (9 / 5)) + 32)

# Import data
data = pd.read_csv("day_25/day_25/Squirrel_Data.csv")

# # Find all unique colours in dataset
# diff_colours = list(data["Primary Fur Color"].unique())[1:]

# # Create dictionary of colour: number of instances
# colour_count_dict = {
#     colour: len(data[data["Primary Fur Color"] == colour]) for colour in diff_colours
# }

# df = pd.DataFrame([colour_count_dict])

# df.to_csv("day_25/day_25/squirrel_count_comprehension.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(grey_squirrels)

red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(red_squirrels)

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels)

print(grey_squirrels_count, black_squirrels_count, red_squirrels_count)

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pd.DataFrame(data_dict)
df.to_csv("day_25/day_25/squirrel_count.csv")

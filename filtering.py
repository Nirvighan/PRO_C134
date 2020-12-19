# IMPOR MODULES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# READ CSV
df = pd.read_csv("stars.csv")

# CREATE DISTANCE LIST
star_distance_list = df["distance"].tolist()
star_distance_list.pop(0)

print(star_distance_list)


# MAKE  A NEW LIST WITH STARS THAT IS LESS THAN 100 LIGHT YEARS AWAY AND THEN CREATE A CSV OF IT
new_data = []
for data in star_distance_list:
    if data > 100:
        df.remove(data)
    new_data.append(df)

new_data.to_csv("output.csv")






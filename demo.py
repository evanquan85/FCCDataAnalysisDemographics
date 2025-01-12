import pandas as pd

df = pd.read_csv('adult.data.csv')
total_people = len(df)
percentage_bachelors = df[df['education'] == "Bachelors"]
count_percentage_bachelors = len(percentage_bachelors)
percent = (count_percentage_bachelors / total_people) * 100
print(percent)
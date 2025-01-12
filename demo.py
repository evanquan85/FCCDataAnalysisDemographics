import pandas as pd

df = pd.read_csv('adult.data.csv')
min_work_hours = df['hours-per-week'].min()
num_min_workers = df[df['hours-per-week'] == min_work_hours]
min_workers = len(num_min_workers)
rich = (df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])
rich_percentage = round((len(rich) / min_workers) * 100, 1)
print(rich_percentage)

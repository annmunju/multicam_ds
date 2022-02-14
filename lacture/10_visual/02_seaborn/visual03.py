import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


car_crashes = sns.load_dataset('car_crashes')
car_crashes.sort_values("total", ascending=False, inplace=True)

plt.figure(figsize=(15, 10))
sns.barplot(data=car_crashes, x='abbrev', y='total', facecolor='w', edgecolor='black')

sns.barplot(data=car_crashes, x='abbrev', y='speeding', color='r', alpha=0.4, label='speeding')
sns.barplot(data=car_crashes, x='abbrev', y='alcohol', color='g', alpha=0.3, label='alcohol')
sns.barplot(data=car_crashes, x='abbrev', y='not_distracted', color='b', alpha=0.2, label='no_previous')

plt.xlim(-1, 51)
plt.show()
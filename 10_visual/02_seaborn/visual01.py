import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

# for i in sns.get_dataset_names():
#     print(i)

car_crashes = sns.load_dataset('car_crashes')
# print(car_crashes)

"""
total : 전체 사고 건수
speeding : 과속 비율
alcohol : 음주 비율
not_distracted : 전방주시 태만
no_previous : 사고 전적 없는 운전자 비율
ins_premium : 자동차 보험료
ins_losses : 운전자 1인당 충돌 사고로 보험사가 입은 손해
abbrev : 미국 주 (약어)
"""

plt.figure(figsize=(15, 10))

sns.barplot(data=car_crashes, x='abbrev', y='total')
plt.show()
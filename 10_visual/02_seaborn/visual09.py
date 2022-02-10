import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


penguins = sns.load_dataset('penguins')

"""
species : 종
island : 서식지
bill_length_mm : 부리 길이
bill_depth_mm : 부리 깊이
flipper_length_mm : 날개 길이
body_mass_g : 체질량
sex : 성별
"""
# regplot = scatter + 추세선(line)
sns.regplot(data=penguins, x='bill_length_mm', y='bill_depth_mm')
plt.show()
#!/usr/bin/env python
# coding: utf-8

# # 데이터 시각화(visualization)

# - 데이터의 변수의 수, 종류, 분석 목적에 따라 시각화 도구가 달라짐

# ![](./img/시각화.png)
# 
# - 출처: https://blog.qlik.com/third-pillar-of-mapping-data-to-visualizations-usage

# <img src='./img/시각화표.png' width=300 align='left'>

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import *


# ### 도수분포표란?
# 
# - 분할된 구간과 데이터의 개수를 표로 정리한 것

# In[2]:


df = pd.read_csv('./data/ch2_scores_em.csv',
                 index_col='student number')
# df의 처음 5행을 표시
df.head()


# In[3]:


# 50명의 영어 점수 array
eng = df['english']

# Series로 변환하여 describe를 표시
eng.describe()


# In[4]:


freq, _ = np.histogram(eng, bins=10, range=(0,100))
freq


# In[5]:


# 0~10, 10~20, ... 이라는 문자열의 리스트를 작성
freq_class = [f'{i}~{i+10}' for i in range(0,100,10)]

# freq_class를 인덱스로 DataFrame을 작성
freq_dist_df = pd.DataFrame({'frequency':freq},
                           index=pd.Index(freq_class, name='class'))
freq_dist_df


# ### 계급값
# 
# - 각 계급을 대표하는 값으로 계급의 중앙값이 이용
# - 60~70의 계급이면 계급값은 65 점

# In[8]:


class_value =[(i+(i+10))//2 for i in range(0,100,10)]
class_value


# ### 상대도수
# 
# - 전체 데이터에 대해서 해당 계급의 데이터가 어느 정도 비율을 차지하고 있는지를 나타냄
# 

# In[9]:


rel_freq = freq/freq.sum()
rel_freq


# ### 누적 상대도수
# - 해당 계급 까지의 상대도수의 합
# - 누적합 : np.cumsum()

# In[10]:


cum_rel_freq = np.cumsum(rel_freq)
cum_rel_freq


# In[12]:


# 도수 분포표 확장
freq_dist_df['class value']=class_value
freq_dist_df['relative freq.']=rel_freq
freq_dist_df['cum. relative freq.']=cum_rel_freq
freq_dist_df


# ### 도수분포표의 최빈값
# 
# - 최대가 되는 계급의 계급값 => 60-70인 계급의 도수가 최대

# ##### 판다스 데이터프레임의 idxmax(), idxmin() 함수
# 
# - pandas.DataFrame.idxmax(axis=0, skipna=True) :
#     - 지정된 축을 따라 최대 값의 인덱스를 포함하는 Series 반환
# - 인수들
#     - axis: 정수 또는 문자열 유형 매개 변수로 사용할 축 지정
#         - row-wise: 0 또는 index, column-wise: 1 또는 columns
#     - skipna: 부울 매개 변수
#         - 널값 제외를 지정
#         - 전체 행 또는 열이 널이면 결과는 NA가 됨
# - 반환 값 : 지정된 축을 따라 최대 값의 인덱스를 포함하는 Series를 반환

# In[13]:


import pandas as pd

dataframe=pd.DataFrame({'Attendance': {0: 60, 1: 100, 2: 80,3: 78,4: 95},
                        'Obtained Marks': {0: 90, 1: 75, 2: 82, 3: 64, 4: 45}})
dataframe


# In[14]:


series = dataframe.idxmax()
series


# In[15]:


series = dataframe.idxmin()
series


# ### 도수 분포표 최빈값
# - 빈도가 높은 계급이 계급값 반환

# In[17]:


freq_dist_df.loc[freq_dist_df['frequency'].idxmax(), 'class value']


# #### 백분위수 및 사분위수 계산

# In[18]:


x = np.arange(1,12,1)
x


# In[21]:


print(np.percentile(x, 10))  # 백분위수
print(np.quantile(x, 0.1))   # 0~1사이의 값으로 입력


# In[22]:


print(np.percentile(x, 25))  # 25%
print(np.quantile(x, 0.25))   # 하사분위수


# ## 히스토그램

# In[25]:


import matplotlib.pyplot as plt


# In[26]:


plt.hist(eng, bins=25, range=(0,100))
plt.show()


# In[27]:


plt.hist(eng, bins=15, range=(0,100))
plt.show()


# In[28]:


plt.hist(eng, bins=20, range=(0,100))
plt.show()


# In[29]:


plt.hist(eng, bins=10, range=(0,100))
plt.show()


# ## 상자그림

# In[30]:


plt.boxplot(eng, labels=['English'])
plt.show()


# In[ ]:





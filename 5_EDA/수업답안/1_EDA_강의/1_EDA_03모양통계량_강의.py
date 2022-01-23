#!/usr/bin/env python
# coding: utf-8

# # 모양 통계량(measure of shape)
# 
# - 분포의 모양
# - 왜도, 첨도

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import *


# ## 왜도(skewness)
# 
# - 데이터의 비대칭도
# - 분포 모양이 대표값(예. 평균)을 중심으로 좌우의 모양이 대칭적인가 아닌가를 측정
# - 데이터가 한쪽 방향으로 얼마나 치우쳐져 있는가를 나타냄 
# - 특징
#     - 왜도가 0에 가까운 값을 가지면 분포의 모양은 좌우 대칭
#     - 왜도가 음수로 나타나면 오른쪽으로 치우친 분포(왼쪽 꼬리분포) 모양 

# <img src='./img/왜도1.png'  align='left'>

# <img src='./img/왜도2.png' width=400 align='left'>

# #### 왜도 계산
# - 분포의 비대칭도
# - 왜도가 0이면 정규분포
# - 왜도의 절대값이 1.5 이상이면 많이 치우쳤다고 봄
# 
# 
# - scipy.stats.skew(a[, axis, bias, nan_policy])

# **예제 데이터 생성**

# In[2]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# 오른쪽으로 꼬리가 긴분포(right skwed, positive)
x1=[1]*30+[2]*20+[3]*20+[4]*15+[5]*15

# 좌우대칭 분포
x2=[1]*15+[2]*20+[3]*30+[4]*20+[5]*15

# 왼쪽으로 꼬리가 긴분포(left skwed, negative)
x3=[1]*15+[2]*15+[3]*20+[4]*20+[5]*30


# In[3]:


x1[:10]


# In[5]:


pd.Series(x1).value_counts(sort=False)


# In[6]:


pd.Series(x1).value_counts(sort=False).plot(kind='bar')


# In[7]:


pd.Series(x2).value_counts(sort=False).plot(kind='bar')


# In[8]:


pd.Series(x3).value_counts(sort=False).plot(kind='bar')


# In[9]:


print("오른쪽으로 꼬리가 긴 분포의 왜도:", skew(x1))
print("좌우대칭 분포 왜도:", skew(x2))
print("왼쪽으로 꼬리가 긴 분포의 왜도:", skew(x3))


# ### 첨도(kurtosis)
# 
# 
# - 데이터의 뽀족한 정도
# - 분포가 대표값을 중심으로 얼마나 모여 있는가를 나타내는 척도
# - 정규분포(첨도=3)를 기준으로 비교
#     - 데이터가 대푯값을 중심으로 상당히 많이 몰려 있다면 분포 가운데 모양이 뾰족한 모양(첨도>3)으로 나타남
#     - 데이터가 대표값을 중심으로 좌우에 퍼져 있다면 가운데 모양은 완만(첨도<3) 
#     
# ![](./img/첨도.png)
# 
# - Fisher's definiton : the kurtosis of the normal distribution is zero

# #### 첨도 계산
# 
# - scipy.stats.kurtosis(a[, axis, fisher, bias, nan_policy])
#     - Fisher's definition을 따름
#     - 정규분포에 가까울수록 0이 나옴
#     - 균일분포에 가까울수록 음수가 나옴 

# In[10]:


# 균일분포(uniform dist.)
x1=[1]*20+[2]*20+[3]*20+[4]*20+[5]*20

# 좌우대칭 분포(정규분포와 유사: 조금 뽀족)
x2=[1]*10+[2]*20+[3]*40+[4]*20+[5]*10

# 뽀족한 분포
x3=[1]*5+[2]*15+[3]*60+[4]*15+[5]*5


# In[11]:


pd.Series(x1).value_counts(sort=False).plot(kind='bar')


# In[12]:


pd.Series(x2).value_counts(sort=False).plot(kind='bar')


# In[13]:


pd.Series(x3).value_counts(sort=False).plot(kind='bar')


# In[14]:


print("전혀 뾰족하지 않을 때 (평평할 때) 첨도:", kurtosis(x1))
print("조금 뾰족할 때 첨도:", kurtosis(x2))
print("매우 뾰족할 때 첨도:", kurtosis(x3)) #뾰족하면 첨도가 높아짐


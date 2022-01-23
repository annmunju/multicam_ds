#!/usr/bin/env python
# coding: utf-8

# # 2차원 데이터의 정리

# ## 두 데이터 사이의 관계를 나타내는 지표

# In[1]:


import numpy as np
import pandas as pd

get_ipython().run_line_magic('precision', '3')
pd.set_option('precision', 3)


# **두 변수 사이의 관계 측도**
# - 수치형 변수간의 관계 : Pearson's correlation
# - 순서형 변수간의 관계 : Kendall's tau, Spearman correlation
# - 범주형 변수간의 관계 : 카이제곱검정- Phi correlation

# ![](./img/상관분석.png)

# **두 변수간의 관계 시각화**
# - 범주형 변수간의 관계 시각화 : 모자익플롯(Mosaic plot)
# - 수치형 변수간의 관계 시각화 : 산점도(scatter plot)

# ![image.png](attachment:image.png)

# ![image-2.png](attachment:image-2.png)

# **예제 데이터**

# In[2]:


df = pd.read_csv('./data/ch2_scores_em.csv',
                 index_col='student number')
df.head()


# In[3]:


import matplotlib.pyplot as plt

plt.scatter(df['english'], df['mathematics'])
plt.xlabel('english score')
plt.ylabel('mathematics score')

plt.axhline(y=df['mathematics'].mean(), color='r',
            linewidth=1,linestyle=':')
plt.axvline(x=df['english'].mean(), color='r',
            linewidth=1,linestyle=':')
plt.show()


# ### 공분산(共分散, covariance)
# 
# - 두 변수 사이의 관계성 척도
# 
# - 예.
#     - 직사각형의 가로길이는 영어 점수의 편차, 세로는 수학 점수의 편차
#     - 공분산은 면적, 음의 면적도 가능(음의 상관)
# 
# 
# <img src='./img/공분산.jpg' width=500 height=300>

# In[5]:


# 각 과목의 편차 및 과목간 공분산

summary_df = df.copy()
summary_df['eng_dev.'] =    summary_df['english'] - summary_df['english'].mean()
summary_df['math_dev.'] =    summary_df['mathematics'] - summary_df['mathematics'].mean()
summary_df['productOfDev.'] =    summary_df['eng_dev.'] * summary_df['math_dev.']
summary_df.head()


# In[7]:


summary_df['productOfDev.'].mean() 
# 각 학생별 영어와 수학의 공분산 평균이 58.49 이므로  영어와 수학은 양의 상관 관계에 있다고 볼 수 있음


# #### numpy의 공분산 함수 : cov(data1,data2, ddof=)
# 
# - 반환값 : 공분산 행렬 
# - 반환 행렬 중 [0,1]과 [1,0] 의 원소가 공분산 값
# \begin{pmatrix}
#   {영어,영어} & {영어,수학} \\
#   {수학,영어} & {수학,수학}
# \end{pmatrix}

# In[8]:


cov_mat= np.cov(df['english'],df['mathematics'], ddof=0) # 모집단의 공분산
cov_mat


# In[9]:


cov_mat[0,1], cov_mat[1,0]


# #### 각 과목의 분산

# In[10]:


cov_mat[0,0] # 영어과목의 분산


# In[11]:


cov_mat[1,1] # 수학과목의 분산


# In[12]:


np.var(df['english'], ddof=0),np.var(df['mathematics'], ddof=0)


# ### 상관계수
# 
# 
# - 공분산의은 단위의 제곱으로 표현되어 직관적으로 이해하기 어려움
#     - 시험 점수간의 공분산 (점수X점수), 키와 점수간의 공분산 (cm X 점수)
# - 단위에 의존하지 않는 상관성을 나타내는 지표    
# - 상관계수는 공분산을 각 데이터의 표준편차로 나누어 단위에 의존하지 않음
# ![](./img/상관계수수식.png)
# 
# 
# - 양의 상관은 1에 가까워지고, 음의 상관은 -1에 가까워지고, 무상관은 0
# 

# In[13]:


# 수식으로 상관계수 계산

np.cov(df['english'], df['mathematics'], ddof=0)[0, 1] /    (np.std(df['english']) * np.std(df['mathematics']))


# #### 상관계수 함수(np.corrcoef(x,y) / df.corr())

# In[14]:


np.corrcoef(df['english'],df['mathematics'])


# **pandas.DataFrame.corr() 함수**

# In[15]:


# pandas.DataFrame.corr() 함수 적용
df.corr()


# - 양의 상관은 1에 가까워지고, 음의 상관은 -1에 가까워지고, 무상관은 0
# - 상관계수가 -1일 때와 1일 때 데이터는 완전히 직선상에 놓임

# <img src='./img/상관계수예시.jpg' width=500 height=500>

# ## 2차원 데이터의 시각화

# ### 산점도

# In[16]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


# 산점도
plt.scatter(df['english'],df['mathematics'] )
plt.xlabel('english')
plt.ylabel('mathematics')
plt.show()


# ### 회귀직선
# 
# ![](회귀직선수식.png)

# In[25]:


# 계수β_0와β_1를 구한다(기울기와 절편)
poly_fit = np.polyfit(df['english'],df['mathematics'], 1)

# β_0+β_1 x를 반환하는 함수를 작성
poly_1d = np.poly1d(poly_fit)

# 직선을 그리기 위한 x좌표
xs = np.linspace(df['english'].min(), df['english'].max())

# xs에 대응하는 y좌표
ys = poly_1d(xs)

plt.xlabel('english')
plt.ylabel('mathematics')
plt.scatter(df['english'],df['mathematics'], label='score')
plt.plot(xs, ys, color='gray',
        label=f'{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x')

# 범례의 표시
plt.legend(loc='upper left')

plt.show()


# ### 히트맵
# 
# - 히스토그램의 2차원 버전으로 색을 이용해 표현하는 그래프
# - 영어 점수 35점부터 80점, 수학 점수 55점부터 95점까지 5점 간격
# 

# In[21]:


c = plt.hist2d(df['english'], df['mathematics'],
          bins=(9,8), range=[(35,80),(55,95)])
c[3]
plt.xlabel('english')
plt.ylabel('mathematics')
plt.xticks(c[1])
plt.yticks(c[2])

plt.colorbar(c[3])
plt.show()


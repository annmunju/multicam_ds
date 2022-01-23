#!/usr/bin/env python
# coding: utf-8

# # 변이통계량(measure of dispersion)
# 
# - 데이터의 퍼짐 정도
# - 범위, 사분위간 범위, 표준편차, 분산, 변동계수

# - 데이터들이 얼마나 흩어져 있는가를 나타내는 것(산포도)
# - 하나의 수치로 데이터가 흩어진 정도를 계산 
# - 대표값과 더불어 데이터를 비교하는 경우에 유용하게 사용 
# - 예. 평균이 같은 A와 B반의 성적 : 두 집단이 동일한 집단?
# 
# ![](./img/성적분포비교.png)
# 
# - 어느 대학에서 같은 과목을 두 교수가 가르친다고 하자. 두 교수 모두 평균 C학점을 학생들에게 준다면 그 과목을 배우려는 학생들은 어떤 교수를 선택해도 마찬가지라고 생각할 것이다.
# - 그러나 한 교수는 대부분의 학생들이 평범하다고 생각하여 C만 주고 다른 교수는 학생들이 반은 우수하고 반은 공부를 안 한다고 생각하여 A를 주거나 D만 준다.
# - 그러므로 이러한 흩어짐의 정보 없이 학생들이 평균 성적 C라는 사실만 가지고 교수를 선택한다면 학점 때문에 어려움에 처할 수도 있게 된다.

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import *


# In[2]:


import numpy as np
# numpy float 출력옵션 변경
# np.set_printoptions(precision=3)
# np.set_printoptions(precision=20, suppress=True)
# pd.options.display.float_format = '{:.2f}'.format
np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.3f}".format(x)})


# In[3]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# ### 범위(range)
# 
# - 데이터의 최대값과 최소값의 차이
# - 데이터가 퍼져 있는 정도를 나타내는 가장 간단한 방법
# - 범위가 클수록 산포가 크다고 말할 수 있지만
# - 중앙값과 마찬가지로 극단적인 값에 영향을 받음
# - 데이터 중 2개의 정보(최대값, 최소값)만을 이용하므로 적절한 척도로 사용하기 어려움
# 
# **범위(R)=최댓값 - 최솟값**

# In[4]:


np.random.seed(123)
data = np.random.normal(100, 20, size=1000)
data[:10]


# In[6]:


np.min(data), np.max(data)


# - numpy의 max(), min()함수 이용하여 범위 계산

# In[7]:


# 범위 = 최대값 - 최소값
np.max(data)-np.min(data)


# - numpy의 ptp(a[, axis, out, keepdims]) 함수 이용하여 범위 계산

# In[8]:


# numpy.ptp() 이용
np.ptp(data)


# ### 중간 범위
# 
# - 최대값과 최소값의 평균

# In[9]:


# 중간 범위 계산
(np.max(data)+np.min(data))/2


# ### 사분위간 범위 (interquartile range: IQR)
# 
# - IQR = Q3-Q1

# In[10]:


# numpy.quantile() 이용하여 IQR 계산
np.quantile(data, 0.75)-np.quantile(data, 0.25)


# In[11]:


# scipy.stats.iqr(x[, axis, rng, scale, nan_policy, …]) 이용
iqr(data)


# ### 사분위수 편차(quartile deviation)
# 
# - 범위(range)의 문제점을 보완한 척도
# - 사분위간 범위의 값을 2로 나눈 값으로 사분위 범위의 평균값 
# 
# ![](./img/사분위수편차.png)

# In[12]:


# numpy.quantile() 이용
(np.quantile(data, 0.75)-np.quantile(data, 0.25))/2


# In[13]:


# scipy.stats.iqr(x[, axis, rng, scale, nan_policy, …]) 이용
iqr(data)/2


# ### 편차(deviation)
# 
# - 자료값과 평균과의 차이
# - xi-mean()

# In[15]:


data-np.mean(data)


# In[16]:


# 편차의 합은 항상 0
(data-np.mean(data)).sum()


# ### 분산(variaince)

# - 산포도의 척도로 가장 널리 사용되는 방법 
# - 평균을 중심으로 데이터가 퍼져 있는 정도의 측도
# 
# 
# - 각 데이터와 평균과의 차이를 제곱하여 합한 값의 평균
#     - 모분산 : n으로 나누어 줌
#     - 표본분산 : n-1 로 나누어 줌    
# 
# ![](./img/분산식.png)

# #### 분산 계산 : var(a, ddof=0) 함수 
# 
# - numpy.var(a[, axis, dtype, out, ddof, keepdims, where])
# - pandas.Series.var(axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs)
# 
# - ddof 인수 :
#     - 기본값은 0 => 모집단 분산
#     - 표본 분산의 경우 1로 설정

# In[17]:


x = [1,2,3,4,5]

# 표본분산
np.var(x, ddof=1)

# 모분산
np.var(x)

# 모분산
np.array(x).var()
pd.Series(x).var(ddof=0)


# ### 표준편차(standard deviation)
# 
# 
# - 계산된 분산의 제곱근으로 계산
# - 평균을 중심으로 일정한 거리에 포함된 데이터의 비율이 얼마인가를 계산
# - 모든 데이터를 고려한 척도
# 
# 
# - 특징
#     - 모든 데이터가 동일한 값을 갖는다면 분산과 표준편차는 0으로 계산
#     - 모든 데이터에 동일한 값을 더해 주거나 빼도 변하지 않음
#     - 모든 데이터에 동일한 값(C)을 곱하면 분산은 $분산×C^2$으로 표준편차는 $표준편차×C$ 만큼 커짐 
#     
# ![](./img/분산표준편차예시.png)

# #### 표준편차 계산 : std(a, ddof=0) 함수 사용
# 
# - 데이터의 단위와 동일하게 만듬
#     - 분산에서 제곱의 영향을 없앤 지표
# - 분산과 표준편차가 크면 클수록 산포가 크다
# 
# 
# - numpy.std(a[, axis, dtype, out, ddof, keepdims, where])
# - pandas.Series.std(axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs)
# 
# - ddof 인수 :
#     - 기본값은 0 => 모집단 분산
#     - 표본 분산의 경우 1로 설정

# In[18]:


x = [1,2,3,4,5]

# 표본표준편차 (S)
np.std(x, ddof=1)

# 모표준편차 (sigma)
np.std(x)
np.array(x).std()
pd.Series(x).std(ddof=0)


# ### 변동계수(CV: Coefficient of Variable)
# 
# - 표본 표준편차를 표본평균으로 나눈 값 또는 그 값에 100을 곱한 값
# - 상대표준편차
# - 서로 다른 평균과 표준편차를 갖는 여러 데이터의 흩어진 정도를 비교할 때 사용
# - 변동계수 값이 크다는 것은 데이터의 흩어진 정도가 상대적으로 크다는 의미
# 
# - 표본 변동계수 $ 𝐶𝑉=\frac{S}{\overline{x}}$,  모변동계수  $𝐶𝑉= \frac{𝜎}{𝜇}$
# 
# ![](./img/변동계수.png)

# #### 변동계수 계산
# - scipy.stats.variation(a, axis=0, nan_policy='propagate', ddof=0, *, keepdims=False)
# - np.std(x, axis=axis, ddof=ddof) / np.mean(x)

# In[19]:


men=[72,74,77,68,66,75]
women=[45,48,52,53,46,50]

print('평균')
np.mean(men)
np.mean(women)
print('표본 표준편차')
np.std(men,ddof=1)
np.std(women,ddof=1)


# In[20]:


# np.std(x, axis=axis, ddof=ddof) / np.mean(x) 이용

print('남자CV:',np.std(men, ddof=1)/np.mean(men))
print('여자CV:',np.std(women, ddof=1)/np.mean(women))


# In[21]:


# scipy.stats.variation() 이용

print('남자CV:',variation(men))
print('여자CV:',variation(women))


# ## 데이터의 정규화
# : scaling(표준화)
# 
# - 각 값들을 상대적인 값으로 변화시키는 기법
# - 예. 국어 평균 95점, 수학 평균 30인 경우
#     - 취득점수 국어 90, 수학 80 이라면 어떤 과목을 더 잘한 것인가?
#     
# 
# 1. standard scaling(Z)
#     - ${ z_i = \frac {x_i - mean(x)} {S} }$
#     - 평균 : 0, 표준편차 : 1 이 됨
# 
# 
# 2. min-max scaling
#     - ${ s_i = \frac {x_i - min(x)} {max(x)-min(x)} }$
#     - 0 ~ 1 사이의 값으로 변환

# #### 표준화 예제

# In[23]:


df = pd.read_csv('./data/ch2_scores_em.csv',
                index_col="student number")
df.head()


# In[24]:


df['english'].describe()


# In[26]:


df['mathematics'].describe()


# In[27]:


df.describe()


# **Z-scaling**

# In[28]:


# Z-scaling - 평균이 0 표준편차가 1이 됨
z1 = (df['english']-df['english'].mean())/df['english'].std()
z2 = (df['mathematics']-df['mathematics'].mean())/df['mathematics'].std()

print(z1.min(), z1.max())
print(z2.min(), z2.max())
# -3 ~ 3 사이의 값으로 분포됨


# In[29]:


z1.mean(), z1.std()


# **min-max scaling**

# In[30]:


# min-max scaling
s1 = (df['english']-df['english'].min())/(df['english'].max()-df['english'].min())
s2 = (df['mathematics']-df['mathematics'].min())/(df['mathematics'].max()-df['mathematics'].min())

print('eng :', s1.min(), s1.max())
print('math:', s2.min(), s2.max())


# ### sklearn.preprocessing.MinMaxScaler를 이용한 스케일링
# - 머신러닝을 위해 쓰는 경우가 대부분
# - df의 각 열에 대해서 스케일링하는데 적합함

# In[31]:


df.head()


# In[33]:


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
S = scaler.fit_transform(df)
pd.DataFrame(S, columns=df.columns, index=df.index).head()


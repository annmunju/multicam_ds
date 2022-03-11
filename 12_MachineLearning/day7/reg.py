# 회귀계수 함수

def Regression(X, y):

    #  모듈 임포트
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
    import numpy as np

    # features & target : X, y

    # train & test dataset split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=156)

    # Linear Regression OLS로 학습/예측/평가 수행 
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    pred = lin_reg.predict(X_test)
    mse = mean_squared_error(y_test, pred)
    r2 = r2_score(y_test, pred)

    # 결과 출력
    print(lin_reg.__class__.__name__)
    print('mse\t:', round(mse, 3), '\t\tRMSE :', round(np.sqrt(mse),3))
    print('r2\t:', round(r2, 3))

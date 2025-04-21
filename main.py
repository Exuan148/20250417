import numpy as np
from sklearn.linear_model import LinearRegression
import time

X = np.array([[1], [2], [3],[10],[21]])
y = np.array([2, 4, 6,33,38])
X2 = np.array([[0.1], [2], [3],[10],[21]])
y2 = np.array([2, 12, 6,30,38])
#线性回归
model = LinearRegression().fit(X, y)
model2 = LinearRegression().fit(X2, y2)

time.sleep(5)
print("模型系数:", model.coef_,model2.coef_)

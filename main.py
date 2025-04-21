import numpy as np
from sklearn.linear_model import LinearRegression
import time

X = np.array([[1], [2], [3],[10],[21]])

y = np.array([2, 4, 6,33,38])
#线性回归
model = LinearRegression().fit(X, y)
time.sleep(5)
print("模型系数:", model.coef_)

import numpy as np
from sklearn.linear_model import LinearRegression
import time
import argparse

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])

model = LinearRegression().fit(X, y)
time.sleep(5)

parser = argparse.ArgumentParser()
parser.add_argument("--arg1")
parser.add_argument("--arg2")
args = parser.parse_args()
print(args.arg1, args.arg2)

print("模型系数:", model.coef_)

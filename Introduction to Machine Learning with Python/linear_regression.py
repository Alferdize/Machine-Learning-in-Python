from sklearn import linear_model
import numpy as np
N, F = list(map(int,input().split()))
observed = []
output = []
for i in range(F):
    d = list(map(float,input().split()))
    output.append(d[-1])
    observed.append(d[:len(d)-1].copy())
T = int(input())
house = []
for i in range(T):
    d = list(map(float,input().split()))
    house.append(d.copy())

np.set_printoptions(precision=2)
regr = linear_model.LinearRegression()
regr.fit(observed, output)

data = regr.predict(house)
for i in data:
    print(i)
"""
Linear_regression.py
"""

from numpy import *
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

diamond_path = './diamond.csv'

diamond_data = pd.read_csv(diamond_path)

# print(diamond_data.columns)
y = diamond_data.price

diamond_features = ['carat','depth']
X = diamond_data[diamond_features]

diamond_model = DecisionTreeRegressor(random_state=1)

diamond_model.fit(X, y)


print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(diamond_model.predict(X.head()))
"""
Linear_regression.py
"""

from numpy import *
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

diamond_path = './diamond.csv'

diamond_data = pd.read_csv(diamond_path)

# print(diamond_data.columns)
y = diamond_data.price

diamond_features = ['carat','depth']
X = diamond_data[diamond_features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

diamond_model = DecisionTreeRegressor()

diamond_model.fit(train_X, train_y)

val_predictions = diamond_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))



























# diamond_model = DecisionTreeRegressor(random_state=1)

# diamond_model.fit(X, y)
# predicted_diamond_prices = diamond_model.predict(X)
# mean = mean_absolute_error(y, predicted_diamond_prices)
# print("Mean :: ",mean)
# print("Making predictions for the following 5 houses:")
# print(X.head())
# print("The predictions are")
# print(diamond_model.predict(X.head()))
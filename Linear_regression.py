"""
Linear_regression.py
"""

from numpy import *
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

diamond_path = './diamond.csv'

diamond_data = pd.read_csv(diamond_path)

# print(diamond_data.columns)
y = diamond_data.price

diamond_features = ['carat','depth']
X = diamond_data[diamond_features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)



forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))

















# def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
#     model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
#     model.fit(train_X, train_y)
#     preds_val = model.predict(val_X)
#     mae = mean_absolute_error(val_y, preds_val)
#     return(mae)



# for max_leaf_nodes in [5, 50, 500, 5000]:
#     my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
#     print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))



































# diamond_model = DecisionTreeRegressor()

# diamond_model.fit(train_X, train_y)

# val_predictions = diamond_model.predict(val_X)
# print(mean_absolute_error(val_y, val_predictions))



























# diamond_model = DecisionTreeRegressor(random_state=1)

# diamond_model.fit(X, y)
# predicted_diamond_prices = diamond_model.predict(X)
# mean = mean_absolute_error(y, predicted_diamond_prices)
# print("Mean :: ",mean)
# print("Making predictions for the following 5 houses:")
# print(X.head())
# print("The predictions are")
# print(diamond_model.predict(X.head()))
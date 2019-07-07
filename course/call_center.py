import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from mlinsights.mlmodel import QuantileLinearRegression


plt.figure(figsize=(20, 8))

call_center_data = pd.read_csv("data/call_center.csv", parse_dates=["timestamp"])
print(call_center_data)
# print(call_center_data.dtypes)

call_center_data.at[17, "calls"] = 500
call_center_data.at[18, "calls"] = 500
call_center_data.at[19, "calls"] = 500

X = np.array(call_center_data.index).reshape(-1, 1)
y = np.array(call_center_data["calls"]).reshape(-1, 1)

plt.plot(X, y)

ols_model = lm.LinearRegression()
ols_model.fit(X, y)

ols_trend = ols_model.predict(X)

print(ols_model.coef_)
print(ols_trend[-1] - ols_trend[0])

plt.plot(X, ols_trend, color="r")

X_lad = np.array(call_center_data.index).reshape(-1, 1)
y_lad = np.array(call_center_data["calls"])

# print(X_lad)

lad_model = QuantileLinearRegression(verbose=True)

lad_model.fit(X_lad, y_lad)

lad_trend = lad_model.predict(X_lad)

print(lad_model.coef_)
print(lad_trend[-1] - lad_trend[0])

plt.plot(X, lad_trend, color="g")

plt.show()

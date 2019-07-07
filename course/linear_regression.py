import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

csv_path = "/home/ievgen/PycharmProjects/ML_course_hillel/course/data/subscribers_from_ads.csv"
subscribers_from_ads = pd.read_csv(csv_path)

# subscribers_from_ads["budget*sub"] = subscribers_from_ads["promotion_budget"] * subscribers_from_ads["subscribers"]
# subscribers_from_ads["budget**2"] = subscribers_from_ads["promotion_budget"] ** 2

# subscribers_sum_df = subscribers_from_ads.sum()
# print(subscribers_sum_df)

linear_model = lm.LinearRegression()

promotion_budget = np.array(subscribers_from_ads["promotion_budget"]).reshape(-1, 1)
number_of_subscribers = np.array(subscribers_from_ads["subscribers"]).reshape(-1, 1)

linear_model.fit(promotion_budget, number_of_subscribers)

print(linear_model.coef_)
print(linear_model.intercept_)

model = linear_model.predict(promotion_budget)

print(subscribers_from_ads)
plt.scatter(subscribers_from_ads['promotion_budget'], subscribers_from_ads['subscribers'])
plt.plot(subscribers_from_ads['promotion_budget'], model)
plt.show()

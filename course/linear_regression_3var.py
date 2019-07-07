import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

csv_path = "/home/ievgen/PycharmProjects/ML_course_hillel/course/data/advertising.csv"
advertising = pd.read_csv(csv_path, index_col=0)

tv_data = np.array(advertising["TV"]).reshape(-1, 1)
radio_data = np.array(advertising["radio"]).reshape(-1, 1)
newspaper_data = np.array(advertising["newspaper"]).reshape(-1, 1)
sales_data = np.array(advertising["sales"]).reshape(-1, 1)


def visualise_single_var(method, sales):
    plt.scatter(method, sales)
    linear_model = lm.LinearRegression()
    linear_model.fit(method, sales)
    model = linear_model.predict(method)

    plt.plot(method, model)
    plt.show()


visualise_single_var(tv_data, sales_data)
visualise_single_var(radio_data, sales_data)
visualise_single_var(newspaper_data, sales_data)

ad_data = np.array(advertising[["TV", "radio", "newspaper"]]).reshape(-1, 3)

ad_data_model = lm.LinearRegression()
ad_data_model.fit(ad_data, sales_data)
print(ad_data_model.coef_)
print(ad_data_model.intercept_)

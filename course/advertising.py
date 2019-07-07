import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import sklearn.model_selection as ms
import sklearn


def visualize_single_variable_regression(x, y):
    x = np.array(x).reshape(-1, 1)
    y = np.array(y).reshape(-1, 1)

    plt.scatter(x, y)

    linear_model = lm.LinearRegression()
    linear_model.fit(x, y)

    model = linear_model.predict(x)

    plt.plot(x, model, color="r")

    plt.show()


def train_linear_model(X, y):
    trained_model = lm.LinearRegression()
    trained_model.fit(X, y)
    return trained_model


def get_MSE_for_linear_model(trained_model, X, y_true):
    y_predicted = trained_model.predict(X)
    MSE = sklearn.metrics.mean_squared_error(y_true, y_predicted)
    return MSE


def model_to_string(model, labels):
    result_string = "{} = ".format(labels[0])
    for z in range(1, len(labels)):
        result_string += "{} * {} + ".format(model.coef_[0][z - 1], labels[z])
    result_string += "{}".format(model.intercept_[0])
    return result_string


advertising_data = pd.read_csv("data/advertising.csv", index_col=0)
print(advertising_data)

values = advertising_data.values
min_max_scaler = sklearn.preprocessing.MinMaxScaler()
values_scaled = min_max_scaler.fit_transform(values)



# visualize_single_variable_regression(advertising_data["TV"], advertising_data["sales"])
# visualize_single_variable_regression(advertising_data["radio"], advertising_data["sales"])
# visualize_single_variable_regression(advertising_data["newspaper"], advertising_data["sales"])

ad_data = np.array(
    advertising_data[["TV", "radio", "newspaper"]]).reshape(-1, 3)
sales_data = np.array(advertising_data[["sales"]]).reshape(-1, 1)

linear_model = train_linear_model(ad_data, sales_data)

# print(model_to_string(linear_model, ["sales", "TV", "radio", "newspaper"]))

MSE = get_MSE_for_linear_model(linear_model, ad_data, sales_data)
# print("MSE = {}".format(MSE))

print("Cross validated models.")

X_train, X_test, y_train, y_test = ms.train_test_split(ad_data, sales_data)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

cv_linear_model = train_linear_model(X_train, y_train)

print(model_to_string(cv_linear_model, ["sales", "TV", "radio", "newspaper"]))

cv_MSE = get_MSE_for_linear_model(cv_linear_model, X_test, y_test)
print("MSE = {}".format(cv_MSE))

print("Removing newspapers.")

X_train_no_newspapers = np.array([np.delete(l, 2) for l in X_train])
X_test_no_newspapers = np.array([np.delete(l, 2) for l in X_test])
# print(X_train_no_newspapers)
# print(X_test_no_newspapers)

linear_model_TV_radio = train_linear_model(X_train_no_newspapers, y_train)

print(model_to_string(linear_model_TV_radio, ["sales", "TV", "radio"]))

MSE_no_newspapers = get_MSE_for_linear_model(linear_model_TV_radio, X_test_no_newspapers, y_test)
print("MSE = {}".format(MSE_no_newspapers))

print("Removing radio.")

X_train_no_radio = np.array([np.delete(l, 1) for l in X_train])
X_test_no_radio = np.array([np.delete(l, 1) for l in X_test])
# print(X_train_no_newspapers)
# print(X_test_no_newspapers)

linear_model_TV_newspaper = train_linear_model(X_train_no_radio, y_train)

print(model_to_string(linear_model_TV_newspaper, ["sales", "TV", "newspaper"]))

MSE_no_radio = get_MSE_for_linear_model(linear_model_TV_newspaper, X_test_no_radio, y_test)
print("MSE = {}".format(MSE_no_radio))

print("Removing TV.")

X_train_no_TV = np.array([np.delete(l, 0) for l in X_train])
X_test_no_TV = np.array([np.delete(l, 0) for l in X_test])
# print(X_train_no_newspapers)
# print(X_test_no_newspapers)

linear_model_TV_radio = train_linear_model(X_train_no_TV, y_train)

print(model_to_string(linear_model_TV_radio, ["sales", "TV", "radio"]))

MSE_no_TV = get_MSE_for_linear_model(linear_model_TV_radio, X_test_no_TV, y_test)
print("MSE = {}".format(MSE_no_TV))

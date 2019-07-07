import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LogisticRegression, LinearRegression

csv_path = "/home/ievgen/PycharmProjects/ML_course_hillel/course/data/linear_vs_logistic.csv"

qualifies_by_single_grade = pd.read_csv(csv_path)
qualifies_by_single_grade.sort_values(by='grade', inplace=True)

print(qualifies_by_single_grade)

qualified_candidates = qualifies_by_single_grade[qualifies_by_single_grade['qualifies'] == 1]
unqualified_candidates = qualifies_by_single_grade[qualifies_by_single_grade['qualifies'] == 0]

plt.scatter(qualified_candidates['grade'], qualified_candidates['qualifies'], color='g')
plt.scatter(unqualified_candidates['grade'], unqualified_candidates['qualifies'], color='r')

X = np.array(qualifies_by_single_grade['grade']).reshape(-1, 1)
y = np.array(qualifies_by_single_grade['qualifies'])

logistic_model = LogisticRegression(solver="lbfgs")
linear_model = LinearRegression()

logistic_model.fit(X, y)
linear_model.fit(X, y)

logistic_modeled_values = logistic_model.predict(X)
linear_modeled_values = linear_model.predict(X)

binary_linear_modeled_values = [1 if i > 0.5 else 0 for i in linear_modeled_values]
# print(binary_linear_modeled_values)

logistic_model_predict_probabilities = logistic_model.predict_proba(X)[:, 1]
linear_model_predict_probabilities = linear_model.predict(X)

qualifies_by_single_grade['logistic_model_probabilities'] = logistic_model_predict_probabilities
qualifies_by_single_grade['linear_model_probabilities'] = linear_model_predict_probabilities

print(qualifies_by_single_grade)

logistic_confusion_metrics = metrics.confusion_matrix(y, logistic_modeled_values)
linear_confusion_metrics = metrics.confusion_matrix(y, binary_linear_modeled_values)
print("logistic_confusion_metrics \n", logistic_confusion_metrics)
print("linear_confusion_metrics \n", linear_confusion_metrics)

print('logistic_Accuracy:', metrics.accuracy_score(y, logistic_modeled_values))
print('linear_Accuracy:', metrics.accuracy_score(y, binary_linear_modeled_values))
print('logistic_Error rate:', 1 - metrics.accuracy_score(y, logistic_modeled_values))
print('linear_Error rate:', 1 - metrics.accuracy_score(y, binary_linear_modeled_values))
print('logistic_Precision:', metrics.precision_score(y, logistic_modeled_values))
print('linear_Precision:', metrics.precision_score(y, binary_linear_modeled_values))
print('logistic_Recall :', metrics.recall_score(y, logistic_modeled_values))
print('linear_Recall :', metrics.recall_score(y, binary_linear_modeled_values))

plt.plot(X, logistic_modeled_values)
plt.plot(X, binary_linear_modeled_values)
plt.plot(X, logistic_model_predict_probabilities)
plt.plot(X, linear_model_predict_probabilities)
plt.show()

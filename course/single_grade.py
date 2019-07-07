import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

csv_path = "/home/ievgen/PycharmProjects/ML_course_hillel/course/data/single_grade.csv"

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
# logistic_model = LogisticRegression()
logistic_model.fit(X, y)
modeled_values = logistic_model.predict(X)

predict_probabilities = logistic_model.predict_proba(X)[:, 1]
qualifies_by_single_grade['probabilities'] = predict_probabilities

confusion_metrics = metrics.confusion_matrix(y, modeled_values)
print(confusion_metrics)

print('Accuracy:', metrics.accuracy_score(y, modeled_values))
print('Error rate:', 1 - metrics.accuracy_score(y, modeled_values))
print('Precision:', metrics.precision_score(y, modeled_values))
print('Recall :', metrics.recall_score(y, modeled_values))

plt.plot(X, modeled_values)
plt.plot(X, predict_probabilities)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics, model_selection
from sklearn.linear_model import LogisticRegression
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

csv_path = "/home/ievgen/PycharmProjects/ML_course_hillel/course/data/double_grade.csv"

qualifies_by_double_grade = pd.read_csv(csv_path)
print(qualifies_by_double_grade)

qualified_candidates = qualifies_by_double_grade[qualifies_by_double_grade['qualifies'] == 1]
unqualified_candidates = qualifies_by_double_grade[qualifies_by_double_grade['qualifies'] == 0]

plt.xlabel('technical_grade')
plt.xlabel('english_grade')

plt.scatter(qualified_candidates['technical_grade'], qualified_candidates['qualifies'], color='g')
plt.scatter(unqualified_candidates['technical_grade'], unqualified_candidates['qualifies'], color='r')


X = np.array(qualifies_by_double_grade[['technical_grade', 'english_grade']]).reshape(-1, 2)
y = np.array(qualifies_by_double_grade['qualifies'])

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True)

ann = MLPClassifier(hidden_layer_sizes=(6, ), max_iter=1000000)
ann.fit(X_train, y_train)

y_predicted = ann.predict(X_test)
y_propabilities = ann.predict_proba(X_test)[:, 1]


# plt.show()

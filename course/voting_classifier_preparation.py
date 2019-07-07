import numpy as np
import pandas as pd
import sklearn.model_selection as ms
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder, StandardScaler


qualifies_by_double_grade = pd.read_csv("data/double_grade_reevaluated.csv")
print(qualifies_by_double_grade)

X = np.array(qualifies_by_double_grade[["technical_grade", "english_grade"]]).reshape(-1, 2)
y = np.array(qualifies_by_double_grade["qualifies"])

standart_scaler = StandardScaler()
X = standart_scaler.fit_transform(X)

k_folds = ms.KFold(n_splits=4, shuffle=True)
confusion_matrix = np.array([[0, 0], [0, 0]])

for train_index, test_index in k_folds.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    classification_model = RandomForestClassifier()
    # classification_model = SVC(kernel="rbf", gamma="scale")
    # classification_model = MLPClassifier(hidden_layer_sizes=(6,), max_iter=1000000)
    classification_model.fit(X_train, y_train)
    y_modeled = classification_model.predict(X_test)

    test_confusion_matrix = metrics.confusion_matrix(y_test, y_modeled)
    print(test_confusion_matrix)

    confusion_matrix += test_confusion_matrix

print("Confusion matrix:")
print(confusion_matrix)

accuracy = (confusion_matrix[0][0] + confusion_matrix[1][1])/sum(confusion_matrix.ravel())
print("Accuracy: {}".format(accuracy))

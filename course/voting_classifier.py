import numpy as np
import pandas as pd
import sklearn.model_selection as ms
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder, StandardScaler


qualifies_by_double_grade = pd.read_csv("/home/ievgen/PycharmProjects/ML_course_hillel/course/data/double_grade_reevaluated.csv")
print(qualifies_by_double_grade)

X = np.array(qualifies_by_double_grade[["technical_grade", "english_grade"]]).reshape(-1, 2)
y = np.array(qualifies_by_double_grade["qualifies"])

standart_scaler = StandardScaler()
X = standart_scaler.fit_transform(X)

k_folds = ms.KFold(n_splits=4, shuffle=True)

models = []

models.append(("SVC", SVC(kernel="rbf", gamma="scale")))
models.append(("ANN", MLPClassifier(hidden_layer_sizes=(6,), max_iter=1000000)))
models.append(("RF", RandomForestClassifier()))

ensemble = VotingClassifier(models, voting="hard")

accuracy_results = ms.cross_val_score(ensemble, X, y, cv=k_folds)

accuracy = accuracy_results.mean()
print("Accuracy: {}".format(accuracy))

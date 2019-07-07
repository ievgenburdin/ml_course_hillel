import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics, svm
from sklearn.linear_model import LogisticRegression, LinearRegression


def plot_model(svm_classifier):
    # plot the decision function
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    # create grid to evaluate model
    plotting_step = 50
    xx = np.linspace(xlim[0], xlim[1], plotting_step)
    yy = np.linspace(ylim[0], ylim[1], plotting_step)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = svm_classifier.decision_function(xy).reshape(XX.shape)
    # plot decision boundary and margins
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])
    # plot support vectors
    ax.scatter(svm_classifier.support_vectors_[:, 0], svm_classifier.support_vectors_[:, 1], s=100,
               linewidth=1, facecolors='none')


csv_path = "/home/ievgen/PycharmProjects/ML_course_hillel/course/data/double_grade_small.csv"

qualifies_by_double_grade = pd.read_csv(csv_path)
# qualifies_by_single_grade.sort_values(by='grade', inplace=True)

qualified_candidates = qualifies_by_double_grade[qualifies_by_double_grade['qualifies'] == 1]
unqualified_candidates = qualifies_by_double_grade[qualifies_by_double_grade['qualifies'] == 0]

plt.xlabel('technical_grade')
plt.xlabel('english_grade')

plt.scatter(qualified_candidates['technical_grade'], qualified_candidates['qualifies'], color='g')
plt.scatter(unqualified_candidates['technical_grade'], unqualified_candidates['qualifies'], color='r')


X = np.array(qualifies_by_double_grade[['technical_grade', 'english_grade']]).reshape(-1, 2)
y = np.array(qualifies_by_double_grade['qualifies'])

#
# swm_classifier = svm.SVC(kernel="linear")
# swm_classifier.fit(X, y)
# plot_model(swm_classifier)


plt.show()

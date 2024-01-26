import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import graphviz

PlayTennis = pd.read_csv("C:\Datasets\Prac4\PlayTennis.csv")
print(PlayTennis)
Le = LabelEncoder()

PlayTennis['Outlook'] = Le.fit_transform(PlayTennis['Outlook'])
PlayTennis['Temperature'] = Le.fit_transform(PlayTennis['Temperature'])
PlayTennis['Humidity'] = Le.fit_transform(PlayTennis['Humidity'])
PlayTennis['Wind'] = Le.fit_transform(PlayTennis['Wind'])
PlayTennis['Play Tennis'] = Le.fit_transform(PlayTennis['Play Tennis'])
print(PlayTennis)

y= PlayTennis['Play Tennis']
X = PlayTennis.drop(['Play Tennis'], axis=1)
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X,y)
print(tree.plot_tree(clf))

dot_data = tree.export_graphviz(clf, out_file= None)
graph = graphviz.Source(dot_data)
print(graph)

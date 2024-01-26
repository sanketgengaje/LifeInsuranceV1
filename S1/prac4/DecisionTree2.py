import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from graphviz import Digraph, Source

# Read the dataset
PlayTennis = pd.read_csv("C:\\Datasets\\Prac4\\PlayTennis.csv")
print(PlayTennis)

# Label encoding
Le = LabelEncoder()
PlayTennis['Outlook'] = Le.fit_transform(PlayTennis['Outlook'])
PlayTennis['Temperature'] = Le.fit_transform(PlayTennis['Temperature'])
PlayTennis['Humidity'] = Le.fit_transform(PlayTennis['Humidity'])
PlayTennis['Wind'] = Le.fit_transform(PlayTennis['Wind'])
PlayTennis['Play Tennis'] = Le.fit_transform(PlayTennis['Play Tennis'])
print(PlayTennis)

# Split into features and target
y = PlayTennis['Play Tennis']
X = PlayTennis.drop(['Play Tennis'], axis=1)

# Train the decision tree classifier
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, y)

# Create a Digraph object
dot = Digraph(comment='Decision Tree')

# Add nodes and edges to the Digraph
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=X.columns,
                                class_names=['No', 'Yes'],
                                filled=True, rounded=True, special_characters=True)

dot.attr(size='10,10')  # Set the size of the graph
dot.node('start', style='invis')  # Add an invisible node as the starting point
dot.node('end', style='invis')  # Add an invisible node as the ending point
dot.edge('start', 'root')  # Connect the invisible starting point to the root of the tree
dot.node('root', label='', shape='plaintext', width='0')  # Add a blank root node to align the tree
dot.edge('root', 'node')  # Connect the blank root node to the actual root of the tree

# Add the tree structure
dot.node('node', label=dot_data, shape='plaintext')

# Connect the invisible ending point to the actual tree
dot.edge('node', 'end')

# Save and render the Digraph
dot_path = r'C:\Program Files\Graphviz\bin\dot.exe'
graph = Source(dot.source, filename='decision_tree', format='png')
graph.render(view=True, cleanup=True)


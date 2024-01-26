from warnings import filterwarnings
filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.svm import SVC, LinearSVC




from skompiler import skompile
from lightgbm import LGBMRegressor
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
df = pd.read_csv("C:\Datasets\Prac1\diabetes.csv")
df.head
print(df.shape)
print(df.describe())
#till here sir told us

x= df.drop("Outcome",axis=1)
y= df["Outcome"]
x_train = x.iloc[:600]
x_test = x.iloc[600:]
y_train = y[:600]
y_test = y[600:]
print("x_train shape:", x_train.shape)
print("x_test shape:",x_test.shape)
print("y_train shape:",y_train.shape)
print("y_test shape:",y_test.shape)
#ended here

support_vector_classifier = SVC(kernel="linear").fit(x_train, y_train)
print(support_vector_classifier)
print(support_vector_classifier.C)

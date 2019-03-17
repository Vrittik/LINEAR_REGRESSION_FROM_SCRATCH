import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean
from ML_library import mlSkies
dataset=pd.read_csv("Salary_Data.csv")
X=dataset.iloc[:,0].values
y=dataset.iloc[:,1].values


X_train,X_test,y_train,y_test = mlSkies.train_test_split(X,y,split_index=0.2)

X_train=np.array(X_train , dtype=np.float64)
X_test=np.array(X_test, dtype=np.float64)
y_train=np.array(y_train , dtype=np.float64)
y_test=np.array(y_test , dtype=np.float64)


m,b=mlSkies.linear_regression(X_train,y_train)

mlSkies.plot_regression_line(X_train,y_train,m,b)


y_pred=mlSkies.linear_regression_predict(7,m,b)

print("The estimated salary for",7,"years of experience is",y_pred,"rupees")

    






















































    

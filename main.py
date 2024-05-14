from gplearn_e.genetic import SymbolicRegressor
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import graphviz

#read the data sheet using read_excel function in pandas library
df = pd.read_excel(r'E:\OneDrive - Aston University\AstonCS\CS3\CS3IP\CS3IPCode\RTEM R1135D1Lx 31-1-2023 normalize.xlsx')

#load data in specific columns
x1 = df.iloc[:, 2]
x2 = df.iloc[:, 3]
x3 = df.iloc[:, 4]

#transfer inputs into a 2d-array with pandas dataframe
data = {'x1': x1, 'x2': x2, 'x3': x3}
X = pd.DataFrame(data)

#load output
Y = df.iloc[:, 1]
print(Y)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
# fit the model
est_gp = SymbolicRegressor(population_size=5000,
                           generations=10, stopping_criteria=0.01,
                           p_crossover=0.7, p_subtree_mutation=0.05,
                           p_hoist_mutation=0.05, p_point_mutation=0.2,
                           max_samples=0.9, verbose=1,
                           parsimony_coefficient=0.03, random_state=0)
est_gp.fit(X_train, y_train)

print(est_gp._program)

print('R2:',est_gp.score(X_test,y_test))

dot_data = est_gp._program.export_graphviz()
graph = graphviz.Source(dot_data)
graph.render('ex1', format='png', view=True)
graph
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier




#this function creates a random forest model and prints train and validation accuracy
def r_forest(X_train, y_train):
    
    rf = RandomForestClassifier(max_depth=5, random_state=42, class_weight = 'balanced')
    
    rf.fit(X_train, y_train)

    print(f'Train Accuracy = {rf.score(X_train, y_train)}')

    #print(f'Validate Accuracy = {rf.score(X_val, y_val)}')
    

#this function creates a decision tree model and prints train and validation accuracy
def d_tree(X_train, y_train):
    
    dt = DecisionTreeClassifier(max_depth=5, random_state=42, class_weight = 'balanced')
    
    dt.fit(X_train, y_train)

    print(f'Train Accuracy = {dt.score(X_train, y_train)}')

    #print(f'Validate Accuracy = {dt.score(X_val, y_val)}')
    

#this function creates a K-Nearest Neighbor model and prints train and validation accuracy    
def knn_m(X_train, y_train):
    
    knn = KNeighborsClassifier(n_neighbors=5)
    
    knn.fit(X_train, y_train)

    print(f'Train Accuracy = {knn.score(X_train, y_train)}')

    #print(f'Validate Accuracy = {knn.score(X_val, y_val)}')
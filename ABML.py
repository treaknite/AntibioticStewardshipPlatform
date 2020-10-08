import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import warnings
from  collections import Counter
from keras.layers import Dense
import json
from keras import Sequential





def training(df):
    df = df.dropna()
    df.isna().any()
    #df = df.drop('id', axis=1)
    pre_y = df['ar']
    pre_X = df.drop('ar',axis = 1)
    dm_X = pd.get_dummies(pre_X)
    dm_y = pre_y.map(dict(Y=1, N=0))
    #smote = SMOTE(ratio='minority')   #for balancing yes/nos
    #X1, y = smote.fit_sample(dm_X, dm_y)
    sc = MinMaxScaler()
    X = sc.fit_transform(dm_X)
    #Counter(y)
    X_train, X_test, dm_y_train, dm_y_test = train_test_split(X, dm_y, test_size=0.3, random_state = 42, shuffle = True)
    classifier = Sequential()
    classifier.add(Dense(units = 400, activation = 'relu', kernel_initializer='random_normal', input_dim=X_test.shape[1]))
    classifier.add(Dense(units = 800, activation = 'relu', kernel_initializer='random_normal'))
    classifier.add(Dense(units = 10, activation = 'relu', kernel_initializer='random_normal'))
    classifier.add(Dense(units = 1, activation = 'sigmoid', kernel_initializer='random_normal'))
    classifier.compile(optimizer='adam',loss = 'binary_crossentropy', metrics = ['accuracy'])
    classifier.fit(X_train,dm_y_train,batch_size=30,epochs=100,verbose=0)
    eval_model = classifier.evaluate(X_train, dm_y_train)
    y_pred = classifier.predict(X_test)
    y_pred = (y_pred>0.5)
    
    import pickle
    from sklearn.externals import joblib
    filename = "abpredictor.pkl"
    joblib.dump(classifier, filename)
    #a lot of yes' hidden in 0.4 and 0.5

if __name__=='__main__':
    df = pd.read_csv('C:\\Users\\pawan\\Desktop\\pharmafuture\\pharmafuture\\data.csv')
    training(df)
    
 
           


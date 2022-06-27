import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

dt = pd.read_csv('ge.csv')
df = dt.apply(np.random.permutation,axis = 1)
dt = pd.get_dummies(dt,drop_first=True)
x = dt.drop('target',1)
y = dt['target']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1,random_state=10) #split the data

classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

#from sklearn.metrics import confusion_matrix
#cm = confusion_matrix(y_test,y_pred)
#print(cm)


def predict_disease(l):
    print(l)
    if l[1].lower() == 'female':
        l[1] = 0
    else:
        l[1] = 1

    a = 0
    if l[2] == 'atypical angina':
        a = 1
    elif l[2] == 'non-anginal pain':
        a = 2
    elif l[2] == 'typical angina':
        a = 0
    else:
        a = 4

    if l[5] == 'lower than 120mg/ml':
        l[5] = 0
    else:
        l[5] = 1

    # n1 = n3 = 0
    n = 0
    if l[6] == 'left ventricular hypertrophy':
        n = 2
    elif l[6] == 'ST-T wave abnormality':
        n = 1
    elif l[6] == 'normal':
        n = 0

    if l[8] == 'no':
        l[8] = 0
    elif l[8] == 'yes':
        l[8] = 1

    u = 0
    if l[10] == 'flat':
        u = 1
    elif l[11] == 'upsloping':
        u = 0
    elif l[11] == 'downsloping':
        u = 2

    c = 0
    if l[12] == 'fixed defect':
        c = 2
    elif l[12] == 'normal':
        c = 1
    elif l[12] == 'reversible defect':
        c = 3

    data = {dt.columns[0]:[l[0]],dt.columns[1]:[l[1]],dt.columns[2]:[a],dt.columns[3]:[l[3]],dt.columns[4]:[l[4]],dt.columns[5]:[l[5]],dt.columns[6]:[l[6]],dt.columns[7]:[l[7]],dt.columns[8]:[l[8]],dt.columns[9]:[l[9]],dt.columns[10]:[l[10]],dt.columns[11]:[l[11]],dt.columns[12]:[c]}

    df = pd.DataFrame(data)
    print(data)
    y_pred = classifier.predict(df)
    return y_pred
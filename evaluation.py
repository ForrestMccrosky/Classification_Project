import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import sklearn.metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression

import os
from env import host, user, password

#############################Model Evaluation Function##############################

# Function for model performs. move to explore.py
def evaluate(X_df, y_df, model):
    '''
    takes in the current X and y datasets and displays a model evaluation report with
    with confusion matrixes, forming predictions, and classification report
    '''

    #prediction
    pred = model.predict(X_df)

    #score = accuracy
    acc = model.score(X_df, y_df)

    #conf Matrix
    conf = confusion_matrix(y_df, pred)
    mat =  pd.DataFrame ((confusion_matrix(y_df, pred )),index = ['actual_not_churned','actual_churned'], columns =['pred_not_churned','pred_churned' ])
    rubric_df = pd.DataFrame([['True Negative', 'False positive'], ['False Negative', 'True Positive']], columns=mat.columns, index=mat.index)
    cf = rubric_df + ': ' + mat.values.astype(str)

    #assign the values
    tp = conf[1,1]
    fp =conf[0,1] 
    fn= conf[1,0]
    tn =conf[0,0]

    #calculate the rate
    tpr = tp/(tp+fn)
    fpr = fp/(fp+tn)
    tnr = tn/(tn+fp)
    fnr = fn/(fn+tp)

    #classification report
    clas_rep =pd.DataFrame(classification_report(y_df, pred, output_dict=True)).T
    clas_rep.rename(index={'0': "not churned", '1': "churned"}, inplace = True)
    print(f'''
    The accuracy for our model is {acc:.4%}

    The True Positive Rate is {tpr:.3%},    The False Positive Rate is {fpr:.3%},
    The True Negative Rate is {tnr:.3%},    The False Negative Rate is {fnr:.3%}

    ________________________________________________________________________________
    ''')
    print('''
    The positive is  'churned'

    Confusion Matrix
    ''')
    display(cf)
    print('''

    ________________________________________________________________________________
    
    Classification Report:
    ''')
    display(clas_rep)
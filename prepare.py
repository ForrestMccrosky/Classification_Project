import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer 

#############################Clean Blank Strings and Convert to Floats##############################

def prep_telco(df):
    """
    This function is designed to clean up the blank characters in the total charges column and set them
    to 0. Also set the entire column to the float data type that way it can be used for statistical testing.
    """
    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)



#############################Train Validate Test Split Function####################################

def test_train_split(df):
    '''
    This function take in the telco_churn data data acquired by aquire.py, get_db_data(),
    performs a split, stratifies by churn.
    Returns train, validate, and test dfs.
    '''
     train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=713,
                                        stratify = df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=713,
                                   stratify= train.churn)
    return train, validate, test
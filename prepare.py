import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import LabelEncoder


#############################Clean Blank Strings and Convert to Floats##############################

def prep_telco(df):
    """
    This function is designed to clean up the blank characters in the total charges column and set them
    to 0. Also set the entire column to the float data type that way it can be used for statistical testing.
    """
    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    return df



#############################Train Validate Test Split Function####################################

def split_data(df):
    '''
    This function takes in the telco_df dataframe and splits it into a train, validate, and
    test dataframe for exploratoy analysis and modeling purposes
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123,
                                        stratify = df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123,
                                   stratify= train_validate.churn)
    return train, validate, test


####################################Converting to Machine Format##################################
            

    
def convert_cats(df):
    '''
    This function takes the categorical variables of the Telco_churn dataframe
    and converts them into numbers for statistical testing and model building
    '''
    cols3 = [col for col in list(df.columns) if df[col].dtype == 'object']
    label_encoder = LabelEncoder()
    for col in cols3:
        df[col] = label_encoder.fit_transform(df[col])
    return df

####################################Graph Distributions##################################


def graph_distributions(df):
    '''
    This function graphs the distributions of the categorical variables I want to look at
    '''
    
    cols = ['gender', 'senior_citizen', 'partner',
           'dependents', 'phone_service', 'multiple_lines',
           'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']
    
    for col in df[cols]:
        plt.hist(df[col])
        plt.title(f'Distribution of {col}')
        plt.ylabel('Number of Customers')
        plt.xlabel(f'{col}: values')
        plt.show()
        

       
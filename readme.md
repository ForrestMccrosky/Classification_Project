# Telco Classification Project: Predicting Churn
<br>

## Project Description
 - Classification Modeling project to predict customer churn in a Teclecommunications database from SQL
 - Project created using the data science pipeline (Acquisition, Preparation, Exploration, Analysis & Statistical Testing, and finally Modeling and Evaluation)
 - Target: Use the initial phases of the data science pipeline to discover drivers of churn and create a model that can predict whether a customer will churn using those derived parameters
<br>

## Target Dictionary

| Target | Description                                                                               | Data Type |
|--------|-------------------------------------------------------------------------------------------|-----------|
| Churn  | Column indicating whether or not a customer will churn originally valued as 'Yes' or 'No' | Object    |


## Default Data Dictionary

| Column Name              | Description                                                                                                                                             | Data Type                        |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| payment_type_id          | Numerical identity of the payment_type column (1, 2, 3, 4)                                                                                              | int64                            |
| internet_service_type_id | Numerical identity of the internet_service column (1, 2, 3)                                                                                             | int64                            |
| contract_type_id         | Numerical identity of the contract_type column (1, 2, 3)                                                                                                | int64                            |
| customer_id              | Alphanumeric code for unique customer identity                                                                                                          | object                           |
| gender                   | Categorical variable determining customer gender (male, female)                                                                                         | object                           |
| senior_citizen           | Categorical variable determining customer's age represented as 0 or 1                                                                                   | int64                            |
| partner                  | Categorical variable determining if a customer has a partner or not                                                                                     | object                           |
| dependants               | Categorical variable determining if a customer has dependants                                                                                           | object                           |
| tenure                   | Numerical value determining how many months a customer has been with the company from their origin                                                      | int64                            |
| phone_service            | Categorical variable of the phone service for each customer (Yes, No)                                                                                   | object                           |
| multiple_lines           | Categorical variable of the customer's number of phone line status (Yes: Multiple, No: 1 line, No phone service)                                        | object                           |
| paperless_billing        | Categorical variable of the customer's payment arrangement for monthly charges (Yes: paperless billing, No: no paperless)                               | object                           |
| monthly_charges          | Numerical value determining the customer's monthly charges for service                                                                                  | float64                          |
| total_charges            | Numerical value determining the customer's total charges since point of origin with the company                                                         | converted to float64 from object |
| contract_type            | Categorical variable determining the type of contract the customer is in (Month-to-Month, Two year, One year)                                           | object                           |
| internet_service_type    | Categorical variable determining the type of internet a customer is using (Fiber optic, DSL, None)                                                      | object                           |
| payment_type             | Categorical variable determining the type of payment arrangement a customer has agreed too (Electronic Check, Mailed Check, Bank transfer, Credit card) | object                           |

## Engineered Column Dictionary

| Column Name    | Description                                                                                               | Data Type |
|----------------|-----------------------------------------------------------------------------------------------------------|-----------|
| month-to-month | categorical variable with a boolean value of 1 if customer is not in a contract or 0 if they are          | int64     |
| fiber          | categorical variable with a boolean value of 1 if a customer has fiber internet and 0 if they do not      | int64     |
| e_check        | categorical variable with a boolean value of 1 if the customer uses electronic checks and 0 if they don't | int64     |
| 2_contract     | categorical variable with a boolean value of 1 if a customer has a 2 year contract and 0 if not           | int64     |


## Ideas and Hypothesis

### Question 1: Is there a relationship between customers with paperless billing and whether or not they churned
 - Null Hypothesis: There is no relationship between paperless billing and whether or not a customer has churned
 - Alternate Hypothesis: There is a relationship between paperless billing customers and whether or not they have churned

### After some chi squared testing we determined there is a significant relationship between paperless billing customers and whether or not they have churned

### Question 2: Is there a relationship between if a customer has multiple lines and whether or not they have churned
 - Null Hypothesis: There is no relationship between customers having multiple lines and whether or not they have churned
 - Alternate Hypothesis: There is a relationship between customers having multiple lines and whether or not they have churned

### After some chi squared testing we can determine there is a significant relationship between customers who have multiple lines and whether or not they have churned.

## Models
 - After lots of feature and parameter tweaking in conclusion the Decision Tree model performed the best and was used on the test dataframe.
    - Accuracy was 76.72% compared to the basline of 73.47%
    - Precision was a solid 82.5%
    - The best recall achieved was 60.8%
 - With more time I think more feature engineering could be used to better optimize for recall to improve the True Positive rate.

## Reccomendations
 - Use the prediction model to uncover 6 out of every 10 customers who will churn and target them with greater incentives or promotions.
 - Given the models good precision and decent recall prediction we can use it to save an estimated 60% of the churn customers.

## Project Reproduction
 - You will need your own env.py file with your Codeup database credentials to use the sql_connect function

 - Read the readme file and download the acquire, prepare, and evaluate.py files. Use the functions to recreate the dataframes and seperate the data ad the final_notebook suggest. Follow the comments to complete statistical testing and finally use the visualizations to create your own parameters and build the models.
 - Last but not least choose your best models from the training dataframe to run a validate test. Then choose your best validate scored model to run the model on the test dataframe.
 - Finish with concluding remarks and reccomendations for business use of the model.







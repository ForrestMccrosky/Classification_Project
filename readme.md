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

| Column Name    | Description                                                                                          | Data Type |
|----------------|------------------------------------------------------------------------------------------------------|-----------|
| month-to-month | categorical variable with a boolean value of 1 if customer is not in a contract or 0 if they are     | int64     |
| fiber          | categorical variable with a boolean value of 1 if a customer has fiber internet and 0 if they do not | int64     |


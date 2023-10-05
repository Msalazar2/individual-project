# individual_project
First project using data and model I chose. 

## Description
As a Data Scientist, I undertook a project focused on predictive modeling for loan default using data imported from Coursera. The primary objective was to build a machine learning model that could accurately predict whether a loan applicant would default or not. By doing so, we aimed to help financial institutions make more informed lending decisions and mitigate potential losses. This project involved extensive data preparation, preprocessing, feature engineering, and model evaluation to achieve meaningful insights. As a result I was able to make recommendations to minimize loan defaults.


## Goal
* The purpose of this model is to predict borrowers that default.
* My goal is to find specific features that drive defaults.

## Initial hypotheses

* Null Hypothesis: Features do not drive borrowers to default
* Alternative Hypothesis: Features drive borrowers to default

## Data dictionary

| Column       | Column_type | Data_type| Description                                                                |
|--------------|-------------|----------|----------------------------------------------------------------------------|
|LoanID	       |Identifier   |string    |A unique identifier for each loan.                                          |
|Age	       |Feature      |integer	|Age of the borrower.                                                        |
|Income        |Feature      |integer   |Annual income of the borrower.                                              |
|LoanAmount    |Feature      |integer	|Amount of money being borrowed.                                             |
|CreditScore   |Feature      |integer	|Credit score of the borrower, indicating their creditworthiness.            |
|MonthsEmployed|Feature      |integer	|Number of months the borrower has been employed.                            |
|NumCreditLines|Feature      |integer	|Number of credit lines the borrower has open.                               |
|InterestRate  |Feature      |float	    |Interest rate for the loan.                                                 |
|LoanTerm      |Feature      |integer	|Term length of the loan in months.                                          |
|DTIRatio      |Feature      |float	    |Debt-to-Income ratio, borrower's debt compared to their income.             |
|Education     |Feature      |string	|Highest level of education attained by the borrower.                        |
|EmploymentType|Feature      |string	|Type of employment status of the borrower.                                  |
|MaritalStatus |Feature      |string	|Marital status of the borrower (Single, Married, Divorced).                 |
|HasMortgage   |Feature      |string	|Whether the borrower has a mortgage (Yes or No).                            |
|HasDependents |Feature      |string	|Whether the borrower has dependents (Yes or No).                            |
|LoanPurpose   |Feature      |string	|Purpose of the loan (Home, Auto, Education, Business, Other).               |
|HasCoSigner   |Feature      |string	|Whether the loan has a co-signer (Yes or No).                               |
|Default	   |Target       |integer	|Binary target variable indicating whether the loan defaulted (1) or not (0).|

## Planning:
- Generate questions to ask about the data set based off of what I want my model to predict. Do any features have an impact on defaults?. What features significantly drive defaults?
- Determine the format. Final report should be in .ipynb, Modules should be in .py, Predictions should be in .csv.
- Determine audience and develop speech and presention accordingly. Audience will be lead data scientist.
- Determine significance between features and defaults.
- Develop my null hypothsisis and alternative hypothesis. 
- Determine what model to create
  
## Acquisition:
- Data acquired from Coursera into a csv file

## Preparation
- Renamed columns& lowercased column names
- No missing values
- Dropped LoanID column
- Split data 70%,15%,15%

## Exploration & pre-processing:
- Made visuals and used stats to understand which features had a significance
- Binned data for better visuals

## Modeling:
- Decision tree and random forest models with balanced weight parameters perform worse than the baseline
- Distribution of default binary values heavily concentrated on one value
- Knearest tree is weighing one outcome significantly more than the other

## Delivery:
- Deployed my model and a reproducable report
- Made recommendations

## Key findings, recommendations, and takeaways
- Distribution of defaults significantly concentrated on non defaults (0)
- Interest rates, loan amount, and age seem to drive borrrowers to default on loans
- Target loan amounts lowers than 150k
- Require higher qualifications for younger population 
- Target borrowers with low interest rates

## Instructions or an explanation of how someone else can reproduce project and findings

Enviroment setup: 
- Install Conda, Python, MySql, VS Code or Jupyter Notebook
- Clone this repo 

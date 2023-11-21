import os
import pandas as pd
from sklearn.model_selection import train_test_split
from IPython.display import HTML, display


def train_data():
    
    filename = 'train.csv'
    
    if os.path.isfile(filename):
        
        print('Found Data')
        
        return pd.read_csv(filename)
    
    

def test_data():
    
    filename = 'test.csv'
    
    if os.path.isfile(filename):
        
        return pd.read_csv(filename)
    
#since my data is already split into train and test, I will only split my test subset into val and test.          
def val_test(df, seed = 42):

    val, test = train_test_split(df, train_size = 0.5,
                                       random_state = seed)
    return val, test
    


def wrangle_data():
    
    seed = 42
    
    train = train_data()
    
    test = test_data()
    
    val, test = val_test(test)
    
    
    train = train.rename(columns = {
        'LoanID': 'loan_id', 'LoanAmount': 'loan_amount', 'CreditScore': 'credit_score', 'MonthsEmployed': 'months_employed',
        'NumCreditLines': 'num_credit_lines', 'InterestRate': 'interest_rate', 'LoanTerm': 'loan_term', 'DTIRatio': 'dti_ratio',
        'EmploymentType': 'employment_type', 'MaritalStatus': 'marital_status', 'HasMortgage': 'mortgage', 'HasDependents':
        'dependents', 'LoanPurpose': 'loan_purpose', 'HasCoSigner': 'cosigned', 'Default': 'default'
    })
    
    val = val.rename(columns = {
        'LoanID': 'loan_id', 'LoanAmount': 'loan_amount', 'CreditScore': 'credit_score', 'MonthsEmployed': 'months_employed',
        'NumCreditLines': 'num_credit_lines', 'InterestRate': 'interest_rate', 'LoanTerm': 'loan_term', 'DTIRatio': 'dti_ratio',
        'EmploymentType': 'employment_type', 'MaritalStatus': 'marital_status', 'HasMortgage': 'mortgage', 'HasDependents':
        'dependents', 'LoanPurpose': 'loan_purpose', 'HasCoSigner': 'cosigned'
    })
    
    test = test.rename(columns = {
        'LoanID': 'loan_id', 'LoanAmount': 'loan_amount', 'CreditScore': 'credit_score', 'MonthsEmployed': 'months_employed',
        'NumCreditLines': 'num_credit_lines', 'InterestRate': 'interest_rate', 'LoanTerm': 'loan_term', 'DTIRatio': 'dti_ratio',
        'EmploymentType': 'employment_type', 'MaritalStatus': 'marital_status', 'HasMortgage': 'mortgage', 'HasDependents':
        'dependents', 'LoanPurpose': 'loan_purpose', 'HasCoSigner': 'cosigned'
    })
        
    
    train = train.drop(columns = ['loan_id'])
    
    val = val.drop(columns = ['loan_id'])
    
    test = test.drop(columns = ['loan_id'])
    
    train.columns = train.columns.str.lower()
    
    val.columns = val.columns.str.lower()
    
    test.columns = test.columns.str.lower()
    
    return train, val, test


def summarize(df):
    
    text = 'Shape:'
    bold_text = f'<b>{text}</b>'
    display(HTML(bold_text))
    print(df.shape)
    print('')
    print('_________________________________________________')
    print('')
    
    text = 'Info:'
    bold_text = f'<b>{text}</b>'
    display(HTML(bold_text))
    df.info()
    print('')
    print('_________________________________________________')
    print('')
    
    text = 'Null Values:'
    bold_text = f'<b>{text}</b>'
    display(HTML(bold_text))
    print('')
    print(df.isna().sum())
    print('')
    print('_________________________________________________')
    print('')
    
    for col in df.columns.values:
        text = f'Value Count for {col}:'
        bold_text = f'<b>{text}</b>'
        display(HTML(bold_text))

        print('')
        vc = df[col].value_counts()
        print(vc)
        print('')
        print('_________________________________________________')
        print('')
import os
import pandas as pd
from IPython.display import HTML, display


def train_data():
    
    filename = 'train.csv'
    
    if os.path.isfile(filename):
        
        print('Found Data')
        
        return pd.read_csv(filename)
    

def wrangle_data():
    
    df = train_data()
    
    df = df.rename(columns = {
        'LoanID': 'loan_id', 'LoanAmount': 'loan_amount', 'CreditScore': 'credit_score', 'MonthsEmployed': 'months_employed',
        'NumCreditLines': 'num_credit_lines', 'InterestRate': 'interest_rate', 'LoanTerm': 'loan_term', 'DTIRatio': 'dti_ratio',
        'EmploymentType': 'employment_type', 'MaritalStatus': 'marital_status', 'HasMortgage': 'mortgage', 'HasDependents':
        'dependents', 'LoanPurpose': 'loan_purpose', 'HasCoSigner': 'cosigned'
    })
    
    df = df.drop(columns = ['loan_id'])
    
    df.columns = df.columns.str.lower()
    
    return df


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
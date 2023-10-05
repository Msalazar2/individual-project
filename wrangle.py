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
    
    
    
def train_val_test(df, seed = 42):

    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed)
                                       
    
    val, test = train_test_split(val_test, train_size = 0.5,
                                 random_state = seed)
                                 
    
    return train, val, test
    


def wrangle_data():
    
    seed = 42
    
    df = train_data()
    
    train, val, test = train_val_test(df)
    
    #df3 = test_data()
    
    #df2, df3 = train_test_split(df3, train_size = 0.5,
                                # random_state = seed)
    
    df = df.rename(columns = {
        'LoanID': 'loan_id', 'LoanAmount': 'loan_amount', 'CreditScore': 'credit_score', 'MonthsEmployed': 'months_employed',
        'NumCreditLines': 'num_credit_lines', 'InterestRate': 'interest_rate', 'LoanTerm': 'loan_term', 'DTIRatio': 'dti_ratio',
        'EmploymentType': 'employment_type', 'MaritalStatus': 'marital_status', 'HasMortgage': 'mortgage', 'HasDependents':
        'dependents', 'LoanPurpose': 'loan_purpose', 'HasCoSigner': 'cosigned'
    })
    
    #df2 = df2.rename(columns = {
        #'LoanID': 'loan_id', 'LoanAmount': 'loan_amount', 'CreditScore': 'credit_score', 'MonthsEmployed': 'months_employed',
        #'NumCreditLines': 'num_credit_lines', 'InterestRate': 'interest_rate', 'LoanTerm': 'loan_term', 'DTIRatio': 'dti_ratio',
        #'EmploymentType': 'employment_type', 'MaritalStatus': 'marital_status', 'HasMortgage': 'mortgage', 'HasDependents':
        #'dependents', 'LoanPurpose': 'loan_purpose', 'HasCoSigner': 'cosigned'
    #})
    
    #df3 = df3.rename(columns = {
        #'LoanID': 'loan_id', 'LoanAmount': 'loan_amount', 'CreditScore': 'credit_score', 'MonthsEmployed': 'months_employed',
        #'NumCreditLines': 'num_credit_lines', 'InterestRate': 'interest_rate', 'LoanTerm': 'loan_term', 'DTIRatio': 'dti_ratio',
        #'EmploymentType': 'employment_type', 'MaritalStatus': 'marital_status', 'HasMortgage': 'mortgage', 'HasDependents':
        #'dependents', 'LoanPurpose': 'loan_purpose', 'HasCoSigner': 'cosigned'
    #})
        
    
    df = df.drop(columns = ['loan_id'])
    
    #df2 = df2.drop(columns = ['loan_id'])
    
    #df3 = df3.drop(columns = ['loan_id'])
    
    df.columns = df.columns.str.lower()
    
    #df2.columns = df2.columns.str.lower()
        
    #df3.columns = df3.columns.str.lower()
    
    train, val, test = train_val_test(df)
    
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
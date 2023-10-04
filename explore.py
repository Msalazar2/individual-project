import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def plt_dist(df, feats, loop = False):
    
    if loop:
        
        for col in df.columns:

            plt.hist(df[col], bins = 50)

            plt.xlabel(f'{col.replace("_", " ").title()}')

            plt.ylabel('Count')

            plt.title(f'Distribution of {col.replace("_", " ").title()}')

            plt.show()
            
    else: 
        
        plt.hist(df[feats], bins = 50)

        plt.xlabel(f'{feats.replace("_", " ").title()}')

        plt.ylabel('Count')

        plt.title(f'Distribution of {feats.replace("_", " ").title()}')

        plt.show()
        

        
def bin_data(df):
    

    credit_bins = [300, 400, 500, 600, 700, 800, 850]
    credit_labels = ['300s', '400s', '500s', '600s', '700s', '800s']

    # Create a new column 'credit_Bin' by assigning data points to bins
    df['credit_bin'] = pd.cut(df['credit_score'], bins=credit_bins, labels = credit_labels, right= False)


    age_bins = [18, 26, 30, 36, 40, 46, 50, 56, 60, 66, 70]
    age_labels = ['18-25', '26-29', '30-35', '36-39', '40-45', '46-49', '50-55', '56-59', '60-65', '66-69']

    # Create a new column 'Age_Bin' by assigning data points to bins
    df['age_bin'] = pd.cut(df['age'], bins=age_bins, labels = age_labels, right= False)


    interest_bins = [1, 7, 11, 16, 20, 26]
    interest_labels = ['2-6', '7-10', '11-15', '16-19', '20-25']

    # Create a new column 'Age_Bin' by assigning data points to bins
    df['interest_bin'] = pd.cut(df['interest_rate'], bins = interest_bins, labels = interest_labels, right= False)


    loan_amount_bins = [5000, 50_000, 100_000, 150_000, 200_000, 250_000]
    loan_amount_labels = ['5k-50k', '50k-100k', '100k-150k', '150k-200k', '200k-250k']

    # Create a new column 'Age_Bin' by assigning data points to bins
    df['loan_amount_bin'] = pd.cut(df['loan_amount'], bins = loan_amount_bins, labels = loan_amount_labels, right= True)


    income_bins = [1500, 30_000, 60_000, 90_000, 120_000, 150_000]
    income_labels = ['15k-30k', '30k-60k', '60k-90k', '90k-120k', '120k-150k']

    # Create a new column 'Age_Bin' by assigning data points to bins
    df['income_bin'] = pd.cut(df['income'], bins = income_bins, labels = income_labels, right= True)


    df['years_employed'] = df.months_employed / 12
    df.head()


    year_emp_bins = [0, 3, 5, 7, 9, 10]
    year_emp_labels = ['0-2', '3-4', '5-6', '7-8', '9-10']

    # Create a new column 'Age_Bin' by assigning data points to bins
    df['years_employed_bin'] = pd.cut(df['years_employed'], bins = year_emp_bins, labels = year_emp_labels, right= False)
    
    return df



def plt_1(df):
    
    custom_colors = ["lightgrey",'lightgrey', 'lightgrey', 'lightgrey',"lightseagreen"]  # Replace with your desired colors

    ax = sns.barplot(data = df, x = 'interest_bin', y = 'default', errorbar = None, palette = custom_colors)
    ax = plt.gca()

    for p in ax.patches:
        value = float(round(p.get_height(), 2)) * 100  # Get the height (value) of each bar

        label = f"{int(round(value))}%" 

        if value == 18:  # Customize the label for the highest value
            ax.text(p.get_x() + p.get_width() / 2, p.get_height(), label, ha="center", va="bottom", fontweight="bold")
        else:
            ax.text(p.get_x() + p.get_width() / 2, p.get_height(), label, ha="center", va="bottom")


    sns.despine(bottom = True, left = True)
    plt.tick_params(axis='x', which='both', bottom=False, top=False)
    plt.yticks([])
    plt.ylabel('')
    plt.xlabel('Interest Rates (%)')
    plt.title(' Average Defaults')
    plt.show()
    
    
    
def plt_2(df):
    
    custom_colors = ['lightseagreen', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightgrey',
                     'lightgrey', 'lightgrey']  # Replace with your desired colors

    ax = sns.barplot(data = df, x = 'age_bin', y = 'default', errorbar = None, palette = custom_colors)
    ax = plt.gca()

    for p in ax.patches:
        value = float(round(p.get_height(), 2)) * 100  # Get the height (value) of each bar

        label = f"{int(round(value))}%" 

        if value == 21:  # Customize the label for the highest value
            ax.text(p.get_x() + p.get_width() / 2, p.get_height(), label, ha="center", va="bottom", fontweight="bold")
        else:
            ax.text(p.get_x() + p.get_width() / 2, p.get_height(), label, ha="center", va="bottom")


    sns.despine(bottom = True, left = True)
    plt.tick_params(axis='x', which='both', bottom=False, top=False)
    plt.yticks([])
    plt.ylabel('')
    plt.xlabel('Ages')
    plt.title(' Average Defaults')
    plt.show()
    
    
    
def plt_3(df):

    custom_colors = ['lightgrey', 'lightgrey', 'lightgrey', 'lightgrey', 'lightseagreen']  # Replace with your desired colors

    ax = sns.barplot(data = df, x = 'loan_amount_bin', y = 'default', errorbar = None, palette = custom_colors)
    ax = plt.gca()

    for p in ax.patches:
        value = float(round(p.get_height(), 2)) * 100  # Get the height (value) of each bar

        label = f"{int(round(value))}%" 

        if value == 16:  # Customize the label for the highest value
            ax.text(p.get_x() + p.get_width() / 2, p.get_height(), label, ha="center", va="bottom", fontweight="bold")
        else:
            ax.text(p.get_x() + p.get_width() / 2, p.get_height(), label, ha="center", va="bottom")

    sns.despine(bottom = True, left = True)
    plt.tick_params(axis='x', which='both', bottom=False, top=False)
    plt.yticks([])
    plt.ylabel('')
    plt.xlabel('Loan Amounts')
    plt.title(' Average Defaults')# Question : Does interest rate drive default?
    plt.show()
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler




def get_continuous_feats(df):
    '''
    find all continuous numerical features
    
    return: list of column names (strings)
    '''
    num_cols = []
    
    num_df = df.select_dtypes('number')
    
    for col in num_df:
        
        if num_df[col].nunique() > 20:
            
            num_cols.append(col)
    
    return num_cols



def get_discrete_feats(df):
    '''
    find all continuous numerical features
    
    return: list of column names (strings)
    '''
    cat_cols = []
    
    cat_df = df.select_dtypes('object')
    
    for col in cat_df:
        
        if cat_df[col].nunique() > 0:
            
            cat_cols.append(col)
    
    return cat_cols



def dummies(df):

    cat_cols = get_discrete_feats(df)

    df[cat_cols] = pd.get_dummies(df[cat_cols])
    
    return df



def xy_split(df):
    
    return df.drop(columns= 'default'), df.default



def scale(df):
    
    num_cols = get_continuous_feats(df)
    
    scaler = MinMaxScaler()

    #fit the thing
    scaler.fit(df[num_cols])


    #use the thing
    df[num_cols] = scaler.transform(df[num_cols])
    
    return df
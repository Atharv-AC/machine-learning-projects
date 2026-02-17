from sklearn.model_selection import train_test_split

#==========================================================================================
# preprocessing is the process of splitting the data into training and testing sets.
# The train_test_split function is used to split the data into training and testing sets.
# making data ready for the model to train on it.
#==========================================================================================

# df is comming from the main.py file when the user chooses the option 2 in the menu.
def preprocess(df):
    # input values
    features = df[['math_score', 'writing_score']]  # X

    # output value
    target = df['reading_score']   # y

    # random state is used to ensure that the same 
    # random numbers are generated every time the code is run.
    X_train, X_test, y_train, y_test = train_test_split(
        features,target, test_size=0.2, random_state=10
    ) 

    return X_train, X_test, y_train, y_test


from sklearn.model_selection import train_test_split



def preprocess(df):

    df["pass"] = df["reading_score"] >= 50
    # input values
    features = df[['math_score', 'writing_score']]  # X

    # output value
    target = df["pass"]   # y


    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=10
    )


    return X_train, X_test, y_train, y_test,


def gender(df):
    df["pass"] = df["reading_score"] >= 50

    df["gender"] = df["gender"].map({"male": 0, "female": 1})

    features = df[["math_score","writing_score","gender"]]


    target = df["pass"]   

    # print(df["gender"])

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=10
    )


    return X_train, X_test, y_train, y_test,


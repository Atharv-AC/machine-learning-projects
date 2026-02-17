from sklearn.linear_model import LogisticRegression
import os 
import joblib

def train_model(X_train, y_train):
    LogisticRegression(max_iter=1000)
    # training the model on the training data.
    clf = LogisticRegression()
    # The fit method is used to train the model on the training data.
    
    mod = clf.fit(X_train,y_train)
    return mod



# def save_model(model): 
#     base_path = os.path.dirname(__file__)
#     model_path = os.path.join(base_path, "..", "models", "reading_model.pkl")
#     os.makedirs(os.path.dirname(model_path), exist_ok=True)

#     joblib.dump(model, model_path)

def save_model(model, X_test, y_test, math): 
    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, "..", "models", "reading_model.pkl")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    # joblib.dump(model, model_path)
    
    joblib.dump({
        "model": model,
        "X_test": X_test,
        "y_test": y_test,
        "math_score": math,
    }, model_path)


    # joblib.dump(model, "../models/reading_model.pkl")

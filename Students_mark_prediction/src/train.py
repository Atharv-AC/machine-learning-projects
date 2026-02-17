from sklearn.linear_model import LinearRegression
clf = LinearRegression()
import joblib
import os

# Train_model() because we need to use the model variable in the evaluate function 
# and we need to assign the value to it 
# when the user chooses the option 3 in the menu.

def Train_model(X_train,y_train):
    # training the model on the training data.
    # The fit method is used to train the model on the training data.
    
    mod = clf.fit(X_train,y_train)
    return mod



def save_model(model, X_test, y_test): 

    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, "..", "models", "reading_model.pkl")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    # joblib.dump(model, model_path)
    

    joblib.dump({
        "model": model,
        "X_test": X_test,
        "y_test": y_test
    }, model_path)

    # joblib.dump(model, "../models/reading_model.pkl")

from sklearn.metrics import mean_absolute_error
# from train import clf

# pred is comming from the main.py file when the user chooses the option 4 in the menu.
def evaluate(model, pred, X_test, y_test):
    # pred = clf.predict(X_test)
    # y_test
    print("\n")
    print("=" * 35)
    # mean_absolute_error is a metric that measures the average absolute error 
    # between the predicted values and the actual values.
    mae = mean_absolute_error(y_test, pred)
    print(f"Mean absolute error: {mae:<10.2f}")

    print("-" * 35)


    rsq = model.score(X_test, y_test) 
    # rsq = clf.score(X_test, y_test) 

    # R-squared (R²) is a statistical measure that represents the proportion of the variance 
    # for a dependent variable that's explained by an independent variable or variables in a regression model.
    # R² = 0.9 → 90% of the variance in the reading scores can be explained by the math and writing scores.
    print(f"Varience: {rsq * 100:.2f}% ")
    print("=" * 35, "\n")


    return pred, mae, rsq

def pred_user_input(model):
    
    import pandas as pd

    # Example for your current model:
    # b = reading_score, features = ['math_score', 'writing_score']

    print()
    print("-----Predicition------")
    math = float(input("Enter math score: "))
    write = float(input("Enter write score: "))

    # DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
    user_df = pd.DataFrame([{
    "math_score": math,
    "writing_score": write
    }])


    # The predict() method is used to make predictions using the trained model.
    # but it has the [0] to get the first element.
    # because the predict() method returns an array of predictions.
    preds = model.predict(user_df)[0]
    print()
    print(f"Predicted reading score: {preds:.2f}")
    print("-" * 35, "\n")
     
    return preds
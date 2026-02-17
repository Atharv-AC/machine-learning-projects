from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# pred is comming from the main.py file when the user chooses the option 4 in the menu.
def evaluate(model, pred, X_test, y_test):

    acc_score = accuracy_score(y_test, pred)
    print("=" * 75)
    print()
    print("-" * 35)        
    print(f"Accuracy Score: {acc_score:<10.2f}")
    print("-" * 35, "\n")

    con_score = confusion_matrix(y_test, pred)
    print("-" * 25)        
    print(f"Confusion matrix:\n\n {con_score}")
    print("-" * 25, "\n")

    class_score = classification_report(y_test, pred)
    print("-" * 60)        
    print(f"Classification report:\n {class_score}")
    print("-" * 60, "\n")
    print("=" * 70, "\n")


    return pred



def pred_user_input(model):
    
    import pandas as pd

    print()
    print("-----Pass/Fail------")

    math = float(input("Enter math score: "))
    write = float(input("Enter writing score: "))

    user_df = pd.DataFrame([{
        "math_score": math,
        "writing_score": write
    }])

    # DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
    # user_df = pd.DataFrame([{
    preds = model.predict(user_df)
    result = preds[0]
    print("Result:", "PASS" if result else "FAIL")
    print("-" * 35, "\n")
     
    return preds



def pred_gender_input(model):
    
    import pandas as pd

    print()
    print("-----Pass/Fail------")

    math = float(input("Enter math score: "))
    write = float(input("Enter writing score: "))
    gender_input = input("Enter gender (male/female): ").lower()
    # gen = input("Enter gender: ")

    if gender_input == "male":
        gender = 0
    elif gender_input == "female":
        gender = 1
    else:
        print("Invalid input")
        return


    user_df = pd.DataFrame([{
        "math_score": math,
        "writing_score": write,
        "gender": gender
    }])

    # print(user_df)
    # DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
    # user_df = pd.DataFrame([{
    preds = model.predict(user_df)
    result = preds[0]
    print("Result:", "PASS" if result else "FAIL")
    # print(preds)
    print("-" * 35, "\n")
     
    return preds


from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import os 

base_path  = os.path.dirname(__file__)
mat = os.path.join(base_path, "..", "reports", "confusion_matrix.svg")

def plot_confusion_matrix(y_test, pred):

    cm = confusion_matrix(y_test, pred)

    plt.imshow(cm)
    plt.title("Confusion Matrix")
    plt.colorbar()
    plt.savefig(mat)
    plt.show()
    plt.close()


# Mistakes:

# training and predications where different so this cause error
# they need to be same 

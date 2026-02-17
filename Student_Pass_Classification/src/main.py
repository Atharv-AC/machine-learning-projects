from loader import load_csv
from train import  save_model, joblib, train_model
from preprocess import preprocess, gender
from evaluate import evaluate, pred_user_input, pred_gender_input, plot_confusion_matrix
from charts import pass_fail_chart, score_distribution, scatter_chart, histo, curve
# load_csv()

def main():
    model_load = False
    data_load = False
    uses_gender = False
    saved_model = False

    df = X_train = X_test = y_train = y_test = model = math = pred =None

    while True:
        print("1. Load Data.")
        print("2. Load Saved Model.")
        print("3. Preprocess Data.")
        print("4. Train Model.")
        print("5. Evaluate Data.")
        print("6. Save Trained model.")
        print("7. plot confusion matrix")
        print("8. Predict pass/fail.")
        print("9. Predict pass/fail gender")
        print("10. charts")
        print("11. exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input....\n")
            continue
        
        if choice == 2:
            import os

            base_path = os.path.dirname(__file__)
            model_path = os.path.join(base_path, "..", "models", "reading_model.pkl")

            saved_model = True

            if data_load == True:
                print("-" * 35)
                print("Data is already loaded...")
                print("-" * 35, "\n")
            else:
                model = joblib.load(model_path)
                print("-" * 35)
                print("Model loaded successfully")
                print("-" * 35, "\n")
            continue

        if choice == 1:

            if data_load:
                print("-" * 35)
                print("Data is already loaded....")
                print("-" * 35, "\n")
            else:
                df = load_csv()
                data_load = True
                print("-" * 35)
                print("Data loaded successfully..")
                print("-" * 35, "\n")

        elif not data_load and choice in [3,4,5,6]:
            print("-" * 35)
            print("Please load Data first......")
            print("-" * 35, "\n")
            continue


        elif choice == 3:
            while True:
                print("\n----------Preprocessing------------\n")
                print("1. Without gender")
                print("2. With gender")
                print("3. Exit.\n")

                try:
                    choices = int(input("Enter your choice: "))
                except ValueError:
                    print("-" * 35)
                    print("Invalid input....")
                    print("-" * 35, "\n")
                    continue
                                   
                if choices == 1:
                    uses_gender = False
                    if df is None:
                        print("-" * 35)
                        print("Please load data first....")
                        print("-" * 35, "\n")
                    else:
                        X_train,X_test,y_train,y_test = preprocess(df)
                        print("-" * 35)
                        print("Preprocess without Gender....")
                        print("-" * 35, "\n")
                        break
                
                elif choices == 2:
                    uses_gender = True
                    if df is None:
                        print("-" * 35)
                        print("Please load data first....")
                        print("-" * 35, "\n")
                    else:
                        X_train,X_test,y_train,y_test = gender(df)
                        print("-" * 35)
                        print("Preprocess with Gender....")
                        print("-" * 35, "\n")
                        break


                elif choices == 3:
                    break
            # if df is None:
            #     print("=" * 35)
            #     print("Load data first....\n")
            #     print("=" * 35)
            # else:
            #     # preprocess the data and assign the values to the 
            #     # variables X_train, X_test, y_train, y_test.
            #     # so that we can use these variables in the train and evaluate functions.
            #     X_train,X_test,y_train,y_test = gender(df)
            #     # print(X_train.shape)
            #     print("-" * 35)
            #     print("Data preprocessed successfully....")
            #     print(y_train.head())
            #     print("-" * 35, "\n")

        elif choice == 4:
        #    train_model()
            if X_train is None:
                print("Please preprocess data first.")
            else:
                model = train_model(X_train, y_train)
                print("-" * 35)
                print("Model Trained successful...")
                print("-" * 35, "\n")
                

        elif choice == 5:
            if model is None:
                print("-" * 35)
                print("Please train the model first....")
                print("-" * 35, "\n")
            elif X_test is None:
                print("-" * 35)
                print("Please load and preprocess data for evaluation")
                print("-" * 35, "\n")
            else:
                # because we need to use the pred variable in the ActualPred_chart function 
                # and we need to assign the value to it 
                # when the user chooses the option 4 in the menu.
                pred = model.predict(X_test)
                evaluate(model, pred, X_test, y_test)

        elif choice == 6:
            if model is None:
                print("-" * 35)
                print("Train model first")
                print("-" * 35, "\n")
            else:
                save_model(model, X_test, y_test, math)
                print("-" * 35)
                print("Model saved successfully")
                print("-" * 35, "\n")


        elif choice == 7:
            if pred is None:
                print("Please evaluate data first.")
            else:
                plot_confusion_matrix(y_test, pred)

        elif choice == 8:
            if uses_gender:
                print()
                print("-" * 35)
                print("Wrong option.... Select 9")
                print("You have selected pass/fail with gender")
                print("-" * 35, "\n")
            else:
                if pred is None:
                    print("Please evaluate data first.")
                else:
                    pred_user_input(model)

        elif choice == 9:
            if model is None:
                print("Load or train model first.")
                continue
            else:
                pred_gender_input(model)


        elif choice == 10:
            while True:
                print("\n----------Charts------------")
                print("1. Pass fail distribution chart.")
                print("2. Math score distribution chart.")
                print("3. Scatter chart.")
                print("4. Probability distibution.")
                print("5. ROC Curve chart.")
                print("6. Exit.\n")

                try:
                    choices = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input....")
                    continue
                
                if choices == 1:
                    if df is None:
                        print("Load data first")

                    else:
                        pass_fail_chart(df)

                elif choices == 2:
                    if df is None:
                        print("Load data first")

                    else:
                        score_distribution(df)
                        continue
                        
                
                elif choices == 3:
                    scatter_chart(df)
                
                elif choices == 4:
                    histo(model, X_test)

                elif choices == 5:
                    curve(model, X_test, y_test)

                elif choices == 6:
                    break

        elif choice == 11:
            break

if __name__ == "__main__":
    main()

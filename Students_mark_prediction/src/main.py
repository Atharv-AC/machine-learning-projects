from loader import load_csv
from train import Train_model, save_model, joblib
from preprocess import preprocess
from evaluate import evaluate, pred_user_input
from charts import corelationMathRead, corelationWriteRead, ActualPred_chart, residuals_chart,distribution_chart



def main():
    data_load = False
    model_data = False
    # df = X_train = X_test = y_train = y_test = model = pred =None
    #  because we need to use these variables in the while loop and
    #  we need to initialize them with None to avoid any errors. 
    # We will assign values to these variables when the user chooses 
    # the corresponding options in the menu.
    df = X_train = X_test = y_train = y_test = model = pred =None


    while True:

        print("1. Load Data.")
        print("2. Load Saved Model.")
        print("3. Preprocess Data.")
        print("4. Train Model.")
        print("5. Evaluate Data.")
        print("6. plot Data.")
        print("7. Save Trained model.")
        print("8. Predict Reading Score.")
        print("9. Exit.")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please select 1-9.\n")
            continue

        if choice == 2:
            import os

            base_path = os.path.dirname(__file__)
            model_path = os.path.join(base_path, "..", "models", "reading_model.pkl")

            try:
                model = joblib.load(model_path)
                model_data = True
                print("Model loaded successfully")
                print("-" * 65)
                print("NOTE: With saved model you can only predict score option 8")
                print("-" * 65, "\n")
                continue

            except Exception as e:
                print("Error loading model:", e)
            
           
        
        elif model_data and choice in [3,4,5,6,7]:
            print("These options require training workflow. Only prediction is available.")
            continue

        if choice == 1:
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
            if df is None:
                print("=" * 35)
                print("Load data first....\n")
                print("=" * 35)
            else:
                # preprocess the data and assign the values to the 
                # variables X_train, X_test, y_train, y_test.
                # so that we can use these variables in the train and evaluate functions.
                X_train,X_test,y_train,y_test = preprocess(df)
                # print(X_train.shape)
                print("-" * 35)
                print("Data preprocessed successfully....")
                print("-" * 35, "\n")

       
        elif choice == 4:
            if X_train is None:
                print("-" * 35)
                print("Please preprocess first....")
                print("-" * 35, "\n")
            else:
                # because we need to use the model variable in the evaluate function 
                # and we need to assign the value to it 
                # when the user chooses the option 3 in the menu.
                model = Train_model(X_train, y_train)
                print("-" * 35)
                print("Model trained successfully....")
                print("-" * 35, "\n")

        elif choice == 5:
            if model is None:
                print("-" * 35)
                print("Please train the model first....")
                print("-" * 35, "\n")
            elif X_test is None:
                print("-" * 35)
                print("Preprocess data before evaluation")
                print("-" * 35, "\n")
            else:
                # because we need to use the pred variable in the ActualPred_chart function 
                # and we need to assign the value to it 
                # when the user chooses the option 4 in the menu.
                pred = model.predict(X_test)
                evaluate(model, pred, X_test, y_test)


        elif choice == 6:
            while True:
                print("\n----------Charts------------")
                print("1. Math and read correlation chart.")
                print("2. write and Reading correlation chart.")
                print("3. Actual and prediction chart.")
                print("4. Residuals chart.")
                print("5. Histogram chart.")
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
                        corelationMathRead(df)

                elif choices == 2:
                    if df is None:
                        print("Load data first")

                    else:
                        corelationWriteRead(df)
                        continue
                        
                
                elif choices == 3:
                    if pred is None:
                        print("-" * 35)
                        print("Please evaluate data first....")
                        print("-" * 35, "\n")
                    else:
                        ActualPred_chart(y_test, pred)
                
                elif choices == 4:
                      if pred is None:
                        print("-" * 35)
                        print("Please evaluate data first....")
                        print("-" * 35, "\n")

                      else: 
                          residuals_chart(y_test, pred)

                elif choices == 5:
                      if pred is None:
                        print("-" * 35)
                        print("Please evaluate data first....")
                        print("-" * 35)
                      else:
                          distribution_chart(y_test, pred)

                elif choices == 6:
                    break


        elif choice == 7:
            if model is None:
                print("-" * 35)
                print("Train model first")
                print("-" * 35, "\n")
            else:
                save_model(model, X_test, y_test)
                print("-" * 35)
                print("Model saved successfully")
                print("-" * 35, "\n")





        elif choice == 8:
            if model is None:
                print("-" * 35)
                print("Load or train model first")
                print("-" * 35, "\n")
            else:
                print("-" * 35)
                pred_user_input(model)
                print("-" * 35, "\n")

        
        elif choice == 9:
            break


if __name__ == "__main__":
    main()



# what i learned:
# 1. face lot of bugs and resolved them
# 2. how to save trained model and load them

import pandas as pd
import os 


base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "..", "Data", "StudentsPerformance_cleaned.csv")



# df = pd.read_csv(csv_path)
# print(df.head())


def load_csv():
    df = pd.read_csv(csv_path)
    return df

# print(df.head())



#==============================================================
# loader → preprocess → train → evaluate → charts → main →
#==============================================================
#--------------------------------------
# loader → loads data 
#--------------------------------------
# preprocess → splits data
#--------------------------------------
# train → trains model
#--------------------------------------
# evaluate → metrics
#--------------------------------------
# charts → visualization
#--------------------------------------
# main → pipeline control
#--------------------------------------
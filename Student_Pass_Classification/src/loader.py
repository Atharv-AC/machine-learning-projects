import pandas as pd
import os 

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "..", "Data", "StudentsPerformance_cleaned.csv")

def load_csv():
    df = pd.read_csv(csv_path)
    return df
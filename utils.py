import pandas as pd

def get_females(dataset_path):

    df = pd.read_csv(dataset_path)

    female_passengers = df[df['sex']  == 'male']

    return(female_passengers)
import pandas as pd
import numpy as np

def map_data(df):
    # Helper function for range-based mapping
    def map_ranges(value, ranges, default=-1):
        if value == -1:
            return default
        if value < ranges[0]:
            return 0
        elif value <= ranges[1]:
            return 1
        else:
            return 2

    # Apply the mappings
    df['Age'] = df['Age'].apply(lambda x: 0 if int(x) == -1 else 0 if int(x) < 60 else 1)
    df['Gender'] = df['Gender'].apply(lambda x: 1 if x.lower() == '-1' else 0 if x.lower() == 'male' else 1)
    df['Place of Habitation'] = df['Place of Habitation'].apply(lambda x: 1 if x.lower() == '-1' else 0 if x.lower() == 'urban' else 1)
    df['Annual Income'] = df['Annual Income'].apply(lambda x: 0 if x.lower() == '-1' else 0 if x.lower() == 'bpl' else 1)
    df['Smoking Status'] = df['Smoking Status'].apply(lambda x: 0 if x.lower() == '-1' else 1 if x.lower() == 'smoker' else 0)
    df['Alcohol'] = df['Alcohol'].apply(lambda x: 0 if x.lower() == '-1' else 1 if x.lower() == 'alcoholic' else 0)
    df['Tobacco Chewing Status'] = df['Tobacco Chewing Status'].apply(lambda x: 0 if x.lower() == '-1' else 1 if x.lower() == 'yes' else 0)
    df['Comorbidities'] = df['Comorbidities'].apply(lambda x: 0 if x.lower() == '-1' else 1 if x.lower() == 'yes' else 0)
    df['ECOG PS'] = df['ECOG PS'].apply(lambda x: 0 if int(x) == -1 else 0 if int(x) in [0, 1, 2] else 1)
    df['BMI'] = df['BMI'].apply(lambda x: 0 if x.lower() == '-1' else {'normal': 0, 'underweight': 1, 'overweight/obese': 2}[x.lower()])
    df['Bipedal Edema'] = df['Bipedal Edema'].apply(lambda x: 0 if x.lower() == '-1' else 1 if x.lower() == 'yes' else 0)
    df['Site of Primary Cancer'] = df['Site of Primary Cancer'].apply(lambda x: 2 if x.lower() == '-1' else 0 if x.lower() == 'hematological' else 1)
    df['Stage'] = df['Stage'].apply(lambda x: 2 if x.lower() == '-1' else {'early (stage 1 &2)': 0, 'stage 3': 1, 'stage 4': 2}[x.lower()])
    df['Chemotherapy Protocol'] = df['Chemotherapy Protocol'].apply(lambda x: 1 if x.lower() == '-1' else {'single agent': 0, 'doublet': 1, 'triplet': 2}[x.lower()])
    df['Cycle Number'] = df['Cycle Number'].apply(lambda x: 1 if int(x) == -1 else 0 if int(x) == 1 else 1)
    df['Dosing of Chemotherapy'] = df['Dosing of Chemotherapy'].apply(lambda x: 0 if x.lower() == '-1' else 0 if x.lower() == 'standard' else 1)
    df['Use of Prophylactic Growth Factors'] = df['Use of Prophylactic Growth Factors'].apply(lambda x: 0 if x.lower() == '-1' else 1 if x.lower() == 'yes' else 0)

    # Apply range-based mappings with updated default values
    df['Haemoglobin'] = df['Haemoglobin'].apply(lambda x: map_ranges(int(x), (13, 17), default=0))
    df['WBC'] = df['WBC'].apply(lambda x: map_ranges(int(x), (4000, 11000), default=1))
    df['Absolute Lymphocytes'] = df['Absolute Lymphocytes'].apply(lambda x: map_ranges(int(x), (800, 4400), default=1))
    df['Absolute Neutrophil Count'] = df['Absolute Neutrophil Count'].apply(lambda x: map_ranges(int(x), (1600, 8800), default=1))
    df['Neutrophil to Lymphocyte ratio'] = df['Neutrophil to Lymphocyte ratio'].apply(lambda x: map_ranges(int(x), (2, 2), default=0))
    df['Total Platelet count'] = df['Total Platelet count'].apply(lambda x: map_ranges(int(x), (150000, 450000), default=1))
    df['Serum Albumin'] = df['Serum Albumin'].apply(lambda x: map_ranges(int(x), (3.5, 5.2), default=1))
    df['Serum Creatinine'] = df['Serum Creatinine'].apply(lambda x: map_ranges(int(x), (0.7, 1.3), default=1))
    df['Eosinophils'] = df['Eosinophils'].apply(lambda x: map_ranges(int(x), (1, 6), default=1))
    df['Basophils'] = df['Basophils'].apply(lambda x: 0 if int(x) == -1 else 0 if int(x) in [0, 1, 2] else 1)
    df['Monocytes'] = df['Monocytes'].apply(lambda x: map_ranges(int(x), (2, 10), default=1))

    return df

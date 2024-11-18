import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os.path
from project_pages.dataprocessMode import map_data


# Load the saved model
def load_model(file_path):
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model

def runAndSave(input_df,input_data,savedModel,file_path):
    output_df = map_data(input_df)
    # output_file_path = 'modified_data.xlsx' 
    # output_df.to_excel(output_file_path, index=False)

    result = savedModel.predict(output_df)
    label = result[0]

    if label == 1:
        st.markdown("<p style='font-size: 20px;'><b>Prediction:</b></p><p style='font-size: 25px; color: red;'>Patient may develop severe hematologic toxicity</p>", unsafe_allow_html=True)

    else:
        st.markdown(f"<p style='font-size: 20px;'><b>Prediction:</b></p><p style='font-size: 25px; color:green;'>No severe hematologic toxicity</p>", unsafe_allow_html=True)
        
    input_data['Predicted Hematological Toxicity'] = label    
    if os.path.exists(file_path):
            existing_data = pd.read_excel(file_path)
            updated_data = pd.concat([existing_data, input_data], ignore_index=True)
    else:
        updated_data = pd.DataFrame([input_data])  
    updated_data.to_excel(file_path, index=False)


def runAndSavemod(input_df,input_data,savedModel,patient_id,file_path):
    outputdf = map_data(input_df)
    # output_file_path = 'modified_data.xlsx' 
    # output_df.to_excel(output_file_path, index=False)

    result = savedModel.predict(outputdf)
    label = result[0]

    if label == 1:
        st.markdown("<p style='font-size: 20px;'><b>Prediction:</b></p><p style='font-size: 25px; color: red;'>Patient may develop severe hematologic toxicity</p>", unsafe_allow_html=True)

    else:
        st.markdown(f"<p style='font-size: 20px;'><b>Prediction:</b></p><p style='font-size: 25px; color:green;'>No severe hematologic toxicity</p>", unsafe_allow_html=True)
        
    try:
        prev_df = pd.read_excel(file_path, sheet_name='Sheet1')
        input_data['Predicted Hematological Toxicity'] = label

        file_no = patient_id
        if file_no in prev_df['FILE NO'].values:
            prev_df.loc[prev_df['FILE NO'] == file_no, 'Predicted Hematological Toxicity'] = label
        else:
            prev_df = pd.concat([prev_df, input_data])

        prev_df.to_excel(file_path, sheet_name='Sheet1', index=False)
    except Exception as e:
        st.error(f"An error occurred while saving the result: {e}")

    

    
    
    

    
    




    

import streamlit as st 
from sklearn.ensemble import RandomForestClassifier 
import numpy as np
import pandas as pd
import pickle
import os.path
from dataprocess import map_data


def patient_id(savedModel_hematologic, savedModel_nonhematologic, spreadsheet):
    st.title("Enter Patient FILE NO")
    #st.write("Interface for Doctor")

    patient_id = st.text_input("Patient FILE NO")

    # Prediction button
    col1, col2, col3 = st.columns([4, 1, 1])

    button_style = """
        <style>
        .stButton > button {
            padding: 10px 20px;
            font-size: 20px;
            border-radius: 10px;
            color: white;
            border: 2px solid #FFFFFF;
            cursor: pointer;
        }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    relevant_fields = ['Age', 'Gender', 'Place of Habitation', 'Annual Income', 'Smoking Status', 'Alcohol',
                       'Tobacco Chewing Status', 'Comorbidities', 'ECOG PS', 'BMI', 'Bipedal Edema', 'Site of Primary Cancer',
                       'Stage', 'Chemotherapy Protocol', 'Cycle Number', 'Dosing of Chemotherapy', 'Use of Prophylactic Growth Factors',
                       'Hemoglobin', 'WBC', 'Absolute Lymphocytes', 'Absolute Neutrophil Count', 'Neutrophil to Lymphocyte ratio',
                       'Total Platelet Count', 'Serum Albumin', 'Serum Creatinine', 'Eosinophils', 'Basophils', 'Monocytes']

    with col2:
    
        if st.button("Predict Hematological Toxicity"):
            if patient_id:
                try:
                    # Read the data from book1.csv
                    df = pd.read_excel('data.xlsx',sheet_name='Sheet3')
    
                    # Filter the data for the given patient ID
                    input_data = df[df['FILE NO'] == str(patient_id)][relevant_fields]
    
                    if input_data.empty:
                        st.error(f"No data found for Patient ID {patient_id}")
                    else:
    
                        # input_df = input_data
                        # output_df = map_data(input_df)
    
                        # output_file_path = 'modified_data.xlsx'  # Replace with your desired output file path
                        # output_df.to_excel(output_file_path, index=False)
            
                        result = savedModel_hematologic.predict(input_data)
                        # result = np.array([1])
                        label = result[0]
                        if label == 1:
                            toxicity="Yes"
                        else:
                            toxicity="No"
                        st.text(f'Prediction: {toxicity}')
    
                        input_data['Predicted Hematological Toxicity'] = label
                        
    
                        # # Save to Excel
                        input_data_df = input_data
                        if os.path.exists('patient_data1.xlsx'):
                            existing_data = pd.read_excel('patient_data1.xlsx')
                            updated_data = pd.concat([existing_data, input_data_df], ignore_index=True)
                        else:
                            updated_data = input_data_df
    
                        updated_data.to_excel('patient_data1.xlsx', index=False)
    
                        # Save to Google Sheets
                        # data_to_append = list(inputData[0]) + [label]
                        # data_to_append = inputData[0].tolist() + [str(label)]
                        # sheet = spreadsheet.sheet1
                        # sheet.append_row(data_to_append)
    
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    with col3:
    
        if st.button("Predict Non-hematological Toxicity"):
            if patient_id:
                try:
                    # Read the data from book1.csv
                    df = pd.read_excel('data.xlsx',sheet_name='Sheet3')
    
                    # Filter the data for the given patient ID
                    input_data = df[df['FILE NO'] == str(patient_id)][relevant_fields]
    
                    if input_data.empty:
                        st.error(f"No data found for Patient ID {patient_id}")
                    else:
    
                        # input_df = input_data
                        # output_df = map_data(input_df)
    
                        # output_file_path = 'modified_data.xlsx'  # Replace with your desired output file path
                        # output_df.to_excel(output_file_path, index=False)
            
                        result = savedModel_nonhematologic.predict(input_data)
                        # result = np.array([1])
                        label = result[0]
                        if label == 1:
                            toxicity="Yes"
                        else:
                            toxicity="No"
                        st.text(f'Prediction: {toxicity}')
    
                        input_data['Predicted Non-hematological Toxicity'] = label
                        
    
                        # # Save to Excel
                        input_data_df = input_data
                        if os.path.exists('patient_data1.xlsx'):
                            existing_data = pd.read_excel('patient_data1.xlsx')
                            updated_data = pd.concat([existing_data, input_data_df], ignore_index=True)
                        else:
                            updated_data = input_data_df
    
                        updated_data.to_excel('patient_data1.xlsx', index=False)
    
                        # Save to Google Sheets
                        # data_to_append = list(inputData[0]) + [label]
                        # data_to_append = inputData[0].tolist() + [str(label)]
                        # sheet = spreadsheet.sheet1
                        # sheet.append_row(data_to_append)
    
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    
if __name__ == "__main__":
    patient_id()

import streamlit as st 
import numpy as np
import pandas as pd
import pickle
import os.path
from project_pages.dataprocessMode import map_data
from project_pages.utils import runAndSavemod

def patient_id(savedModel):
    st.title("Enter File Number")
    # st.write("Interface for Doctor")
    # patient_id = st.text_input("FileNo")

    text_input_style = """
    <style>
    div[data-testid="stTextInput"] label {
        font-size: 25px;
    }
    </style>
    """

    # Inject the CSS into the Streamlit app
    st.markdown(text_input_style, unsafe_allow_html=True)
    
    # Create the text input field
    st.markdown(f"<p style='font-size: 22px;'>File No</p>", unsafe_allow_html=True)
    patient_id = st.text_input("FileNo",label_visibility="collapsed")

     # Prediction button
    col_left, col_right, col = st.columns([2.5, 1.5,0.5])

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


    with col_right:
    
        if st.button("Fetch and Predict"):
            if patient_id:
                try:
                    # Read the data from book1.csv
                    file_path = 'C:/Users/hp/OneDrive/Documents/My projects/streamlitApp/data/prevEntry.xlsx'
                    df = pd.read_excel(file_path, sheet_name='Sheet1')
    
                    # Filter the data for the given patient ID
                    input_data = df[df['FILE NO'] == patient_id]
    
                    if input_data.empty:
                        st.error(f"No data found for Patient ID {patient_id}")
                    else:
                        # Select only the specified columns
                        columns_to_keep = ['Age', 'Gender','Place of Habitation','Annual Income',
                                           'Smoking Status','Alcohol',
                                           'Tobacco Chewing Status', 'Comorbidities','ECOG PS',       
                                           'BMI','Bipedal Edema', 'Site of Primary Cancer', 'Stage',
                                           'Chemotherapy Protocol','Cycle Number','Dosing of Chemotherapy',
                                           'Use of Prophylactic Growth Factors', 'Haemoglobin',
                                           'WBC','Absolute Lymphocytes','Absolute Neutrophil Count',
                                           'Neutrophil to Lymphocyte ratio','Total Platelet count',
                                           'Serum Albumin','Serum Creatinine','Eosinophils',
                                           'Basophils','Monocytes']

                        input_data = input_data[columns_to_keep]    
                        input_data = input_data.fillna(str(-1))
                        inputdata = input_data.copy()
                        inputdata = inputdata.astype(str)

                        runAndSavemod(inputdata,input_data,savedModel,patient_id,file_path)
                        
    
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    
if __name__ == "__main__":
    patient_id()
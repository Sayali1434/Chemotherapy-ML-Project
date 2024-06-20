import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import pickle
import os.path
from dataprocess import map_data


def specific_options(savedModel_hematologic=None, savedModel_nonhematologic=None, spreadsheet=None):
    st.title("Enter Patient Information")
    #st.write("Interface for Doctor")

    # Field selection checkboxes
    st.sidebar.header("Select Fields to Enter")
    selected_fields = {
        "Age": st.sidebar.checkbox("Age"),
        "Gender": st.sidebar.checkbox("Gender"),
        "Place of Habitation": st.sidebar.checkbox("Place of Habitation"),
        "Annual Income": st.sidebar.checkbox("Annual Income"),
        "Smoking Status": st.sidebar.checkbox("Smoking Status"),
        "Alcohol": st.sidebar.checkbox("Alcohol"),
        "Tobacco Chewing Status": st.sidebar.checkbox("Tobacco Chewing Status"),
        "Comorbidities": st.sidebar.checkbox("Comorbidities"),
        "ECOG PS": st.sidebar.checkbox("ECOG PS"),
        "BMI": st.sidebar.checkbox("BMI"),
        "Bipedal Edema": st.sidebar.checkbox("Bipedal Edema"),
        "Site of Primary Cancer": st.sidebar.checkbox("Site of Primary Cancer"),
        "Stage": st.sidebar.checkbox("Stage"),
        "Chemotherapy Protocol": st.sidebar.checkbox("Chemotherapy Protocol"),
        "Cycle Number": st.sidebar.checkbox("Cycle Number"),
        "Dosing of Chemotherapy": st.sidebar.checkbox("Dosing of Chemotherapy"),
        "Use of Prophylactic Growth Factors": st.sidebar.checkbox("Use of Prophylactic Growth Factors"),
        "Haemoglobin": st.sidebar.checkbox("Haemoglobin"),
        "WBC": st.sidebar.checkbox("WBC"),
        "Absolute Lymphocytes": st.sidebar.checkbox("Absolute Lymphocytes"),
        "Absolute Neutrophil Count": st.sidebar.checkbox("Absolute Neutrophil Count"),
        "Neutrophil to Lymphocyte ratio": st.sidebar.checkbox("Neutrophil to Lymphocyte ratio"),
        "Total Platelet count": st.sidebar.checkbox("Total Platelet count"),
        "Serum Albumin": st.sidebar.checkbox("Serum Albumin"),
        "Serum Creatinine": st.sidebar.checkbox("Serum Creatinine"),
        "Eosinophils": st.sidebar.checkbox("Eosinophils"),
        "Basophils": st.sidebar.checkbox("Basophils"),
        "Monocytes": st.sidebar.checkbox("Monocytes")
    }

    # Dynamically creating columns based on selected fields
    input_data = {}
    selected_field_names = [field for field, selected in selected_fields.items() if selected]
    num_columns = 3
    columns = st.columns(num_columns)
    for idx, field in enumerate(selected_field_names):
        with columns[idx % num_columns]:
            if field == "Age":
                input_data["Age"] = st.text_input("Age")
            elif field == "Gender":
                input_data["Gender"] = st.selectbox("Gender", ["Male", "Female"])
            elif field == "Place of Habitation":
                input_data["Place of Habitation"] = st.selectbox("Place of Habitation", ["Urban", "Rural"])
            elif field == "Annual Income":
                input_data["Annual Income"] = st.selectbox("Annual Income", ["BPL", "Non-BPL"])
            elif field == "Smoking Status":
                input_data["Smoking Status"] = st.selectbox("Smoking Status", ["Smoker", "Non-smoker"])
            elif field == "Alcohol":
                input_data["Alcohol"] = st.selectbox("Alcohol", ["Alcoholic", "Non-alcoholic"])
            elif field == "Tobacco Chewing Status":
                input_data["Tobacco Chewing Status"] = st.selectbox("Tobacco Chewing Status", ["Yes", "No"])
            elif field == "Comorbidities":
                input_data["Comorbidities"] = st.selectbox("Comorbidities", ["Yes", "No"])
            elif field == "ECOG PS":
                input_data["ECOG PS"] = st.text_input("ECOG PS")
            elif field == "BMI":
                input_data["BMI"] = st.selectbox("BMI", ["Normal", "Underweight", "Overweight/Obese"])
            elif field == "Bipedal Edema":
                input_data["Bipedal Edema"] = st.selectbox("Bipedal Edema", ["Yes", "No"])
            elif field == "Site of Primary Cancer":
                input_data["Site of Primary Cancer"] = st.selectbox("Site of Primary Cancer", ["HAEMATOLOGICAL", "NON HAEMATOLOGICAL"])
            elif field == "Stage":
                input_data["Stage"] = st.selectbox("Stage", ["Early (Stage 1 &2)", "Stage 3", "Stage 4"])
            elif field == "Chemotherapy Protocol":
                input_data["Chemotherapy Protocol"] = st.selectbox("Chemotherapy Protocol", ["Single agent", "Doublet", "Triplet"])
            elif field == "Cycle Number":
                input_data["Cycle Number"] = st.text_input("Cycle Number")
            elif field == "Dosing of Chemotherapy":
                input_data["Dosing of Chemotherapy"] = st.selectbox("Dosing of Chemotherapy", ["Standard", "Compromised"])
            elif field == "Use of Prophylactic Growth Factors":
                input_data["Use of Prophylactic Growth Factors"] = st.selectbox("Use of Prophylactic Growth Factors", ["Yes", "No"])
            elif field == "Haemoglobin":
                input_data["Haemoglobin"] = st.text_input("Haemoglobin")
            elif field == "WBC":
                input_data["WBC"] = st.text_input("WBC")
            elif field == "Absolute Lymphocytes":
                input_data["Absolute Lymphocytes"] = st.text_input("Absolute Lymphocytes")
            elif field == "Absolute Neutrophil Count":
                input_data["Absolute Neutrophil Count"] = st.text_input("Absolute Neutrophil Count")
            elif field == "Neutrophil to Lymphocyte ratio":
                input_data["Neutrophil to Lymphocyte ratio"] = st.text_input("Neutrophil to Lymphocyte ratio")
            elif field == "Total Platelet count":
                input_data["Total Platelet count"] = st.text_input("Total Platelet count")
            elif field == "Serum Albumin":
                input_data["Serum Albumin"] = st.text_input("Serum Albumin")
            elif field == "Serum Creatinine":
                input_data["Serum Creatinine"] = st.text_input("Serum Creatinine")
            elif field == "Eosinophils":
                input_data["Eosinophils"] = st.text_input("Eosinophils")
            elif field == "Basophils":
                input_data["Basophils"] = st.text_input("Basophils")
            elif field == "Monocytes":
                input_data["Monocytes"] = st.text_input("Monocytes")

    # Convert input_data dictionary to list and then to numpy array
    input_data_list = [input_data.get(field, -1) for field in selected_fields.keys()]
    inputData = np.array([input_data_list])

    input_df = pd.DataFrame(inputData,columns = ['Age','Gender','Place of Habitation','Annual Income','Smoking Status','Alcohol','Tobacco Chewing Status','Comorbidities','ECOG PS','BMI','Bipedal Edema','Site of Primary Cancer','Stage','Chemotherapy Protocol','Cycle Number','Dosing of Chemotherapy','Use of Prophylactic Growth Factors','Haemoglobin','WBC','Absolute Lymphocytes','Absolute Neutrophil Count','Neutrophil to Lymphocyte ratio','Total Platelet count','Serum Albumin','Serum Creatinine','Eosinophils','Basophils','Monocytes'])

    # Prediction button
    col1, col2, col3 = st.columns([2,1,1])

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

    with col2:
        if st.button("Predict hematological toxicity"):

            output_df = map_data(input_df)

            output_file_path = 'modified_data.xlsx'  # Replace with your desired output file path
            output_df.to_excel(output_file_path, index=False)


            result = savedModel_hematologic.predict(output_df)
            #result = np.array([1])  # Dummy prediction for illustration
            label = result[0]
            st.text(f'Hematological Toxicity Prediction: {label}')

            input_data['Predicted Hematological Toxicity'] = result[0]

            if os.path.exists('patient_data1.xlsx'):
                existing_data = pd.read_excel('patient_data1.xlsx')
                updated_data = pd.concat([existing_data, pd.DataFrame([input_data])], ignore_index=True)
            else:
                updated_data = pd.DataFrame([input_data])

            updated_data.to_excel('patient_data1.xlsx', index=False)

            # data_to_append = [int(x) for x in inputData[0]] + [int(label)]
            data_to_append = inputData[0].tolist() + [str(label)]


            if spreadsheet:
                sheet = spreadsheet.sheet1
                sheet.append_row(data_to_append)

    with col3:
        if st.button("Predict non-hematological toxicity"):

            output_df = map_data(input_df)

            output_file_path = 'modified_data.xlsx'  # Replace with your desired output file path
            output_df.to_excel(output_file_path, index=False)


            result = savedModel_nonhematologic.predict(output_df)
            #result = np.array([1])  # Dummy prediction for illustration
            label = result[0]
            st.text(f'Non-hematological Toxicity Prediction: {label}')

            input_data['Predicted Non-hematological Toxicity'] = result[0]

            if os.path.exists('patient_data1.xlsx'):
                existing_data = pd.read_excel('patient_data1.xlsx')
                updated_data = pd.concat([existing_data, pd.DataFrame([input_data])], ignore_index=True)
            else:
                updated_data = pd.DataFrame([input_data])

            updated_data.to_excel('patient_data1.xlsx', index=False)

            # data_to_append = [int(x) for x in inputData[0]] + [int(label)]
            data_to_append = inputData[0].tolist() + [str(label)]


            if spreadsheet:
                sheet = spreadsheet.sheet1
                sheet.append_row(data_to_append)


if __name__ == "__main__":
    specific_options()

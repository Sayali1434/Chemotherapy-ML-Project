import streamlit as st
from project_pages.specific_options import specific_options
from project_pages.patient_id import patient_id
from utils import load_model, setup_google_sheets

st.set_page_config(layout="wide")

savedModel_hematologic = load_model('final_hematologicmodel.pkl')
savedModel_nonhematologic = load_model('final_nonhematologicmodel.pkl')

spreadsheet = setup_google_sheets('chemoapifile.json', 'Hematological')

def main():
    st.title("Chemotherapy Toxicity Prediction Model")
    options=["Enter Patient ID","Consider specific variables"] #"Consider all variables"
    selection=st.selectbox("Select Patient Information Input Option: ",options, index=None, placeholder="Select option") 

    # if selection == "Consider all variables":
    #     app2_model(savedModel_hematologic, savedModel_nonhematologic, spreadsheet)

    if selection == "Consider specific variables":
        specific_options(savedModel_hematologic, savedModel_nonhematologic, spreadsheet)
    
    elif selection == "Enter Patient ID":
        patient_id(savedModel_hematologic, savedModel_nonhematologic, spreadsheet)

if __name__ == "__main__":
    main()
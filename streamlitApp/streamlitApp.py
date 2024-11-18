import warnings
warnings.filterwarnings("ignore")
import streamlit as st
from project_pages.specific_options import specific_options
from project_pages.patient_id import patient_id
from project_pages.utils import load_model

st.set_page_config(layout="wide")

savedModel = load_model('singleHematoSevereStacking.pkl')

# Add the logo image
logo_url = "logo.png" 

def main():

    st.image(logo_url, width=450)
    st.title("Predicting Severe Chemotherapy Related Toxicities")

    button_style = """
    <style>
    .stButton button {
        width: 500px;
        height: 45px;
        background-color: #11A2D7;
        color: white;
    }
    </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,0.5,2])

    if 'button1' not in st.session_state:
        st.session_state['button1'] = False
    if 'button2' not in st.session_state:
        st.session_state['button2'] = False

    with col1:
        if st.button("Enter Patient File Number"):
            st.session_state['button1'] = True
            st.session_state['button2'] = False

    with col2:
        st.markdown("<p style='font-size: 22px;'>OR</p>", unsafe_allow_html=True)

    with col3:
        if st.button("Enter Specific Parameters"):
            st.session_state['button1'] = False
            st.session_state['button2'] = True

    if st.session_state['button1']:
        patient_id(savedModel)
    
    if st.session_state['button2']:
        specific_options(savedModel)
  

if __name__ == "__main__":
    main()
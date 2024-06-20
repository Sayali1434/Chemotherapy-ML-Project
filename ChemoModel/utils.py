from sklearn.ensemble import RandomForestClassifier 
import numpy as np
import pandas as pd
import pickle
import os.path
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API setup
def setup_google_sheets(credentials_file, spreadsheet_name):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open(spreadsheet_name)
    return spreadsheet

# Load the saved model
def load_model(file_path):
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model
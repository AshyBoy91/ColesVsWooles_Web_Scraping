from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account


def google_sheet_wr(list, range:str):
    # remove /edit if you get SCOPES from google sheets
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    # Check path of the key.json. Below is the key file variable
    SERVICE_ACCOUNT_FILE = 'keyssheet.json'
    # Declare credentials
    credentials1 = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # Spreadsheet ID
    SAMPLE_SPREADSHEET_ID = 'YOUR Spreadsheet ID'
    # Access the Spreadsheet
    service = build('sheets', 'v4', credentials=credentials1)
    sheet = service.spreadsheets()
    # Make write request. Pass list and range
    request1 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range, valueInputOption="USER_ENTERED", body={"values":list}).execute()
    # print(request1)
    return request1

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_sheet(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("sheets/creds.json", scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name)

def log_to_sheet(sheet, sheet_title, data):
    try:
        worksheet = sheet.worksheet(sheet_title)
    except:
        worksheet = sheet.add_worksheet(title=sheet_title, rows="1000", cols="20")
    worksheet.append_rows(data)
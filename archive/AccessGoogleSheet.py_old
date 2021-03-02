import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from datetime import datetime

def InitGoogleSheetsAuth():
  scope = ['https://spreadsheets.google.com/feeds',\
          'https://www.googleapis.com/auth/drive']

  creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
  client = gspread.authorize(creds)

  sheet = client.open("Discord_Trending_Songs").sheet1
  return sheet

def AddSongEntry(name, link, requestor="Not provided"):
  timestamp = str(datetime.now())
  row = [name, link, requestor, timestamp]
  sheet = InitGoogleSheetsAuth()
  sheet.insert_row(row, 2)

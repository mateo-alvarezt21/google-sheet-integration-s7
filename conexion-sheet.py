import gspread
from google.oauth2.service_account import Credentials

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_file('ServiceAccountCredentials.json', scopes=SCOPE)

client = gspread.authorize(creds)

sheet = client.open("SheetConection-cesde").sheet1

# Acceder a los datos
print(sheet.get_all_records())

# Insertar datos
sheet.insert_row(["Juanes", "21", "Ing"], 6)
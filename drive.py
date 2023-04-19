# Import the required libraries
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set up the client secret file and the scopes
CLIENT_SECRET_FILE = 'cred/cred.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

# Set up the authorization flow
flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRET_FILE,
    scopes=SCOPES
)
creds = flow.run_local_server(port=0)

# Set up the Drive API client
drive_service = build('drive', 'v3', credentials=creds)

# Set the ID of the folder you want to retrieve the links from
folder_id = '1VsDxRefGRg1YXjRkOj5E1wp1FfjeSCKq'

# Retrieve a list of all files in the folder
results = drive_service.files().list(q=f"'{folder_id}' in parents and trashed = false", fields="nextPageToken, files(id, name, webViewLink)").execute()
items = results.get('files', [])

# Print the links for each file
if not items:
    print('No files found.')
else:
    print('Links:')
    for item in items:
        print(f"{item['name']}: {item['webViewLink']}")

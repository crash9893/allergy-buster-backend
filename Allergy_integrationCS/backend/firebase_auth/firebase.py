import firebase_admin
from firebase_admin import credentials, auth

# Path to your Firebase service account key
cred = credentials.Certificate("allergycheck-b48a9-firebase-adminsdk-fbsvc-143de6fd9d.json")

# Initialize the app with the credentials
firebase_admin.initialize_app(cred)

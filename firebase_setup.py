#firebase_setup.py   import firebase_admin
from firebase_admin import credentials, firestore
import firebase_admin
import pyrebase
from config import config  # Import your Firebase config

#Firebase Setup
if not firebase_admin._apps:
    cred = credentials.Certificate('service-account-file.json')
    firebase_admin.initialize_app(cred)

#Pyrebase Setup
firebase = pyrebase.initialize_app(config)
auth_client = firebase.auth()

#Firestore Setup
db = firestore.client()
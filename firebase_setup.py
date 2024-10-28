import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
from config import config  # Ensure you have your Firebase config in a config.py file

# Firebase Setup
if not firebase_admin._apps:
    cred = credentials.Certificate('service-account-file.json')  # Update this path as needed
    firebase_admin.initialize_app(cred)

# Pyrebase Setup
firebase = pyrebase.initialize_app(config)  # This should contain your Firebase configuration
auth_client = firebase.auth()

# Firestore Setup
db = firestore.client()

def write_events_to_firebase(events):
    """
    Write a list of events to Firestore.
    
    Parameters:
        events (list): A list of dictionaries containing event data.
    """
    for event in events:
        db.collection('events').add(event)  # Adds each event as a separate document

def get_events_from_firebase():
    """
    Retrieve events from Firestore.

    Returns:
        list: A list of dictionaries representing the events.
    """
    events_ref = db.collection('events')
    events = []
    try:
        print("Fetching events from Firestore...")
        for doc in events_ref.stream():
            events.append(doc.to_dict())  # Convert each document to a dictionary
            print(f"Fetched event: {doc.id} -> {doc.to_dict()}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return events

from config import config  # Import your Firebase config

# Firebase Setup
if not firebase_admin._apps:
    cred = credentials.Certificate('service-account-file.json')
    firebase_admin.initialize_app(cred)

# Pyrebase Setup
firebase = pyrebase.initialize_app(config)
auth_client = firebase.auth()

# Firestore Setup
db = firestore.client()
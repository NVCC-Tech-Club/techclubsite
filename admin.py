import streamlit as st
from firebase_admin import firestore

# Function to display admin features
def admin_page(db):
    st.title("Admin Page")
    st.write("Welcome, Admin!")

    # Get the total number of users
    users_ref = db.collection('users')
    users_count = users_ref.get()  # Retrieve all users

    st.write(f"Total number of users: {len(users_count)}")

    # Add your admin functionalities here
    st.write("Here you can manage users, view reports, etc.")
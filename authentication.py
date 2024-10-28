#authentication.py
import streamlit as st
from firebase_setup import auth_client, db

# Sign Up Function
def sign_up(first_name, last_name, gender, github_link, linkedin_link, field_of_interest, email, password):
    try:
        user = auth_client.create_user_with_email_and_password(email, password)
        create_user_profile(user['localId'], {
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "github_link": github_link,
            "linkedin_link": linkedin_link,
            "field_of_interest": field_of_interest,
            "email": email
        })
        st.success(f'Successfully created user: {user["localId"]}')
    except Exception as e:
        st.error(f'Error: {str(e)}')

# Function to create a user profile in Firestore
def create_user_profile(user_id, user_data):
    try:
        # Add the user profile to the Firestore database in a "users" collection
        db.collection('users').document(user_id).set(user_data)
        st.success(f'User profile created for {user_data["first_name"]} {user_data["last_name"]}')
    except Exception as e:
        st.error(f'Error creating user profile: {str(e)}')

# Sign In Function
def sign_in(email, password):
    try:
        user = auth_client.sign_in_with_email_and_password(email, password)
        if user:
            st.session_state.user = user
            st.success(f'Successfully signed in: {user.get("localId", "Unknown")}')
            return user
    except Exception as e:
        st.error(f'Error: {str(e)}')

# Password Reset Function
def send_password_reset_email(email):
    try:
        auth_client.send_password_reset_email(email)
        st.success(f"Password reset link sent to {email}.")
    except Exception as e:
        st.error(f"Error: {e}")

# Logout Function
def logout():
    st.session_state.user = None
    st.success("Successfully logged out.")

# Function to check if the user is an admin
def is_admin(user_email):
    admin_ref = db.collection('admins').where('email', '==', user_email).get()
    return len(admin_ref) > 0

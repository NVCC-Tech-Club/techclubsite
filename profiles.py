#profile.py 
import streamlit as st
from firebase_setup import db

# Function to display the user profile
def profile_page():
    st.title("Profile Page")
    if "user" in st.session_state and st.session_state.user is not None:
        uid = st.session_state.user.get("localId")
        if uid:
            user_data = db.collection('users').document(uid).get()
            if user_data.exists:
                user_info = user_data.to_dict()
                st.write(f"First Name: {user_info.get('first_name', 'N/A')}")
                st.write(f"Last Name: {user_info.get('last_name', 'N/A')}")
                st.write(f"Email: {user_info.get('email', 'N/A')}")
                if "profile_photo_url" in user_info:
                    st.image(user_info["profile_photo_url"], width=100)
            else:
                st.error("User data not found.")
        else:
            st.error("User ID not found.")
    else:
        st.error("You are not logged in.")
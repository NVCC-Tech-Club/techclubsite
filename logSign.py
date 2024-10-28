#main.py
import streamlit as st
from firebase_setup import auth_client, db  # Import Firebase and Firestore setups
from authentication import sign_up, sign_in, send_password_reset_email, logout, is_admin  # Auth functions
from profiles import profile_page # Profile page functions
from admin import admin_page  # Admin page function
from pages import club_blog, event_calendar


st.title('NVCC Tech Club Authentication')


if "user" not in st.session_state or st.session_state.user is None:
    menu = st.sidebar.selectbox("Select Action", ["Sign Up", "Sign In", "Forgot Password"])
else:
    user_email = st.session_state.user.get("email", "")
    if is_admin(user_email):
        menu = st.sidebar.selectbox("Select Action", ["Profile", "Admin Page", "Log Out"])
    else:
        menu = st.sidebar.selectbox("Select Action", ["Profile", "Log Out"])

if menu == "Sign Up":
    st.subheader("Sign Up")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    gender = st.selectbox("Gender", ["Select", "Male", "Female", "Non-binary", "Other"])
    github_link = st.text_input("GitHub Profile Link (optional)")
    linkedin_link = st.text_input("LinkedIn Profile Link (optional)")
    field_of_interest = st.text_input("Field of Interest")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    
    if st.button("Sign Up"):
        if gender == "Select":
            st.error("Please select your gender.")
        elif not field_of_interest:
            st.error("Please enter your field of interest.")
        else:
            sign_up(first_name, last_name, gender, github_link, linkedin_link, field_of_interest, email, password)

elif menu == "Sign In":
    st.subheader("Sign In")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    
    if st.button("Sign In"):
        user = sign_in(email, password)
        if user:
            st.session_state.user = user
            st.rerun()

elif menu == "Forgot Password":
    st.title("Password Reset")
    email_input = st.text_input("Enter your email to reset your password:")
    if st.button("Send Password Reset Email"):
        send_password_reset_email(email_input)

elif menu == "Profile":
    profile_page()
    if st.button("Log Out"):
        logout()
        st.rerun()

elif menu == "Admin Page":
    if "user" in st.session_state:
        admin_page(db)
    else:
        st.error("You must be logged in as an admin to access this page.")


elif menu == "Log Out":
    if st.button("Log Out"):
        logout()
        st.rerun()
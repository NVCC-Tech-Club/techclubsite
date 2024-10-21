import streamlit as st
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZjMDYzNzA0M2Q1MjZmNTUzNTUxMzIi_pc"

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Name")
        contact = st.text_input("Point of Contact (N/A if no replyback desired)")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            # Prepare data and send to webhook URL
            data = {"name": name, "contact": contact, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)
            
            if response.status_code == 200:
                st.success("Message successfully sent!")
            else:
                st.error("There was an error sending your message.")
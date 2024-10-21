import streamlit as st

@st.dialog("Contact Us")
def show_contact_form():
    st.text_input("Name")

# --- MAIN HUB ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./img/club_people.jpg", width=650)
with col2:
    st.title("NOVA Tech Club", anchor=False)
    st.write(
        """
        The core mission of Tech Enthusiasts club is to empower
        curious, creative minds who are deeply passionate about
        technology and its applicationsin our world. TECH aims
        to connect diverse different communities of enthusiasts
        through skillsbuilding exercises such as: competitions,
        workshops, and projects; we provide the support to turn
        a technology interest into a successful lifelong career.
        """
    )
    if st.button("✉️ Contact Us",use_container_width=True):
        show_contact_form()
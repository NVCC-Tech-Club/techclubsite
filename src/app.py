import streamlit as st

st.set_page_config(
        page_title="Main Menu",
)

st.title("Multipage Streamlit website")
st.write("Welcome to Tech Club's official website!")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Home", "Officers", "Roadmap"])

if page == "Home":
    st.title("Welcome to My App")
    st.write("This is the home page.")
elif page == "Officers":
    st.title("Current officers")
    # Add data analysis content here
elif page == "Roadmap":
    st.title("Our roadmap for 2024-25")
    # Add visualizations here
    
user_input = st.text_input("Enter something:")
st.write(f"You entered: {user_input}")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write(data)
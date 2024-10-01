import streamlit as st

st.title("Multipage Streamlit website")
st.write("Welcome to Tech Club's official website!")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Home", "Data Analysis", "Visualization"])

if page == "Home":
    st.title("Welcome to My App")
    st.write("This is the home page.")
elif page == "Data Analysis":
    st.title("Data Analysis Page")
    # Add data analysis content here
elif page == "Visualization":
    st.title("Visualization Page")
    # Add visualizations here
    
user_input = st.text_input("Enter something:")
st.write(f"You entered: {user_input}")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write(data)
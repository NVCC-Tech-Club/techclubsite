import streamlit as st

st.title("Welcome to Tech Club's official website!")

user_input = st.text_input("Enter something:")
st.write(f"You entered: {user_input}")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write(data)
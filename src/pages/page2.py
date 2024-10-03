import streamlit as st
import sys
sys.path.append("../")
from functions.table import mask_equal
from functions.col import pdb_code_col
from functions.path import pages_str, data_str, get_file_path
from functions.gui import load_st_table, write_st_end, create_st_button, show_st_structure, get_neighbor_path

def page1():
    
    left_col, right_col = st.columns(2)
    
    df = load_st_table(__file__)
    
    show_st_structure(mask_equal(df, pdb_code_col, "6oim"),
            zoom=1.2,
            width=400,
            height=300,
            cartoon_trans=0,
            surface_trans=1,
            spin_on=True,
            st_col=left_col)
    
    right_col.markdown("# Tech Club")
    right_col.markdown("### A place to share latest happenings in the Tech industry")
    right_col.markdown("**NOVA Loudoun Campus**")
    
    community_link_dict = {
        "Github Page": "https://github.com/Fraexex/techclubsite/",
    }
    
    st.sidebar.markdown("## Community Links")
    for link_text, link_url in community_link_dict.items():
        create_st_button(link_text, link_url, st_col=st.sidebar)
        
    software_link_dict = {
        "Streamlit": "https://streamlit.io",
    }
    
    st.sidebar.markdown("## Software Links")
    link_1_col, link_2_col, link_3_col = st.sidebar.columns(3)
    
    i = 0
    link_col_dict = {0: link_1_col, 1: link_2_col, 2: link_3_col}
    for link_text, link_url in software_link_dict.items():

        st_col = link_col_dict[i]
        i += 1
        if i == len(link_col_dict.keys()):
            i = 0

        create_st_button(link_text, link_url, st_col=st_col)

    st.markdown("---")

    user_input = st.text_input("Enter something:")
    st.write(f"You entered: {user_input}")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write(data)
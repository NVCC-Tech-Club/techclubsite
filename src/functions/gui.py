import pandas as pd
import uuid
import re
from random import randint
import streamlit as st

from .file import entry_table_file
from .path import (
    load_table,
    load_json,
    get_file_path,
    get_dir_path,
    get_neighbor_path,
    pages_str,
    data_str,
    functions_str,
)
from .col import date_col

def write_st_end():

    df = load_table(
        get_file_path(
            entry_table_file,
            dir_path=get_neighbor_path(__file__, functions_str, data_str),
        )
    )

    df[date_col] = pd.to_datetime(df[date_col])
    df[date_col] = df[date_col].dt.strftime("%Y-%m")

    st.markdown("---")
    st.markdown(
        "Developed and Maintained by Christian Galvez"
    )
    st.markdown(
        "[NOVA Loudoun Campus](https://www.nvcc.edu/about/locations/loudoun/index.html)"
    )
    st.markdown(f"Most Recently Deposited Entry {df[date_col].max()}")
    st.markdown("Copyright (c) 2024 NOVA Tech Club")

def load_st_table(file_path, file_name=None, json_format=False):

    if file_name is None:
        file_name = entry_table_file

    file_path = get_file_path(
            file_name,
            dir_path=get_dir_path(
                dir_path=get_neighbor_path(file_path, pages_str, data_str)
            ))

    if json_format:
        return load_json(file_path)
    else:
        return load_table(file_path)


def create_st_button(link_text, link_url, hover_color="#e78ac3", st_col=None):

    button_uuid = str(uuid.uuid4()).replace("-", "")
    button_id = re.sub("\d+", "", button_uuid)

    button_css = f"""
        <style>
            #{button_id} {{
                background-color: rgb(255, 255, 255);
                color: rgb(38, 39, 48);
                padding: 0.25em 0.38em;
                position: relative;
                text-decoration: none;
                border-radius: 4px;
                border-width: 1px;
                border-style: solid;
                border-color: rgb(230, 234, 241);
                border-image: initial;

            }}
            #{button_id}:hover {{
                border-color: {hover_color};
                color: {hover_color};
            }}
            #{button_id}:active {{
                box-shadow: none;
                background-color: {hover_color};
                color: white;
                }}
        </style> """

    html_str = f'<a href="{link_url}" target="_blank" id="{button_id}";>{link_text}</a><br></br>'

    if st_col is None:
        st.markdown(button_css + html_str, unsafe_allow_html=True)
    else:
        st_col.markdown(button_css + html_str, unsafe_allow_html=True)
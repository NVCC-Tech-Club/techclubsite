import streamlit as st

# Importing the page modules
from pages import *

def main():
    st.title("Welcome to the Club!")

    # Search bar
    search_term = st.text_input("Search for pages:", "")
    
    # Navigation links
    st.header("Main Pages")
    pages = {
        "Event Calendar": pages.event_calendar.app,
        "Project Showcase": pages.project_showcase.app,
        "Member Directory": pages.member_directory.app,
        "Coding Challenges": pages.coding_challenges.app,
        "Resources Section": pages.resources.app,
        "Discussion Forum/Chat": pages.forum.app,
        "Club Blog": pages.club_blog.app,
        "Live Code Demos": pages.live_demos.app,
        "Club Voting": pages.club_voting.app,
        "Leaderboard": pages.leaderboard.app
    }
    
    # Filter pages based on search term
    filtered_pages = {k: v for k, v in pages.items() if search_term.lower() in k.lower()}

    # Display navigation links
    for page_name, page_function in filtered_pages.items():
        if st.button(page_name):
            page_function()

if __name__ == "__main__":
    main()

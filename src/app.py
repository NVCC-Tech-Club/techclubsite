import streamlit as st
import os

# Importing the page modules
import pages.event_calendar as event_calendar
import pages.project_showcase as project_showcase
import pages.member_directory as member_directory
import pages.coding_challenges as coding_challenges
import pages.resources as resources
import pages.forum as forum
import pages.club_blog as club_blog
import pages.live_demos as live_demos
import pages.club_voting as club_voting
import pages.leaderboard as leaderboard

# Edit page config as needed
st.set_page_config(page_title="Tech Home", layout="wide", initial_sidebar_state="collapsed")

# Function to display the selected page
def display_page(page_key):
    if page_key == "event_calendar":
        event_calendar.app()
    elif page_key == "project_showcase":
        project_showcase.app()
    elif page_key == "member_directory":
        member_directory.app()
    elif page_key == "coding_challenges":
        coding_challenges.app()
    elif page_key == "resources":
        resources.app()
    elif page_key == "forum":
        forum.app()
    elif page_key == "club_blog":
        club_blog.app()
    elif page_key == "live_demos":
        live_demos.app()
    elif page_key == "club_voting":
        club_voting.app()
    elif page_key == "leaderboard":
        leaderboard.app()
    else:
        st.write("Select a page.")

def main():
    st.image(os.path.join(os.getcwd(), "img\techclub_logo.png"), width=200)
    st.title("Welcome to the Club! 🎉")

    # Check session state for page selection
    if "page" not in st.session_state:
        st.session_state.page = None
    
    # Navigation links
    st.header("Main Pages")
    page = {
        "Event Calendar": event_calendar.app,
        "Project Showcase": project_showcase.app,
        "Member Directory": member_directory.app,
        "Coding Challenges": coding_challenges.app,
        "Resources Section": resources.app,
        "Discussion Forum/Chat": forum.app,
        "Club Blog": club_blog.app,
        "Live Code Demos": live_demos.app,
        "Club Voting": club_voting.app,
        "Leaderboard": leaderboard.app
    }

    # Display buttons for navigation
    for page_name, page_key in page.items():
        if st.button(page_name):
            st.session_state.page = page_key  # Store selected page in session state
            st.experimental_rerun()  # Refresh the app to show the selected page

    # If a page has been selected, display it
    if st.session_state.page:
        display_page(st.session_state.page)

if __name__ == "__main__":
    main()

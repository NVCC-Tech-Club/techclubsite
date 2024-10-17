import streamlit as st

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

def main():
    st.title("Welcome to the Club!")

    # Search bar
    search_term = st.text_input("Search for pages:", "")
    
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
    
    # Filter pages based on search term
    filtered_pages = {k: v for k, v in page.items() if search_term.lower() in k.lower()}

    # Display navigation links
    for page_name, page_function in filtered_pages.items():
        if st.button(page_name):
            page_function()

if __name__ == "__main__":
    main()

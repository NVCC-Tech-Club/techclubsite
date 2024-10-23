import streamlit as st

# --- CUSTOM CONFIG ---
st.set_page_config(page_title="NOVA Tech Club", layout="wide")

# Hide streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- PAGE SETUP ---


LogIn = st.Page(
    page="logSign.py",
    title="Log In or Sign Up",
    icon="🏠"
)
home = st.Page(
    page="pages/home.py",
    title="Home",
    icon="🏠",
    default=True,
)


club_blog = st.Page(
    page="pages/club_blog.py",
    title="Club Blog",
    icon="📔",
)

club_voting = st.Page(
    page="pages/club_voting.py",
    title="Club Voting",
    icon="✅",
)

coding_challenges = st.Page(
    page="pages/coding_challenges.py",
    title="Coding Challenges",
    icon="💀",
)

event_calendar = st.Page(
    page="pages/event_calendar.py",
    title="Event Calendar",
    icon="📆",
)

forum = st.Page(
    page="pages/forum.py",
    title="Forum",
    icon="💬",
)

leaderboard = st.Page(
    page="pages/leaderboard.py",
    title="Leaderboard",
    icon="🏅",
)

live_demos = st.Page(
    page="pages/live_demos.py",
    title="Live Demos",
    icon="🪧",
)

member_directory = st.Page(
    page="pages/member_directory.py",
    title="Member Directory",
    icon="➡️",
)

project_showcase = st.Page(
    page="pages/project_showcase.py",
    title="Project Showcase",
    icon="🫙",
)

resources = st.Page(
    page="pages/resources.py",
    title="Resources",
    icon="📚",
)

# --- NAVIGATION SETUP ---
pg = st.navigation(
    {   
        "Login": [LogIn],
        "Home": [home],
        "Info": [club_blog, event_calendar, forum, resources],
        "Members": [club_voting, leaderboard, member_directory],
        "Projects": [coding_challenges, live_demos, project_showcase],
        
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("assets/img/techclub_logo.png")
st.sidebar.text("Made with 💗 by NVCC students")

# --- RUN NAVIGATION ---
pg.run()
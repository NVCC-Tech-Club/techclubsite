import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Sample event data with date and time
events = {
    'DateTime': ['2024-10-30 10:00', '2024-11-05 14:00', '2024-11-15 18:30', '2024-12-01 09:00'],
    'Event': ['Zoom', 'Python - Workshop', 'Guest Lecture', 'Project Deadline'],
    'Type': ['Competition', 'Learning', 'Lecture', 'Deadline'],
    'Link': ['https://example.com/hackathon', 
             'https://example.com/workshop', 
             'https://example.com/guest-lecture', 
             'https://example.com/project-deadline']
}

# Create a DataFrame and convert DateTime column to datetime
df = pd.DataFrame(events)
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%Y-%m-%d %H:%M')

# Get the current date
current_date = datetime.now()

# Define event colors
event_colors = {
    'Competition': '#FF6347',   # Tomato Red
    'Learning': '#1E90FF',      # Dodger Blue
    'Lecture': '#32CD32',       # Lime Green
    'Deadline': '#FFA500'       # Orange
}

# Initialize Plotly figure
fig = go.Figure()

# Add a trace for each event type, color-coded with enhanced marker size and shapes
for i, row in df.iterrows():
    fig.add_trace(go.Scatter(
        x=[row['DateTime']],
        y=[row['DateTime'].hour],  # Set y-axis to the hour of the event
        mode='markers+text',
        marker=dict(color=event_colors[row['Type']], size=14, symbol="circle"),
        text=row['Event'],
        textposition="top center",
        name=row['Event'],
        hovertext=f"{row['Event']}<br>{row['DateTime'].strftime('%Y-%m-%d %H:%M')}<br><a href='{row['Link']}'>More Info</a>",
        hoverinfo="text",
        opacity=0.8  # Slight transparency for aesthetics
    ))

# Update layout to set x-axis and y-axis labels and apply aesthetic improvements
fig.update_layout(
    title=dict(
        text="Event Calendar",
        font=dict(size=28, color="#2F4F4F", family="Arial"),  # Custom font and color
        x=0.5,  # Center align the title
    ),
    xaxis_title="Date & Time",
    yaxis_title="Hour",
    xaxis=dict(
        range=[current_date, df['DateTime'].max()],
        tickformat="%Y-%m-%d %H:%M",
        showgrid=False,  # Hide grid lines
        zeroline=False,  # Hide zero line
    ),
    yaxis=dict(
        tickvals=list(range(0, 24)),  # Hourly ticks (0-23)
        ticktext=[f"{hour}:00" for hour in range(24)],  # Hour labels (0:00 to 23:00)
        title=None,
        showgrid=True,  # Show grid for better visual guidance
        zeroline=False  # Hide zero line
    ),
    height=500,
    hovermode='closest',
    
    # Customize background with rgba colors for soft transparency effects
    plot_bgcolor="rgba(255, 255, 255, 0)",  # Transparent plot background
    paper_bgcolor="rgba(230, 245, 255, 0.85)",  # Light blue background with some transparency
    font=dict(family="Arial", color="#2F4F4F"),  # Text font and color
    margin=dict(l=30, r=30, t=80, b=30),  # Adjust margins for cleaner layout
)

# Display the interactive plot in Streamlit
st.markdown("""
    <style>
    .plotly-graph-div {
        border-radius: 15px;  /* Set border radius */
        overflow: hidden;      /* Ensure corners are rounded */
        border: 2px solid #A9C8E3;  /* Optional: Add border color */
    }
    </style>
""", unsafe_allow_html=True)

st.plotly_chart(fig)

# Function to make events clickable (separate clickable links)
st.write("### Click the links for more event details:")
for i in range(len(df)):
    st.markdown(f"[{df.iloc[i]['Event']}]({df.iloc[i]['Link']})")

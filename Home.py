import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('C:/Users/DELL/mydatabase.db')
c = conn.cursor()

# Define function to get data from the database based on date and analysis type
def get_data(date, analysis):
    if analysis == 'Complete Analysis':
        # Get data for all emotions
        query = f"SELECT SUM(Male_Angry), SUM(Male_Fear), SUM(Male_Happy), SUM(Male_Neutral), SUM(Male_Sad), SUM(Male_Surprise), SUM(Male_Disgust), SUM(Female_Angry), SUM(Female_Fear), SUM(Female_Happy), SUM(Female_Neutral), SUM(Female_Sad), SUM(Female_Surprise), SUM(Female_Disgust) FROM emotions WHERE Date = '{date}'"
    elif analysis == 'Male Analysis':
        # Get data for male emotions
        query = f"SELECT SUM(Male_Angry), SUM(Male_Fear), SUM(Male_Happy), SUM(Male_Neutral), SUM(Male_Sad), SUM(Male_Surprise), SUM(Male_Disgust) FROM emotions WHERE Date = '{date}'"
    elif analysis == 'Female Analysis':
        # Get data for female emotions
        query = f"SELECT SUM(Female_Angry), SUM(Female_Fear), SUM(Female_Happy), SUM(Female_Neutral), SUM(Female_Sad), SUM(Female_Surprise), SUM(Female_Disgust) FROM emotions WHERE Date = '{date}'"
    c.execute(query)
    data = c.fetchone()
    return data

# Define function to create pie chart

def create_bar_chart(labels, sizes):
    fig, ax = plt.subplots()
    ax.barh(labels, sizes, height=0.5)
    ax.set_xlabel('Number of Emotions')
    ax.set_ylabel('Emotion Type')
    ax.set_title('Emotion Analysis')
    st.pyplot(fig)


# Define function to run the Streamlit app
def run():
    # Set page title and icon
    st.set_page_config(page_title='Emotion Analysis', page_icon=':bar_chart:')

    # Set sidebar options
    st.sidebar.title('Emotion Analysis')

    date = st.date_input("Select a date")
    date = date.strftime("%Y-%m-%d")

    analysis_type = st.selectbox('Select Analysis Type', ('Complete Analysis', 'Male Analysis', 'Female Analysis'))

    # Check if date is entered and valid
    if date == '':
        st.warning('Please enter a date')
        return
    try:
        pd.to_datetime(date)
    except ValueError:
        st.warning('Please enter a valid date in the format YYYY-MM-DD')
        return

    # Get data from database
    data = get_data(date, analysis_type)

    # Check if data is None
    if data is None:
        st.warning('No data found for the entered date')
        return

    # Create pie chart
    if analysis_type == 'Complete Analysis':
        labels = ['Male Angry', 'Male Fear', 'Male Happy', 'Male Neutral', 'Male Sad', 'Male Surprise', 'Male Disgust', 'Female Angry', 'Female Fear', 'Female Happy', 'Female Neutral', 'Female Sad', 'Female Surprise', 'Female Disgust']
    elif analysis_type == 'Male Analysis':
        labels = ['Angry', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise', 'Disgust']
    elif analysis_type == 'Female Analysis':
        labels = ['Angry', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise', 'Disgust']
    create_bar_chart(labels, data)

    # Display data as table
    df = pd.DataFrame([data], columns=labels)
    st.table(df)


run()
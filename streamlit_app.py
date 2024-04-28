pip install gtts 
pip install streamlit

import streamlit as st
from gtts import gTTS
from IPython.display import Audio
import os

# Define a function to convert text to speech
def speak(text):
    # Create the gTTS object
    tts = gTTS(text=text, lang='en')
    
    # Save the audio file
    audio_file = 'output.mp3'
    tts.save(audio_file)
    
    # Return the audio file
    return audio_file

# Create a Streamlit web app
st.title('Text-to-Speech Demo')

# Add a text input component
text_input = st.text_input('Enter text:', 'Hello, world!')

# Add a button to trigger text-to-speech conversion
if st.button('Convert to Speech'):
    # Call the speak function to convert text to speech
    audio_file = speak(text_input)
    
    # Display the audio file as an audio player
    st.audio(audio_file, format='audio/mp3')


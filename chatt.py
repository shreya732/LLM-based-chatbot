import os
import tempfile
import datetime
import chatbot_function

import streamlit as st
from audio_recorder_streamlit import audio_recorder
import chatbot_function  # Assuming your chatbot functions are in this file

st.title('🎙️🤖Voice ChatBot🤖🎙️')  # Set the title for the Streamlit web application

# Use the audio_recorder function to record audio input
audio_bytes = audio_recorder(
    text="Click to record",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="microphone",
    icon_size="3x",
)

# Check if audio recording is successful
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")  # Display the recorded audio on UI

    # Save audio to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    # Check if the 'Get Response' button is clicked
    if st.button('🎙️ Get Response 🎙️'):
        # Converting speech to text
        try:
            converted_text_openai = chatbot_function.speech_to_text_conversion(temp_audio_path)
            st.write("Transcription:", converted_text_openai)  # Display the transcription on UI

            # Generate response using text-based model
            textmodel_response = chatbot_function.text_chat(converted_text_openai)
            st.write("Chatbot Response:", textmodel_response)  # Display the chatbot response

            # Convert the text response to speech format
            audio_data = chatbot_function.text_to_speech_conversion(textmodel_response)

            # Save the audio response to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                tmpfile.write(audio_data)
                tmpfile_path = tmpfile.name
                st.audio(tmpfile_path)  # Play the audio response
        except Exception as e:
            st.error(f"Error processing the audio: {str(e)}")

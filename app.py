
import os
import threading
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

# Load environment variables
load_dotenv("api_key.env")
groq_api_key = os.getenv("groq_api_key")

# Initialize Groq client
if not groq_api_key:
    st.error("API key not found. Ensure it's set correctly in api_key.env.")
else:
    client = Groq(api_key=groq_api_key)

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak_text(text):
    """Speak text in a separate thread."""
    engine.say(text)
    engine.runAndWait()

# CSS for styling
st.markdown("""
<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
}
.chat-box {
    background-color: #fff;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.user-query {
    background-color: #e8f5e9;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 5px;
    color: #2e7d32;
    font-weight: bold;
}
.bot-response {
    background-color: #e3f2fd;
    border-radius: 10px;
    padding: 10px;
    color: #1565c0;
}
.button {
    border-radius: 5px;
    background-color: #007bff;
    color: #fff;
    padding: 10px 15px;
    font-size: 14px;
    border: none;
    cursor: pointer;
}
.button:hover {
    background-color: #0056b3;
}
.history-item {
    background-color: #f5f5f5;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 5px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("💬 Chat with Groq's LLM")
st.sidebar.title("Personalization")

# Model selection
st.sidebar.subheader("System Prompt:")
model = st.sidebar.selectbox('Choose a model', ['Llama3-8b-8192', 'Llama3-70b-8192', 'Mixtral-8x7b-32768', 'Gemma-7b-It'])

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "voice_query" not in st.session_state:
    st.session_state.voice_query = ""
if "bot_speaking" not in st.session_state:
    st.session_state.bot_speaking = False

# Speech-to-text
st.sidebar.subheader("🎤 Speech Input")
recognizer = sr.Recognizer()

if st.sidebar.button("🎙️ Use Microphone"):
    with sr.Microphone() as source:
        st.sidebar.info("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            st.session_state.voice_query = recognizer.recognize_google(audio)
            st.sidebar.success(f"Recognized Text: {st.session_state.voice_query}")
        except sr.UnknownValueError:
            st.sidebar.error("Sorry, could not understand the audio.")
        except sr.RequestError:
            st.sidebar.error("Speech recognition service error.")
        except sr.WaitTimeoutError:
            st.sidebar.error("Listening timed out. Please try again.")

# User query
user_input = st.text_input("Enter your query or use speech input:", st.session_state.voice_query, key="user_input")

# Function to interrupt and reset speaking state
def interrupt_speech():
    if st.session_state.bot_speaking:
        engine.stop()  # Stop the current speaking thread

# Chat functionality
if st.button("Send", key="send"):
    interrupt_speech()  # Allow user to interrupt

    query = user_input.strip()
    if not query:
        st.error("Please provide a query.")
    else:
        st.session_state.bot_speaking = True  # Indicate that the bot is speaking

        # Generate response
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": query}],
            model=model,
        )
        response = chat_completion.choices[0].message.content

        # Store in history
        st.session_state.history.append({"query": query, "response": response})

        # Display query and response
        st.markdown(f'<div class="chat-box user-query">👤 {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-box bot-response">🤖 {response}</div>', unsafe_allow_html=True)

        # Speak the response in a separate thread
        threading.Thread(target=speak_text, args=(response,), daemon=True).start()

        st.session_state.bot_speaking = False  # Reset speaking state once the bot finishes speaking

# History
st.sidebar.title("🕒 Chat History")
for i, entry in enumerate(st.session_state.history):
    st.sidebar.markdown(f'<div class="history-item">Query {i+1}: {entry["query"]}</div>', unsafe_allow_html=True)

# Clear history
if st.sidebar.button("🗑️ Clear History"):
    st.session_state.history.clear()
    st.sidebar.success("History cleared.")

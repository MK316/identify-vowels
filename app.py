import streamlit as st
from gtts import gTTS
import random
import io

# Sample word dictionary with IPA transcription
word_dict = {
    'head': '/ɛ/',
    'beat': '/i/',
    'bat': '/æ/',
    'boot': '/u/',
    'book': '/ʊ/',
    'bird': '/ɜ˞/',
    'about': '/aʊ/',
    'bed': '/ɛ/',
    'bad': '/æ/',
    'bit': '/ɪ/',
    'bet': '/ɛ/',
    'father': '/ɑ/',
    'caught': '/ɔ/',
    'cut': '/ʌ/',
}

# Function to generate audio for the given word
def generate_audio(word):
    tts = gTTS(text=word, lang='en', tld='us')  # American English accent
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

# Main app
st.title("Vowel Sound Practice App")

# Choose a random word from the dictionary if not already chosen or after "Next Word" is clicked
if "current_word" not in st.session_state or st.session_state.get("next_word"):
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))
    st.session_state.next_word = False

# Display the audio player
st.write("Listen to the word:")
audio_buffer = generate_audio(st.session_state.current_word)
st.audio(audio_buffer, format="audio/mp3")

# Display vowel options as clickable buttons in three rows
st.write("Choose the vowel sound for the word you heard:")

# Vowel options organized in three rows
vowel_options_row1 = ['/i/', '/ɪ/', '/ɛ/', '/æ/', '/u/']
vowel_options_row2 = ['/ʊ/', '/ɔ/', '/ə/', '/ʌ/', '/ɑ/']
vowel_options_row3 = ['/eɪ/', '/oʊ/', '/ɔɪ/', '/aɪ/', '/aʊ/', '/ɜ˞/', '/ɚ/']

# Create three columns for each row of vowel options
col1, col2, col3, col4, col5 = st.columns(5)
with col1: option1 = st.radio("", vowel_options_row1, index=0, key="row1", label_visibility="collapsed")
with col2: option2 = st.radio("", vowel_options_row2, index=0, key="row2", label_visibility="collapsed")
with col3: option3 = st.radio("", vowel_options_row3, index=0, key="row3", label_visibility="collapsed")

# Selected vowel
selected_vowel = st.session_state.row1 if st.session_state.row1 else (
                 st.session_state.row2 if st.session_state.row

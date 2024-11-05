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

# Choose a random word from the dictionary if not already chosen or after "Submit" is clicked
if "current_word" not in st.session_state or st.button("Next Word"):
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))

# Display the audio player
st.write("Listen to the word:")
audio_buffer = generate_audio(st.session_state.current_word)
st.audio(audio_buffer, format="audio/mp3")

# Display vowel options as clickable buttons in three rows
st.write("Choose the vowel sound for the word you heard:")
vowel_options_row1 = ['/i/', '/ɪ/', '/ɛ/', '/æ/', '/u/']
vowel_options_row2 = ['/ʊ/', '/ɔ/', '/ə/', '/ʌ/', '/ɑ/']
vowel_options_row3 = ['/eɪ/', '/oʊ/', '/ɔɪ/', '/aɪ/', '/aʊ/', '/ɜ˞/', '/ɚ/']

selected_vowel = st.radio("Select the vowel sound:", vowel_options_row1 + vowel_options_row2 + vowel_options_row3)

# Submit button to check answer and load a new word
if st.button("Submit"):
    if selected_vowel == st.session_state.correct_vowel:
        st.success("Correct!")
    else:
        st.error("Try again.")
    
    # Load a new word for the next attempt
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))

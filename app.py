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

# Choose a random word from the dictionary
word, correct_vowel = random.choice(list(word_dict.items()))

# Display the audio player
st.write("Listen to the word:")
audio_buffer = generate_audio(word)
st.audio(audio_buffer, format="audio/mp3")

# Display vowel options as clickable buttons
st.write("Choose the vowel sound for the word you heard:")
vowel_options = ['/i/', '/ɪ/', '/ɛ/', '/æ/', '/u/', '/ʊ/', '/ɔ/', '/ə/', '/ʌ/', '/ɑ/', '/eɪ/', '/oʊ/', '/ɔɪ/', '/aɪ/','/aʊ/','/ɜ˞/', '/ɚ/']

# Store selected vowel in session state
if 'selected_vowel' not in st.session_state:
    st.session_state.selected_vowel = None

# Display buttons for each vowel option and capture the selection
for vowel in vowel_options:
    if st.button(vowel):
        st.session_state.selected_vowel = vowel

# Check the answer and give feedback if a vowel is selected
if st.session_state.selected_vowel:
    if st.session_state.selected_vowel == correct_vowel:
        st.success("Correct!")
    else:
        st.error("Try again")

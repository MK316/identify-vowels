import streamlit as st
from gtts import gTTS
import io

# Sample word dictionary with IPA transcription
word_dict = {
    'head': '/ɛ/',
    'beat': '/i/',
    'bat': '/æ/',
    'boot': '/u/',
    'book': '/ʊ/',
    'bird': '/ɜ˞/',
    'about': '/ə/',
    'bed': '/ɛ/',
    'bad': '/æ/',
    'bit': '/ɪ/',
    'bet': '/ɛ/',
    'father': '/ɑ/',
    'caught': '/ɔ/',
    'cut': '/ʌ/',
    'her': '/ɜ/'
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

# Select a random word from the dictionary
word = st.selectbox("Choose a word to practice:", list(word_dict.keys()))
correct_vowel = word_dict[word]

# Display the audio player
st.write("Listen to the word:")
audio_buffer = generate_audio(word)
st.audio(audio_buffer, format="audio/mp3")

# Display options for vowel selection
st.write("Choose the vowel sound for the word you heard:")
vowel_options = ['/i/', '/ɪ/', '/eɪ/', '/ɛ/', '/æ/', '/ɑ/', '/ɔ/', '/oʊ/', '/u/', '/ʊ/', '/ɝ/', '/ɜ˞/', '/ə/', '/ʌ/', '/ɚ/']
selected_vowel = st.selectbox("Select the vowel sound:", vowel_options)

# Check the answer and give feedback
if st.button("Submit Answer"):
    if selected_vowel == correct_vowel:
        st.success("Correct!")
    else:
        st.error("Try again")

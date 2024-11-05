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

# Categories of vowels
monophthongs = ['/i/', '/ɪ/', '/ɛ/', '/æ/', '/u/', '/ʊ/', '/ɔ/', '/ə/', '/ʌ/', '/ɑ/']
diphthongs = ['/eɪ/', '/oʊ/', '/ɔɪ/', '/aɪ/', '/aʊ/']
rhotic = ['/ɜ˞/', '/ɚ/']

# Function to generate audio for the given word
def generate_audio(word):
    tts = gTTS(text=word, lang='en', tld='us')  # American English accent
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

# Main app
st.title("👄 Vowel Sound Practice App")

# Initialize session state variables if not already set
if "current_word" not in st.session_state or "correct_vowel" not in st.session_state:
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.trials = 0

# Arrange 'Start' and 'Next Word' buttons in one row and add color styling
col1, col2, col3 = st.columns([1, 1, 3])
with col1:
    start_clicked = st.button("⛳ Start", key="start", help="Reset score and start over")
with col2:
    next_word_clicked = st.button("▶️ Next Word", key="next", help="Get a new word")

# Reset score and trials when "Start" is clicked
if start_clicked:
    st.session_state.score = 0
    st.session_state.trials = 0
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))
    st.session_state.selected_vowel = None
    st.session_state.monophthong = ""
    st.session_state.diphthong = ""
    st.session_state.rhotic = ""

# Select a new word when "Next Word" is clicked
if next_word_clicked:
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))
    st.session_state.selected_vowel = None
    st.session_state.monophthong = ""
    st.session_state.diphthong = ""
    st.session_state.rhotic = ""

# Display the audio player
st.write("Listen to the word:")
audio_buffer = generate_audio(st.session_state.current_word)
st.audio(audio_buffer, format="audio/mp3")

# Horizontal arrangement for vowel categories
st.write("Choose the vowel sound for the word you heard:")

col1, col2, col3 = st.columns(3)

# Dropdowns for vowel selection with keys for session state
with col1:
    selected_monophthong = st.selectbox("Monophthongs", [""] + monophthongs, key="monophthong")
with col2:
    selected_diphthong = st.selectbox("Diphthongs", [""] + diphthongs, key="diphthong")
with col3:
    selected_rhotic = st.selectbox("Rhotic Vowels", [""] + rhotic, key="rhotic")

# Submit button
if st.button("✅ Submit"):
    # Check which vowel is selected
    selected_vowel = selected_monophthong or selected_diphthong or selected_rhotic
    if selected_vowel == st.session_state.correct_vowel:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error("Try again.")
    
    st.session_state.trials += 1
    st.write(f"Score: {st.session_state.score} out of {st.session_state.trials}")

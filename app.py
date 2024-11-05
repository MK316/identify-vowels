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

# CSS for custom button colors
st.markdown("""
    <style>
    .start-btn, .next-btn, .submit-btn {
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin: 5px;
    }
    .start-btn { background-color: #4CAF50; } /* Green */
    .next-btn { background-color: #FF5722; }  /* Orange */
    .submit-btn { background-color: #2196F3; } /* Blue */
    </style>
""", unsafe_allow_html=True)

# Main app
st.title("Vowel Sound Practice App")

# Initialize session state variables if not already set
if "current_word" not in st.session_state or "correct_vowel" not in st.session_state:
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.trials = 0

# HTML buttons with JavaScript to click the actual Streamlit buttons
st.markdown("""
    <div class="button-container">
        <button class="start-btn" onclick="document.getElementById('start').click();">Start</button>
        <button class="next-btn" onclick="document.getElementById('next').click();">Next Word</button>
    </div>
""", unsafe_allow_html=True)

# Hidden Streamlit buttons triggered by JavaScript
start_button = st.button("Start", key="start")
next_button = st.button("Next Word", key="next")

# Reset score and trials when "Start" is clicked
if start_button:
    st.session_state.score = 0
    st.session_state.trials = 0
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))
    st.session_state.selected_vowel = None
    st.session_state.monophthong = ""
    st.session_state.diphthong = ""
    st.session_state.rhotic = ""

# Select a new word when "Next Word" is clicked
if next_button:
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

# HTML Submit button
st.markdown("""
    <button class="submit-btn" onclick="document.getElementById('submit').click();">Submit</button>
""", unsafe_allow_html=True)

# Hidden Submit button to capture clicks from the HTML button
submit_button = st.button("Submit", key="submit")

# Check and display feedback
if submit_button:
    selected_vowel = selected_monophthong or selected_diphthong or selected_rhotic
    if selected_vowel == st.session_state.correct_vowel:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error("Try again.")
    
    st.session_state.trials += 1
    st.write(f"Score: {st.session_state.score} out of {st.session_state.trials}")

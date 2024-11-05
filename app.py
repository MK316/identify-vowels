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
st.title("Vowel Sound Practice App")

# Initialize session state variables if not already set
if "current_word" not in st.session_state:
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))
if "correct_count" not in st.session_state:
    st.session_state.correct_count = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "answered" not in st.session_state:
    st.session_state.answered = False

# Reset the game when "Start" is clicked
if st.button("Start"):
    st.session_state.correct_count = 0
    st.session_state.attempts = 0
    st.session_state.answered = False
    # Choose the first random word
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))

# Place "Next Word" button and audio player in a row
next_word_col, audio_col = st.columns([1, 3])

with next_word_col:
    if st.button("Next Word"):
        # Choose a new random word, reset selections, and reset answered status
        st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))
        st.session_state.answered = False
        st.session_state.monophthong = ""
        st.session_state.diphthong = ""
        st.session_state.rhotic = ""

with audio_col:
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
if st.button("Submit"):
    if not st.session_state.answered:  # Only allow scoring if the current word hasn't been answered yet
        # Check which vowel is selected
        selected_vowel = selected_monophthong or selected_diphthong or selected_rhotic
        st.session_state.attempts += 1  # Increment attempts for each submission
        if selected_vowel == st.session_state.correct_vowel:
            st.session_state.correct_count += 1  # Increment correct count if the answer is correct
            st.success("Correct!")
        else:
            st.error("Try again.")
        
        # Mark the current word as answered
        st.session_state.answered = True

    # Display the score
    st.write(f"Score: {st.session_state.correct_count} out of {st.session_state.attempts}")

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

# Apply custom CSS to adjust button width
st.markdown(
    """
    <style>
    .stButton button {
        width: 60px;
        margin: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main app
st.title("Vowel Sound Practice App")

# Choose a random word from the dictionary if not already chosen or after "Next Word" is clicked
if "current_word" not in st.session_state or st.button("Next Word", key="next_word_button"):
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))

# Display the audio player
st.write("Listen to the word:")
audio_buffer = generate_audio(st.session_state.current_word)
st.audio(audio_buffer, format="audio/mp3")

# Display vowel options in a single row with unique keys for each button
st.write("Choose the vowel sound for the word you heard:")
vowel_options = ['/i/', '/ɪ/', '/ɛ/', '/æ/', '/u/', '/ʊ/', '/ɔ/', '/ə/', '/ʌ/', '/ɑ/', '/eɪ/', '/oʊ/', '/ɔɪ/', '/aɪ/', '/aʊ/', '/ɜ˞/', '/ɚ/']
selected_vowel = None

# Use columns to display the buttons in a row
cols = st.columns(len(vowel_options))
for i, vowel in enumerate(vowel_options):
    with cols[i]:
        if st.button(vowel, key=f"vowel_{vowel}"):
            st.session_state.selected_vowel = vowel

# Feedback mechanism
col_submit, col_next = st.columns([1, 1])
with col_submit:
    if st.button("Submit", key="submit_button"):
        if "selected_vowel" in st.session_state:
            if st.session_state.selected_vowel == st.session_state.correct_vowel:
                st.success("Correct!")
            else:
                st.error("Try again.")

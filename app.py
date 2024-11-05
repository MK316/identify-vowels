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
if "current_word" not in st.session_state or st.button("Next Word"):
    st.session_state.current_word, st.session_state.correct_vowel = random.choice(list(word_dict.items()))

# Display the audio player
st.write("Listen to the word:")
audio_buffer = generate_audio(st.session_state.current_word)
st.audio(audio_buffer, format="audio/mp3")

# Display vowel options in three rows
st.write("Choose the vowel sound for the word you heard:")
vowel_options_row1 = ['/i/', '/ɪ/', '/ɛ/', '/æ/', '/u/']
vowel_options_row2 = ['/ʊ/', '/ɔ/', '/ə/', '/ʌ/', '/ɑ/']
vowel_options_row3 = ['/eɪ/', '/oʊ/', '/ɔɪ/', '/aɪ/', '/aʊ/', '/ɜ˞/', '/ɚ/']

# Create three columns for the three rows of options
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button(vowel_options_row1[0]):
        st.session_state.selected_vowel = vowel_options_row1[0]
    if st.button(vowel_options_row2[0]):
        st.session_state.selected_vowel = vowel_options_row2[0]
    if st.button(vowel_options_row3[0]):
        st.session_state.selected_vowel = vowel_options_row3[0]
with col2:
    if st.button(vowel_options_row1[1]):
        st.session_state.selected_vowel = vowel_options_row1[1]
    if st.button(vowel_options_row2[1]):
        st.session_state.selected_vowel = vowel_options_row2[1]
    if st.button(vowel_options_row3[1]):
        st.session_state.selected_vowel = vowel_options_row3[1]
with col3:
    if st.button(vowel_options_row1[2]):
        st.session_state.selected_vowel = vowel_options_row1[2]
    if st.button(vowel_options_row2[2]):
        st.session_state.selected_vowel = vowel_options_row2[2]
    if st.button(vowel_options_row3[2]):
        st.session_state.selected_vowel = vowel_options_row3[2]
with col4:
    if st.button(vowel_options_row1[3]):
        st.session_state.selected_vowel = vowel_options_row1[3]
    if st.button(vowel_options_row2[3]):
        st.session_state.selected_vowel = vowel_options_row2[3]
    if st.button(vowel_options_row3[3]):
        st.session_state.selected_vowel = vowel_options_row3[3]
with col5:
    if st.button(vowel_options_row1[4]):
        st.session_state.selected_vowel = vowel_options_row1[4]
    if st.button(vowel_options_row2[4]):
        st.session_state.selected_vowel = vowel_options_row2[4]

# Display feedback and allow user to continue
col_submit, col_next = st.columns(2)
with col_submit:
    if st.button("Submit"):
        if "selected_vowel" in st.session_state:
            if st.session_state.selected_vowel == st.session_state.correct_vowel:
                st.success("Correct!")
            else:
                st.error("Try again.")

with col_next:
    st.button("Next Word")

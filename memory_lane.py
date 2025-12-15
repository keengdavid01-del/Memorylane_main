import streamlit as st

st.set_page_config(page_title="Memory Lane ❤️", page_icon="❤️")

if "page" not in st.session_state:
    st.session_state.page = "login"
if "music_started" not in st.session_state:
    st.session_state.music_started = False

def start_music(file):
    st.audio(file, format="audio/mp3", start_time=0)

if st.session_state.page == "login":
    st.markdown("<h1>Memory Lane ❤️</h1>", unsafe_allow_html=True)
    name = st.text_input("What is your name?")
    date = st.text_input("What is our date?")
    if st.button("Enter 💖", key="enter"):
        if name.upper() == "MONKLET" and date == "26":
            st.session_state.page = "page1"
            st.session_state.music_started = True
            st.rerun()
        else:
            st.error("Access denied 😭")

if st.session_state.music_started:
    if st.session_state.page == "page1":
        start_music("chapter1.mp3")
    elif st.session_state.page == "page2":
        start_music("chapter2.mp3")
    elif st.session_state.page == "page3":
        start_music("chapter3.mp3")
    elif st.session_state.page == "page4":
        start_music("chapter4.mp3")

# Pages
if st.session_state.page == "page1":
    st.header("Chapter One 💕")
    st.markdown("Chapter 1 text here")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back", key="back1"):
            st.session_state.page = "login"
            st.rerun()
    with col2:
        if st.button("Next ➡️", key="next1"):
            st.session_state.page = "page2"
            st.rerun()

elif st.session_state.page == "page2":
    st.header("Chapter Two 💖")
    st.markdown("Chapter 2 text here")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back", key="back2"):
            st.session_state.page = "page1"
            st.rerun()
    with col2:
        if st.button("Next ➡️", key="next2"):
            st.session_state.page = "page3"
            st.rerun()

elif st.session_state.page == "page3":
    st.header("Chapter Three ❤️")
    st.markdown("Chapter 3 text here")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back", key="back3"):
            st.session_state.page = "page2"
            st.rerun()
    with col2:
        if st.button("Next ➡️", key="next3"):
            st.session_state.page = "page4"
            st.rerun()

elif st.session_state.page == "page4":
    st.header("Chapter Four 💘")
    st.markdown("Chapter 4 text here")
    if st.button("⬅️ Back to Chapter Three", key="back4"):
        st.session_state.page = "page3"
        st.rerun()

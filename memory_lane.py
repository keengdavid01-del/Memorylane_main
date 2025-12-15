import streamlit as st

st.set_page_config(page_title="Memory Lane ❤️", page_icon="❤️")

if "page" not in st.session_state:
    st.session_state.page = "login"
if "music_started" not in st.session_state:
    st.session_state.music_started = False

def play_music(file):
    st.markdown(f"""
    <audio id="bgmusic" src="{file}" type="audio/mp3" autoplay loop></audio>
    <script>
    const audio = document.getElementById("bgmusic");
    audio.volume = 0.5;
    audio.play();
    </script>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
body { background-color: #fff0f5; }
h1, h2 { color: #ff4d6d; text-align: center; }
.long-text { font-size: 18px; line-height: 1.7; background: rgba(255,255,255,0.6); padding: 20px; border-radius: 15px; margin-bottom: 20px; }
.fade-in { animation: fadeIn 2s ease-in; }
.button-clickme { background-color: #ff4d6d; color: white; border: none; padding: 10px 25px; border-radius: 20px; font-size: 18px; cursor: pointer; }
.button-clickme:hover { background-color: #ff80a0; }
@keyframes fadeIn { from {opacity:0; transform:translateY(10px);} to {opacity:1; transform:translateY(0);} }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="position:fixed; bottom:10px; right:10px; font-size:30px;">
💖 💕 ❤️ 💘 💞
</div>
""", unsafe_allow_html=True)

if st.session_state.page == "login":
    st.markdown("<h1>Memory Lane ❤️</h1>", unsafe_allow_html=True)
    name = st.text_input("What is your name?")
    date = st.text_input("What is our date?")

    if st.button("Enter 💖", key="enter"):
        if name.upper() == "MONKLET" and date == "26":
            st.session_state.page = "page1"
            st.rerun()
        else:
            st.error("Access denied 😭")

if not st.session_state.music_started and st.session_state.page != "login":
    if st.button("Click Me 🎵", key="clickme"):
        st.session_state.music_started = True
        st.rerun()

if st.session_state.music_started:
    if st.session_state.page == "page1":
        play_music("chapter1.mp3")
    elif st.session_state.page == "page2":
        play_music("chapter2.mp3")
    elif st.session_state.page == "page3":
        play_music("chapter3.mp3")
    elif st.session_state.page == "page4":
        play_music("chapter4.mp3")

# Example Page 1 content
if st.session_state.page == "page1":
    st.header("Chapter One 💕")
    st.markdown("""
    <div class="long-text fade-in">
    It's been a month with you, baby, and honestly, I write this message to you with tears of joy in my eyes...
    </div>
    """, unsafe_allow_html=True)
    st.image("page1_pic1.jpg")
    st.image("page1_pic2.jpg")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back", key="back1"):
            st.session_state.page = "login"
            st.rerun()
    with col2:
        if st.button("Next ➡️", key="next1"):
            st.session_state.page = "page2"
            st.rerun()

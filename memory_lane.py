import streamlit as st

st.set_page_config(page_title="Memory Lane ❤️", page_icon="❤️")

def play_music(file):
    st.markdown(f"""
    <style>
    audio {{
        display: none;
    }}
    </style>
    <audio autoplay loop>
        <source src="{file}.mp3" type="audio/mp3">
    </audio>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
body {
    background-color: #fff0f5;
}
h1, h2 {
    color: #ff4d6d;
    text-align: center;
}
.long-text {
    font-size: 18px;
    line-height: 1.7;
    background: rgba(255, 255, 255, 0.6);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}
.fade-in {
    animation: fadeIn 2s ease-in;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="position:fixed; bottom:10px; right:10px; font-size:30px;">
💖 💕 ❤️ 💘 💞
</div>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "login"

if st.session_state.page == "login":
    play_music("login")

    st.markdown("<h1>Memory Lane ❤️</h1>", unsafe_allow_html=True)

    name = st.text_input("What is your name?")
    date = st.text_input("What is our date?")

    if st.button("Enter 💖", key="enter"):
        if name.upper() == "MONKLET" and date == "26":
            st.session_state.page = "page1"
            st.rerun()
        else:
            st.error("Access denied 😭")

elif st.session_state.page == "page1":
    play_music("chapter1")

    st.header("Chapter One 💕")

    st.markdown("""
    <div class="long-text fade-in">
    It's been a month with you, baby, and honestly, I write this message to you with tears of joy in my eyes. My life has taken a very visible turn since you came into my life, since you said the words that made my year: ‘I would be your girlfriend.’ From that moment, my heart has known a peace and happiness it never felt before. Every day with you feels like a beautiful part of a love story I never want to end. You’ve touched my soul in ways words can’t fully express, and I find myself falling deeper for you with every smile, every laugh, and every moment we share. One month may seem like a short period of time, but to me, it’s the start of something endless, something that feels like forever.
    Sometimes I fear how deeply I fell for you because it makes me realize how much you mean to me, how much I never want to lose this. But that’s also what makes this love so real, so genuine. I love you more than I can put into words, baby, and I’m so thankful I get to call you mine.
    No matter where life takes us, one thing will never change — I’ll keep choosing you, over and over again.
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

elif st.session_state.page == "page2":
    play_music("chapter2")

    st.header("Chapter Two 💖")

    st.markdown("""
    <div class="long-text fade-in">
    Honestly, these past months have been extremely amazing, literally the best year of my life already. You’ve made me the happiest person alive. I know we’ve had one or two down moments, but the beautiful ones outweigh them. A little recap to the first time we met physically — 10th May 2025. That very day, I felt it in my heart that you were the one. You’re such an amazing soul.
    It wasn’t an easy task getting you to say yes, but I can proudly say you were and are very worth the difficulty. Like they say, good things don’t come easy. I always say “Michelle is my blessing from God.” You may think I’m exaggerating, but I’m not.
    I love you beyond measure, beyond human comprehension, and honestly, you’re the best girlfriend in the world. I love you sooooo veryyyy muchhhh, baby.
    </div>
    """, unsafe_allow_html=True)

    st.image("page2_pic1.jpg")
    st.image("page2_pic2.jpg")

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
    play_music("chapter3")

    st.header("Chapter Three ❤️")

    st.markdown("""
    <div class="long-text fade-in">
    There are so many things I could say to you, but even the most beautiful words sometimes feel too small to hold the way I feel. I'm endlessly grateful to have you in my life. You're more than just my girlfriend — you're my safe place, my peace, and my spark. I wouldn't trade you for anything in this world.
    Every moment we've shared means everything to me. The laughter, the deep talks, the quiet glances, especially those times I look into your eyes and get completely lost, like no map could ever find me. You bring out the child in me, the carefree, joyful side I thought I had buried. You've reminded me how it feels to truly live in a moment.
    </div>
    """, unsafe_allow_html=True)

    st.image("page3_pic1.jpg")
    st.image("page3_pic2.jpg")

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
    play_music("chapter4")

    st.header("Chapter Four 💘")

    st.markdown("""
    <div class="long-text fade-in">
    Now those were all recaps of the moments and messages we've shared. It’s been a beautiful time we've spent together, and honestly, I wouldn’t trade it for anything. It’s been 152.08 days, 21.726 weeks, 3650.004 hours, 13,140,014.4 seconds, 13,140,014,400 milliseconds spent officially as your boyfriend and even more unofficially.
    It’s been an amazing time, a lot of beautiful memories we’ve made together, and I love you sooooo muchhhh, baby.
    </div>
    """, unsafe_allow_html=True)

    st.image("page4_pic1.jpg")
    st.image("page4_pic2.jpg")

    if st.button("⬅️ Back to Chapter Three", key="back4"):
        st.session_state.page = "page3"
        st.rerun()

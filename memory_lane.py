import streamlit as st
import random
import base64

st.set_page_config(page_title="Memory Lane ❤️", page_icon="❤️")

if "page" not in st.session_state:
    st.session_state.page = "login"

colors = ["#ff4d6d","#ff80a0","#ffb3c6","#ffccd9"]

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffe6f0, #ffccd9);
    background-attachment: fixed;
}
h1, h2, h3, h4, h5, h6 {
    color: #fff;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
}
.long-text { 
    font-size: 18px; 
    line-height: 1.7; 
    background: rgba(0,0,0,0.85); 
    color: #fff; 
    padding: 25px; 
    border-radius: 20px; 
    margin-bottom: 20px; 
}
.stTextInput>div>input {
    background: rgba(0,0,0,0.85);
    color: #fff;
    border-radius: 12px;
}
.stButton>button {
    background-color: #ff4d6d;
    color: #fff;
    border-radius: 15px;
    font-weight: bold;
}
.fade-in {
    animation: fadeIn 2s ease-in;
}
@keyframes fadeIn {
    from {opacity:0; transform:translateY(10px);}
    to {opacity:1; transform:translateY(0);}
}
.polaroid {
    width: 300px;
    padding: 10px;
    background: white;
    box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
    border-radius: 10px;
    margin-bottom: 20px;
}
.question-bubble {
    background: rgba(0,0,0,0.85);
    color: white;
    padding: 10px 14px;
    border-radius: 12px;
    margin-bottom: 6px;
    display: inline-block;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

def show_polaroid(img):
    with open(img,"rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f'<img src="data:image/jpeg;base64,{data}" class="polaroid">', unsafe_allow_html=True)

if st.session_state.page == "login":
    st.markdown("<h1>Memory Lane ❤️</h1>", unsafe_allow_html=True)

    st.markdown('<div class="question-bubble">What is your name?</div>', unsafe_allow_html=True)
    name = st.text_input("", label_visibility="collapsed")

    st.markdown('<div class="question-bubble">What is our date?</div>', unsafe_allow_html=True)
    date = st.text_input("", label_visibility="collapsed")

    if st.button("Enter 💖"):
        if name.upper() == "MONKLET" and date == "26":
            st.session_state.page = "page1"
            st.rerun()
        else:
            st.error("Access denied 😭")

elif st.session_state.page == "page1":
    st.header("Chapter One 💕")
    st.markdown("""
    <div class="long-text fade-in">
    It's been a month with you baby and honestly I write this message to you with tears of joy in my eyes. My life has taken a very visible turn since you came into my life since you said the words that made my year I would be your girlfriend. From that moment my heart has known a peace and happiness it never felt before. Every day with you feels like a beautiful part of a love story I never want to end. You’ve touched my soul in ways words can’t fully express and I find myself falling deeper for you with every smile every laugh and every moment we share.
    </div>
    """, unsafe_allow_html=True)
    show_polaroid("page1_pic1.jpg")
    show_polaroid("page1_pic2.jpg")

    if st.button("Next ➡️"):
        st.session_state.page = "page2"
        st.rerun()

elif st.session_state.page == "page2":
    st.header("Chapter Two 💖")
    st.markdown("""
    <div class="long-text fade-in">
    Honestly these past months have been extremely amazing literally the best year of my life already. You’ve made me the happiest person alive. That very day I felt it in my heart that you were the one. You’re such an amazing soul.
    </div>
    """, unsafe_allow_html=True)
    show_polaroid("page2_pic1.jpg")
    show_polaroid("page2_pic2.jpg")

    if st.button("Next ➡️"):
        st.session_state.page = "page3"
        st.rerun()

elif st.session_state.page == "page3":
    st.header("Chapter Three ❤️")
    st.markdown("""
    <div class="long-text fade-in">
    There are so many things I could say to you but even the most beautiful words sometimes feel too small to hold the way I feel. You're my safe place my peace and my spark.
    </div>
    """, unsafe_allow_html=True)
    show_polaroid("page3_pic1.jpg")
    show_polaroid("page3_pic2.jpg")

    if st.button("Next ➡️"):
        st.session_state.page = "page4"
        st.rerun()

elif st.session_state.page == "page4":
    st.header("Chapter Four 💘")
    st.markdown("""
    <div class="long-text fade-in">
    It’s been a beautiful time we've spent together and honestly I wouldn’t trade it for anything. I love you sooooo muchhhh baby.
    </div>
    """, unsafe_allow_html=True)
    show_polaroid("page4_pic1.jpg")
    show_polaroid("page4_pic2.jpg")

    if st.button("Take the Memory Quiz 💌"):
        st.session_state.page = "quiz"
        st.rerun()

elif st.session_state.page == "quiz":
    st.header("Memory Quiz 💖")

    st.markdown('<div class="question-bubble">1) Where did you say yes to being my girlfriend?</div>', unsafe_allow_html=True)
    q1 = st.text_input("", label_visibility="collapsed")

    st.markdown('<div class="question-bubble">2) What was the day and month?</div>', unsafe_allow_html=True)
    q2 = st.text_input("", label_visibility="collapsed")

    st.markdown('<div class="question-bubble">3) What is my nickname for you?</div>', unsafe_allow_html=True)
    q3 = st.text_input("", label_visibility="collapsed")

    st.markdown('<div class="question-bubble">4) What is your nickname for me?</div>', unsafe_allow_html=True)
    q4 = st.text_input("", label_visibility="collapsed")

    if st.button("Submit Answers"):
        if (
            q1.strip().lower() == "jabi lake mall" and
            q2.strip().lower() in ["july 26","26 july"] and
            q3.strip().lower() == "monklet" and
            q4.strip().lower() == "hubby"
        ):
            st.balloons()
            st.success("All answers correct 💖")
        else:
            st.error("Try again baby 💕")

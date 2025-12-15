import streamlit as st
import base64

st.set_page_config(page_title="Memory Lane ❤️", page_icon="❤️")

if "page" not in st.session_state:
    st.session_state.page = "login"

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffe6f0, #ffccd9);
}
h1, h2 {
    color: #fff;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
}
.long-text {
    font-size: 18px;
    line-height: 1.7;
    background: rgba(0,0,0,0.85);
    color: white;
    padding: 25px;
    border-radius: 20px;
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
.stTextInput>div>input {
    background: rgba(0,0,0,0.85);
    color: white;
    border-radius: 12px;
}
.stButton>button {
    background-color: #ff4d6d;
    color: white;
    border-radius: 15px;
    font-weight: bold;
}
.polaroid {
    width: 300px;
    padding: 10px;
    background: white;
    box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
    border-radius: 10px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

def show_polaroid(img):
    with open(img, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f'<img src="data:image/jpeg;base64,{data}" class="polaroid">', unsafe_allow_html=True)

if st.session_state.page == "login":
    st.markdown("<h1>Memory Lane ❤️</h1>", unsafe_allow_html=True)

    st.markdown('<div class="question-bubble">What is your name?</div>', unsafe_allow_html=True)
    name = st.text_input("", key="login_name", label_visibility="collapsed")

    st.markdown('<div class="question-bubble">What is our date?</div>', unsafe_allow_html=True)
    date = st.text_input("", key="login_date", label_visibility="collapsed")

    if st.button("Enter 💖"):
        if name.upper() == "MONKLET" and date == "26":
            st.session_state.page = "page1"
            st.rerun()
        else:
            st.error("Access denied 😭")

elif st.session_state.page == "page1":
    st.header("Chapter One 💕")
    st.markdown("""
    <div class="long-text">
    It's been a month with you baby and honestly I write this message to you with tears of joy in my eyes. My life has taken a very visible turn since you came into my life since you said the words that made my year I would be your girlfriend. From that moment my heart has known a peace and happiness it never felt before. Every day with you feels like a beautiful part of a love story I never want to end. You’ve touched my soul in ways words can’t fully express and I find myself falling deeper for you with every smile every laugh and every moment we share. One month may seem like a short period of time but to me it’s the start of something endless something that feels like forever.
    Sometimes I fear how deeply I fell for you because it makes me realize how much you mean to me how much I never want to lose this. But that’s also what makes this love so real so genuine. I love you more than I can put into words baby and I’m so thankful I get to call you mine.
    No matter where life takes us one thing will never change I’ll keep choosing you over and over again.
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
    <div class="long-text">
    Honestly these past months have been extremely amazing literally the best year of my life already. You’ve made me the happiest person alive. I know we’ve had one or two down moments but the beautiful ones outweigh them. A little recap to the first time we met physically 10th May 2025. That very day I felt it in my heart that you were the one. You’re such an amazing soul.
    It wasn’t an easy task getting you to say yes but I can proudly say you were and are very worth the difficulty. Like they say good things don’t come easy. I always say Michelle is my blessing from God. You may think I’m exaggerating but I’m not.
    I love you beyond measure beyond human comprehension and honestly you’re the best girlfriend in the world. I love you sooooo veryyyy muchhhh baby.
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
    <div class="long-text">
    There are so many things I could say to you but even the most beautiful words sometimes feel too small to hold the way I feel. I'm endlessly grateful to have you in my life. You're more than just my girlfriend you're my safe place my peace and my spark. I wouldn't trade you for anything in this world.
    Every moment we've shared means everything to me. The laughter the deep talks the quiet glances especially those times I look into your eyes and get completely lost like no map could ever find me. You bring out the child in me the carefree joyful side I thought I had buried. You've reminded me how it feels to truly live in a moment.
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
    <div class="long-text">
    Now those were all recaps of the moments and messages we've shared. It’s been a beautiful time we've spent together and honestly I wouldn’t trade it for anything. It’s been 152.08 days 21.726 weeks 3650.004 hours 13,140,014.4 seconds 13,140,014,400 milliseconds spent officially as your boyfriend and even more unofficially.
    It’s been an amazing time a lot of beautiful memories we’ve made together and I love you sooooo muchhhh baby.
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
    q1 = st.text_input("", key="q1", label_visibility="collapsed")

    st.markdown('<div class="question-bubble">2) What was the day and month?</div>', unsafe_allow_html=True)
    q2 = st.text_input("", key="q2", label_visibility="collapsed")

    st.markdown('<div class="question-bubble">3) What is my nickname for you?</div>', unsafe_allow_html=True)
    q3 = st.text_input("", key="q3", label_visibility="collapsed")

    st.markdown('<div class="question-bubble">4) What is your nickname for me?</div>', unsafe_allow_html=True)
    q4 = st.text_input("", key="q4", label_visibility="collapsed")

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

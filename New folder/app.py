import streamlit as st
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="A Secret for You ❤️", page_icon="🔒")

# --- CUSTOM CSS FOR FLASHING & HEART ANIMATION ---
st.markdown("""
    <style>
    /* Flashing Animation */
    @keyframes flash {
        0% { opacity: 1; color: #ff0000; }
        50% { opacity: 0.2; color: #b91d47; }
        100% { opacity: 1; color: #ff0000; }
    }
    .flashing-text {
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 32px;
        font-weight: bold;
        animation: flash 1s infinite;
        margin-bottom: 20px;
    }

    /* Heart Rain Animation */
    @keyframes hearts {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .heart {
        position: fixed;
        top: -10%;
        color: #ff4d6d;
        font-size: 24px;
        user-select: none;
        z-index: 1000;
        animation: hearts 4s linear infinite;
    }

    .stApp {
        background: linear-gradient(to bottom, #ffafbd, #ffc3a0);
    }
    
    .main-text {
        color: #b91d47;
        font-family: 'Georgia', serif;
        text-align: center;
    }
    
    div.stButton > button {
        border-radius: 30px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0

# --- PAGE 1: THE SECRET LANDING PAGE ---
if st.session_state.page == 'landing':
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="flashing-text">Baby Click here if you are alone!! 🤫🫦✨</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("CLICK HERE ❤️", use_container_width=True):
            st.session_state.page = 'valentine'
            st.rerun()

# --- PAGE 2: THE VALENTINE QUESTION ---
elif st.session_state.page == 'valentine':
    st.markdown("<h1 class='main-text'>Will you be my Valentine? ❤️</h1>", unsafe_allow_html=True)
    
    img_number = (st.session_state.no_count % 3) + 1
    img_path = f"sad{img_number}.jpg"
    
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    else:
        st.warning(f"Make sure '{img_path}' is in your 'New Folder'!")

    col_yes, col_no = st.columns([1 + (st.session_state.no_count * 0.4), 1])
    
    with col_yes:
        if st.button("YES! 😍", use_container_width=True):
            st.session_state.page = 'success'
            st.rerun()

    with col_no:
        no_labels = ["No", "Are you sure? 🥺", "Really? 😭", "Don't do this...", "You're my Evangeline! ✨"]
        current_no = no_labels[min(st.session_state.no_count, len(no_labels)-1)]
        if st.button(current_no, use_container_width=True):
            st.session_state.no_count += 1
            st.rerun()

# --- PAGE 3: THE FINALE ---
else:
    # Generate Heart Rain using HTML
    heart_html = "".join([f'<div class="heart" style="left:{i*10}%; animation-delay:{i*0.5}s;">❤️</div>' for i in range(10)])
    st.markdown(heart_html, unsafe_allow_html=True)
    
    st.balloons() # Balloons float UP
    
    st.markdown("""
        <style>
        .stApp { background: linear-gradient(to bottom, #0b3d1f, #1e5631) !important; }
        .finale-text { color: white; text-align: center; font-family: 'Garamond', serif; }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='finale-text'>I knew you'd say yes! 👑🐸</h1>", unsafe_allow_html=True)
    
    if os.path.exists("tiana_naveen.jpg"):
        st.image("tiana_naveen.jpg", use_container_width=True)
    
    st.markdown("""
        <div class='finale-text'>
            <br>
            <h2>“My dream wouldn't be complete without you in it.”</h2>
            <p style='font-size: 22px;'>I love you more than Ray loves Evangeline!</p>
            <p style='font-size: 18px;'>Can't wait to see you on Valentine's Day. ❤️</p>
        </div>
    """, unsafe_allow_html=True)
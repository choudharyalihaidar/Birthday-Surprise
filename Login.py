import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday Surprise ",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS with Right.png as Full Background Wallpaper
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;600;700&display=swap');

    /* Hide Streamlit Default Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Set Right.png as Background Wallpaper */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.35)), url("app/static/Right.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
    }

    /* Fallback if static folder path needs direct local handling */
    .stApp {
        background-color: #fce4ec;
    }

    /* Step Badge Styling */
    .step-badge {
        display: inline-block;
        background: #102542;
        color: #f6ca7d;
        padding: 6px 20px;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 2px;
        margin-bottom: 14px;
        border: 1px solid #d4af37;
        box-shadow: 0 4px 12px rgba(16, 37, 66, 0.35);
    }

    /* Main Card - Warm Champagne Gold Contrast */
    .glass-card {
        background: linear-gradient(145deg, rgba(255, 248, 235, 0.95), rgba(245, 230, 200, 0.95));
        border: 2.5px solid #d4af37;
        border-radius: 28px;
        padding: 38px 28px;
        text-align: center;
        box-shadow: 0 18px 40px rgba(0, 0, 0, 0.45), inset 0 0 25px rgba(212, 175, 55, 0.18);
        animation: fadeIn 0.7s ease-in-out;
        margin-bottom: 15px;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .script-heading {
        font-family: 'Great Vibes', cursive;
        font-size: 3.6rem;
        color: #102542 !important;
        font-weight: 700;
        margin: 0px 0 5px 0;
        line-height: 1.2;
        text-shadow: 1px 1px 2px rgba(212, 175, 55, 0.35);
    }

    .sub-heading {
        font-family: 'Great Vibes', cursive;
        font-size: 2.3rem;
        color: #8a5a00 !important;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .body-text {
        color: #1f3652;
        font-size: 1.05rem;
        font-weight: 500;
        line-height: 1.7;
        margin-bottom: 10px;
    }

    /* Vintage Antique Card (Final Step) */
    .antique-card {
        background: linear-gradient(145deg, #f7ebd2, #e5cfa3);
        border: 4px double #102542;
        border-radius: 18px;
        padding: 35px 25px;
        color: #102542;
        box-shadow: inset 0 0 30px rgba(138, 90, 0, 0.2), 0 15px 30px rgba(0,0,0,0.45);
        text-align: center;
        position: relative;
    }

    /* Custom Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #1b365d 0%, #27496d 100%);
        color: #fff8e7 !important;
        border: 1.5px solid #d4af37;
        border-radius: 50px;
        padding: 12px 28px;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.35);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 22px rgba(212, 175, 55, 0.45);
        border-color: #fff8eb;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Set Background Image directly via CSS injection with base64/local file check
def set_bg_local(image_file):
  if Path(image_file).exists():
    with open(image_file, "rb") as f:
      data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)), url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """
    st.markdown(css, unsafe_allow_html=True)


set_bg_local("Right.png")

# Initialize Session State
if "step" not in st.session_state:
  st.session_state.step = 1

# Top Progress Indicator (Out of 4 steps)
st.progress(st.session_state.step / 4)

# ==========================================
# STEP 1: WELCOME SCREEN
# ==========================================
if st.session_state.step == 1:
  st.markdown(
      """
        <div class="glass-card">
            <span class="step-badge">WELCOME</span>
            <div class="script-heading">Happy Birthday to You</div>
            <div style="font-family: 'Great Vibes', cursive; font-size: 2rem; color: #102542; font-weight: 600; margin: 5px 0;">Dear My Sister</div>
            <div class="sub-heading">On Ur 15th Birthday</div>
            <p class="body-text">
                Today isn't just an ordinary day—the world became a little brighter on this exact date.<br>
                I made a small digital surprise just to put a smile on your face.
            </p>
            <p style="color: #8a5a00; font-weight: 600; font-size: 0.92rem;">Are you ready to unlock your birthday surprise?</p>
        </div>
        """,
      unsafe_allow_html=True,
  )
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    if st.button("Start Your Surprise ", use_container_width=True):
      st.session_state.step = 2
      st.rerun()

# ==========================================
# STEP 2: REAL FLYING HEARTS CATCHING GAME
# ==========================================
elif st.session_state.step == 2:
  st.markdown(
      """
        <div class="glass-card" style="padding: 25px 20px; margin-bottom: 10px;">
            <span class="step-badge">MINI GAME</span>
            <div class="script-heading" style="font-size: 2.8rem;">Catch 5 Flying Hearts</div>
            <p class="body-text" style="margin-bottom: 0;">
                Click on all <b>5 flying hearts</b> moving inside the box below to unlock your birthday wish!
            </p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  flying_game_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap');
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            font-family: 'Poppins', sans-serif;
            background: transparent;
        }
        #game-arena {
            position: relative;
            width: 100%;
            height: 330px;
            background: linear-gradient(145deg, rgba(255, 248, 235, 0.85), rgba(245, 230, 200, 0.85));
            border: 2px solid #d4af37;
            border-radius: 24px;
            box-shadow: inset 0 0 25px rgba(16, 37, 66, 0.5);
            overflow: hidden;
            user-select: none;
        }
        #score-board {
            position: absolute;
            top: 15px;
            left: 50%;
            transform: translateX(-50%);
            background: #102542;
            color: #f6ca7d;
            padding: 6px 22px;
            border-radius: 30px;
            font-size: 16px;
            font-weight: 700;
            border: 1.5px solid #d4af37;
            z-index: 10;
            box-shadow: 0 4px 12px rgba(0,0,0,0.35);
        }
        .flying-heart {
            position: absolute;
            font-size: 46px;
            cursor: pointer;
            transition: transform 0.1s ease;
            filter: drop-shadow(0 0 10px rgba(255, 105, 180, 0.85));
            z-index: 5;
        }
        .flying-heart:hover {
            transform: scale(1.25);
        }
        .pop-effect {
            position: absolute;
            color: #8a5a00;
            font-weight: bold;
            font-size: 18px;
            pointer-events: none;
            animation: floatFade 0.8s forwards;
        }
        @keyframes floatFade {
            0% { opacity: 1; transform: translateY(0) scale(1); }
            100% { opacity: 0; transform: translateY(-40px) scale(1.4); }
        }
        #win-banner {
            display: none;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: #102542;
            width: 85%;
        }
        #win-banner h2 {
            color: #8a5a00;
            margin-bottom: 8px;
            font-size: 26px;
        }
        #win-banner p {
            font-size: 15px;
            color: #1f3652;
        }
    </style>
    </head>
    <body>
        <div id="game-arena">
            <div id="score-board">Caught: <span id="count">0</span> / 5</div>
            <div id="win-banner">
                <h2> Amazing! You Caught All 5 Hearts! </h2>
                <p>Click the <b>"Next Step: Celebration 💖"</b> button below to continue!</p>
            </div>
        </div>

        <script>
            const arena = document.getElementById('game-arena');
            const countSpan = document.getElementById('count');
            const winBanner = document.getElementById('win-banner');
            let caught = 0;
            const totalHearts = 5;
            const heartIcons = ['❤️', '💖', '💘', '💕', '💓'];
            const hearts = [];

            for (let i = 0; i < totalHearts; i++) {
                const el = document.createElement('div');
                el.className = 'flying-heart';
                el.innerText = heartIcons[i % heartIcons.length];
                arena.appendChild(el);

                const obj = {
                    el: el,
                    x: Math.random() * (arena.clientWidth - 70) + 15,
                    y: Math.random() * (arena.clientHeight - 90) + 50,
                    vx: (Math.random() * 2.5 + 1.5) * (Math.random() < 0.5 ? 1 : -1),
                    vy: (Math.random() * 2.5 + 1.5) * (Math.random() < 0.5 ? 1 : -1),
                    active: true
                };

                el.addEventListener('click', function(e) {
                    if (!obj.active) return;
                    obj.active = false;
                    el.style.display = 'none';
                    caught++;
                    countSpan.innerText = caught;

                    const pop = document.createElement('div');
                    pop.className = 'pop-effect';
                    pop.innerText = 'Caught! 🎉';
                    pop.style.left = obj.x + 'px';
                    pop.style.top = obj.y + 'px';
                    arena.appendChild(pop);
                    setTimeout(() => pop.remove(), 800);

                    if (caught === totalHearts) {
                        winBanner.style.display = 'block';
                    }
                });

                hearts.push(obj);
            }

            function animate() {
                const width = arena.clientWidth;
                const height = arena.clientHeight;

                hearts.forEach(h => {
                    if (!h.active) return;
                    h.x += h.vx;
                    h.y += h.vy;

                    if (h.x <= 10 || h.x >= width - 55) h.vx *= -1;
                    if (h.y <= 45 || h.y >= height - 55) h.vy *= -1;

                    h.el.style.left = h.x + 'px';
                    h.el.style.top = h.y + 'px';
                });

                requestAnimationFrame(animate);
            }
            animate();
        </script>
    </body>
    </html>
    """

  components.html(flying_game_html, height=345)

  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    if st.button("Next Step: Celebration 💖", use_container_width=True):
      st.session_state.step = 3
      st.rerun()

# ==========================================
# STEP 3: PINK AESTHETIC TEMPLATE CARD WITH BARBIE IMAGE
# ==========================================
elif st.session_state.step == 3:
  barbie_img_path = "barbie.png"
  barbie_html_img = ""
  if Path(barbie_img_path).exists():
    with open(barbie_img_path, "rb") as img_f:
      b64_img = base64.b64encode(img_f.read()).decode()
    barbie_html_img = f'<img src="data:image/png;base64,{b64_img}" class="barbie-character">'
  else:
    barbie_html_img = '<div class="barbie-character" style="background: #ff69b4; display: flex; align-items: center; justify-content: center; font-size: 3rem;">👸</div>'

  st.markdown(
      f"""
        <style>
        .pink-aesthetic-card {{
            background: linear-gradient(135deg, #ffc0cb 0%, #ffb6c1 50%, #ff9ebb 100%);
            border: 3px solid #ff69b4;
            border-radius: 25px;
            padding: 35px 25px;
            text-align: center;
            box-shadow: 0 15px 35px rgba(255, 105, 180, 0.35);
            position: relative;
            overflow: visible;
        }}
        .pink-title {{
            font-family: 'Great Vibes', cursive;
            font-size: 3.5rem;
            color: #5c0632;
            margin: 5px 0;
            text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.6);
        }}
        .pink-badge {{
            background: rgba(255, 255, 255, 0.85);
            border: 2px solid #ff69b4;
            border-radius: 50px;
            padding: 10px 25px;
            display: inline-block;
            font-weight: 700;
            color: #5c0632;
            font-size: 1.1rem;
            margin: 10px 0;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }}
        .barbie-character {{
            position: absolute;
            right: -25px;
            top: -45px;
            width: 130px;
            height: 130px;
            border-radius: 50%;
            border: 4px solid #fff;
            box-shadow: 0 8px 20px rgba(0,0,0,0.25);
            object-fit: cover;
            background-color: #fff;
            z-index: 10;
        }
        </style>
        
        <div class="pink-aesthetic-card">
            {barbie_html_img}
            <div style="font-size: 2.2rem; margin-bottom: 5px;">💖🎈✨</div>
            <div class="pink-title">Happy Birthday</div>
            <div class="pink-badge">💕 15th Birthday 💕</div><br>
            <div class="pink-badge">💕 Wishes for you 💕</div>
            <p style="color: #5c0632; font-weight: 600; margin-top: 15px; font-size: 1.05rem;">
                May your day be filled with sweet moments, endless joy, and wonderful surprises!
            </p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  st.markdown("<br>", unsafe_allow_html=True)
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    if st.button("Read Final Keepsake Card ✨", use_container_width=True):
      st.session_state.step = 4
      st.rerun()

# ==========================================
# STEP 4: ANTIQUE KEEPSAKE CARD & PRAYER
# ==========================================
elif st.session_state.step == 4:
  st.markdown(
      """
        <div class="antique-card">
            <p style="letter-spacing: 3px; font-size: 0.85rem; font-weight: 700; color: #102542;">KEEPSAKE BIRTHDAY CARD</p>
            <h1 style="font-family: 'Great Vibes', cursive; font-size: 3.5rem; color: #102542; margin: 5px 0;">Happy 15th Birthday</h1>
            <p style="font-style: italic; color: #8a5a00; font-weight: 600; margin-bottom: 20px;">~ With love, just for you ~</p>
            <hr style="border: 0; height: 1.5px; background: #d4af37; margin: 20px auto; width: 70%;">
            <p style="font-size: 1.05rem; line-height: 1.8; max-width: 550px; margin: 0 auto;">
                "May Allah bless your life with endless happiness, good health, peace, and success. 
                May every dream in your heart come true, and may your days always be filled with love and beautiful moments. 
                You are a precious blessing, and I pray that this new chapter brings you countless reasons to smile."
            </p>
            <hr style="border: 0; height: 1.5px; background: #d4af37; margin: 25px auto; width: 40%;">
            <p style="font-weight: 700; color: #102542;">✨ Aameen · Stay Happy Always 🌟</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  st.markdown("<br>", unsafe_allow_html=True)
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    if st.button("🔄 Replay Surprise", use_container_width=True):
      st.session_state.step = 1
      st.rerun()

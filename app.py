# app.py
import streamlit as st

# -----------------------------
# Page Config (must be first Streamlit command)
# -----------------------------
st.set_page_config(
    page_title="Daniella Zacharis | Portfolio",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Minimal custom styling
# -----------------------------
# -----------------------------
# Dark Green & Gold Styling
# -----------------------------
st.markdown(
    """
    <style>
      /* Page background & spacing */
      .block-container {
        padding-top: 2rem;
        padding-bottom: 2.5rem;
      }

      /* Card styling */
      .card {
        padding: 1.2rem 1.4rem;
        border-radius: 18px;
        background: rgba(10, 61, 46, 0.85); /* deep green */
        border: 1px solid rgba(212, 175, 55, 0.35); /* gold */
        box-shadow: 0 4px 18px rgba(0,0,0,0.25);
      }

      /* Headers */
      h1, h2, h3 {
        color: #D4AF37; /* gold */
      }

      /* Muted text */
      .muted {
        opacity: 0.9;
        font-size: 0.95rem;
        color: #E6E6E6;
      }

      /* Progress bar container */
      div[data-testid="stProgress"] {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
      }

      /* Progress bar fill */
      div[data-testid="stProgress"] > div {
        background-color: #D4AF37; /* gold */
        height: 14px;
        border-radius: 8px;
      }

      /* Horizontal divider */
      hr {
        margin: 1.6rem 0;
        border: none;
        height: 1px;
        background: linear-gradient(
          to right,
          transparent,
          #D4AF37,
          transparent
        );
      }

      /* Body text */
      p, li {
        color: #F5F5F5;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header / Title
# -----------------------------
st.markdown(
    """
    <div class="card">
      <h1 style="margin-bottom: 0.2rem;">✨ Daniella Zacharis</h1>
      <div class="muted">Business Analytics & Finance • Analytics Explorer • Excel Esports Competitor 📊</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# -----------------------------
# About Me
# -----------------------------
st.markdown(
    """
    <div class="card">
      <h2 style="margin-top: 0;">👋 About Me</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write(
    "I am a Business Analytics and Finance undergraduate with a strong interest in data-driven decision making and analytical problem solving. "
    "I will begin my Master of Science in Business Analytics in Fall 2026, where I aim to further develop advanced analytical, technical, and strategic skills. "
    "My academic and professional interests center on analytics applications across a wide range of industries, with a particular focus on exploring how data can inform operational, financial, and risk-based decisions. "
    "In addition to my academic pursuits, I am an avid Microsoft Excel Esports competitor, where I apply advanced Excel techniques in fast-paced, competitive analytical environments."
)

st.write("")
st.markdown("---")

# -----------------------------
# Skills (columns + progress bars)
# -----------------------------
st.markdown(
    """
    <div class="card">
      <h2 style="margin-top: 0;">🧠 Skills</h2>
      <div class="muted">A snapshot of tools and strengths (progress bars are adjustable).</div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

skills = [
    ("📊 Microsoft Excel", 92),
    ("📈 Power BI", 82),
    ("🧮 SQL", 72),
    ("🐍 Python", 65),
    ("🧾 SAS", 70),
    ("🛡️ Risk & Analytics", 78),
]

col1, col2, col3 = st.columns(3, gap="large")
for i, (label, level) in enumerate(skills):
    target_col = [col1, col2, col3][i % 3]
    with target_col:
        st.markdown(f"**{label}**")
        st.progress(level)
        st.caption(f"{level}%")

st.write("")
st.markdown("---")

# -----------------------------
# Highlights
# -----------------------------
st.markdown(
    """
    <div class="card">
      <h2 style="margin-top: 0;">🚀 Highlights</h2>
      <div class="muted">A few areas I enjoy building and exploring.</div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

a, b = st.columns(2, gap="large")
with a:
    st.markdown("### 📌 Dashboards & Reporting")
    st.write(
        "I enjoy building clean, executive-friendly dashboards that translate performance and trends into actionable insights."
    )
with b:
    st.markdown("### 🔍 Cross-Industry Analytics")
    st.write(
        "I’m interested in applying analytics across different industries to understand how data can improve processes, decisions, and outcomes."
    )

st.write("")
st.markdown("---")

# -----------------------------
# Contact
# -----------------------------
st.markdown(
    """
    <div class="card">
      <h2 style="margin-top: 0;">📬 Contact</h2>
      <div class="muted">I’m open to opportunities, collaborations, and learning conversations.</div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

st.markdown("**📧 Email:** daniellazacharis@gmail.com")

st.write("")
st.markdown(
    """
    <div class="muted" style="text-align:center; margin-top: 1.5rem;">
      Built with Streamlit 💙
    </div>
    """,
    unsafe_allow_html=True,
)


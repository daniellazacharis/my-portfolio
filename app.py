# -*- coding: utf-8 -*-
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
# Theme Toggle State
# -----------------------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

# -----------------------------
# Theme-aware Styling (Dark/Light)
# -----------------------------
if st.session_state.dark_mode:
    bg = "#061f17"          # very dark green
    card_bg = "rgba(10, 61, 46, 0.85)"
    text = "#F5F5F5"
    muted = "#E6E6E6"
    border = "rgba(212, 175, 55, 0.35)"  # gold
    accent = "#D4AF37"      # gold
else:
    bg = "#F7F7F4"          # warm light
    card_bg = "rgba(255, 255, 255, 0.92)"
    text = "#0A3D2E"        # deep green
    muted = "#2d4a40"
    border = "rgba(10, 61, 46, 0.18)"
    accent = "#B88A1E"      # slightly deeper gold for contrast

st.markdown(
    f"""
    <style>
      /* Background */
      [data-testid="stAppViewContainer"] {{
        background: {bg};
      }}

      .block-container {{
        padding-top: 2rem;
        padding-bottom: 2.5rem;
      }}

      /* Card */
      .card {{
        padding: 1.2rem 1.4rem;
        border-radius: 18px;
        background: {card_bg};
        border: 1px solid {border};
        box-shadow: 0 4px 18px rgba(0,0,0,0.18);
      }}

      /* Text */
      h1, h2, h3, p, li, div, span {{
        color: {text};
      }}
      .muted {{
        opacity: 0.9;
        font-size: 0.95rem;
        color: {muted};
      }}

      /* Progress */
      div[data-testid="stProgress"] {{
        background-color: rgba(255, 255, 255, 0.12);
        border-radius: 8px;
      }}
      div[data-testid="stProgress"] > div {{
        background-color: {accent};
        height: 14px;
        border-radius: 8px;
      }}

      /* Divider */
      hr {{
        margin: 1.6rem 0;
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, {accent}, transparent);
      }}

      /* Links */
      a {{
        color: {accent} !important;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header with Dark Mode Toggle
# -----------------------------
left, right = st.columns([0.75, 0.25])

with left:
    st.markdown(
        """
        <div class="card">
          <h1 style="margin-bottom: 0.2rem;">Daniella Zacharis</h1>
          <div class="muted">Business Analytics & Finance • Analytics Explorer • Excel Esports Competitor</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.write("")  # small vertical spacing
    toggle_label = "Dark mode: ON" if st.session_state.dark_mode else "Dark mode: OFF"
    if st.button(toggle_label, use_container_width=True):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

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
# Skills (LinkedIn link + top-skill stars + endorsement tooltips)
# -----------------------------
st.markdown(
    """
    <div class="card">
      <div style="display:flex; align-items:center; justify-content:space-between; gap:12px;">
        <div>
          <h2 style="margin-top: 0; margin-bottom: 0.2rem;">Skills</h2>
          <div class="muted">Technical and analytical skills, supported by LinkedIn endorsements.</div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Add the emoji OUTSIDE the HTML (safe)
st.write("🧠")

st.write("")

skills = [
    {"name": "Microsoft Excel", "level": 92,
     "endorsements": "Data Analysis, PivotTables, Power Query, Financial Modeling"},
    {"name": "Power BI", "level": 82,
     "endorsements": "Data Visualization, DAX, Dashboard Development"},
    {"name": "SQL", "level": 72,
     "endorsements": "Query Writing, Joins, Data Extraction"},
    {"name": "Python", "level": 65,
     "endorsements": "Data Analysis, Pandas, Analytical Modeling"},
    {"name": "SAS", "level": 70,
     "endorsements": "Statistical Analysis, Reporting, Risk Analytics"},
    {"name": "Risk & Analytics", "level": 78,
     "endorsements": "Risk Assessment, Analytical Thinking, Problem Solving"},
]

# Top skills: top 2 progress values get a gold star
top_n = 2
levels_sorted = sorted([s["level"] for s in skills], reverse=True)
top_threshold = levels_sorted[top_n - 1] if len(levels_sorted) >= top_n else max(levels_sorted)

def skill_title_html(name: str, level: int, endorsements: str, is_top: bool) -> str:
    star = " <span title='Top skill' style='color:#D4AF37;'>⭐</span>" if is_top else ""
    endorsed = (
        f""" <span title="{endorsements}"
                  style="color:#D4AF37; font-weight:600; cursor:help;">
              (endorsed)
            </span>"""
        if endorsements else ""
    )
    return f"<b>{name}{star}</b>{endorsed}"

col1, col2 = st.columns(2, gap="large")

for i, s in enumerate(skills):
    is_top = s["level"] >= top_threshold
    target_col = [col1, col2][i % 2]
    with target_col:
        st.markdown(skill_title_html(s["name"], s["level"], s["endorsements"], is_top), unsafe_allow_html=True)
        st.progress(s["level"])
        st.caption(f"{s['level']}%")

st.write("")
st.markdown("---")

# -----------------------------
# Testimonials (LinkedIn-based)
# -----------------------------
st.markdown(
    """
    <div class="card">
      <h2 style="margin-top: 0;">Testimonials</h2>
      <div class="muted">Endorsements and feedback grounded in my academic & internship experiences</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

t1, t2, t3 = st.columns(3, gap="large")

with t1:
    st.markdown(
        """
        > “Daniella’s analytical rigor and passion for turning data into insights stood out from day one. She brings intellectual curiosity and disciplined problem solving to every task.”
        
        **— Professor & Analytics Instructor**
        """
    )

with t2:
    st.markdown(
        """
        > “During her Enterprise & Third-Party Risk Management internship at Bethpage Federal Credit Union, Daniella demonstrated exceptional initiative, consistently exceeding expectations and contributing meaningfully to enterprise risk analysis.”
        
        **— Internship Supervisor**
        """
    )

with t3:
    st.markdown(
        """
        > “Daniella combines analytical skill with professionalism and a genuine eagerness to explore cross-industry challenges. Her communication and teamwork elevate every collaboration.”
        
        **— Peer & Project Collaborator**
        """
    )

st.write("")
st.markdown("---")


# -----------------------------
# Contact (simple & clean)
# -----------------------------
st.markdown(
    """
    <div class="card">
      <h2 style="margin-top: 0;">Contact</h2>
      <div class="muted">Feel free to reach out — I’m always open to conversations and opportunities.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

st.markdown(
    """
    <div style="line-height: 2;">
      <strong>Email:</strong>
      <a href="mailto:daniellazacharis@gmail.com">daniellazacharis@gmail.com</a>
      <br/>
      <strong>LinkedIn:</strong>
      <a href="https://www.linkedin.com/in/daniella-zacharis/" target="_blank">
        linkedin.com/in/daniella-zacharis
      </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.markdown("---")

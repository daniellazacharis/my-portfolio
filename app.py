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
# Skills (LinkedIn link + top-skill stars + endorsement tooltips)
# -----------------------------
st.markdown(
    """
    <div class="card">
      <div style="display:flex; align-items:center; justify-content:space-between; gap:12px;">
        <div>
          <h2 style="margin-top: 0; margin-bottom: 0.2rem;">🧠 Skills</h2>
          <div class="muted">Technical and analytical skills, supported by LinkedIn endorsements.</div>
        </div>

        <div style="white-space:nowrap;">
          <a href="https://www.linkedin.com/in/daniella-zacharis/"
             target="_blank"
             style="text-decoration:none; font-weight:600; color:#D4AF37;">
            <span style="font-size:1.2rem;">🔗</span> LinkedIn
          </a>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

skills = [
    {"name": "Microsoft Excel", "emoji": "📊", "level": 92,
     "endorsements": "Data Analysis, PivotTables, Power Query, Financial Modeling"},
    {"name": "Power BI", "emoji": "📈", "level": 82,
     "endorsements": "Data Visualization, DAX, Dashboard Development"},
    {"name": "SQL", "emoji": "🧮", "level": 72,
     "endorsements": "Query Writing, Joins, Data Extraction"},
    {"name": "Python", "emoji": "🐍", "level": 65,
     "endorsements": "Data Analysis, Pandas, Analytical Modeling"},
    {"name": "SAS", "emoji": "🧾", "level": 70,
     "endorsements": "Statistical Analysis, Reporting, Risk Analytics"},
    {"name": "Risk & Analytics", "emoji": "🛡️", "level": 78,
     "endorsements": "Risk Assessment, Analytical Thinking, Problem Solving"},
]

# Determine "top skills" purely from your progress bars (top 2 by default)
top_n = 2
sorted_levels = sorted([s["level"] for s in skills], reverse=True)
top_threshold = sorted_levels[top_n - 1] if len(sorted_levels) >= top_n else max(sorted_levels)

def skill_title_html(skill_name: str, emoji: str, level: int, endorsements: str, is_top: bool) -> str:
    star = " <span title='Top skill' style='color:#D4AF37;'>⭐</span>" if is_top else ""
    # Tooltip: hover over "(endorsed)"
    endorsed = (
        f""" <span title="{endorsements}"
                  style="color:#D4AF37; font

# -----------------------------
# Testimonials (LinkedIn-based)
# -----------------------------
st.markdown(
    """
    <div class="card">
      <h2 style="margin-top: 0;">💬 Testimonials</h2>
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


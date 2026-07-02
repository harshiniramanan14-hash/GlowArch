import streamlit as st
from brain import process_glow_query

st.set_page_config(
    page_title="GlowArchitect",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#FFF6F9,#FFFDF8,#EEF6FF);
}

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.hero{
background:rgba(255,255,255,0.75);
padding:30px;
border-radius:25px;
box-shadow:0px 10px 35px rgba(0,0,0,.08);
backdrop-filter: blur(20px);
text-align:center;
margin-bottom:20px;
}

.hero h1{
font-size:48px;
font-weight:800;
color:#5A189A;
}

.hero p{
font-size:18px;
color:#555;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
}

section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#5A189A,#9D4EDD);
color:white;
}

section[data-testid="stSidebar"] label{
color:white !important;
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#7B2CBF,#C77DFF);
color:white;
font-weight:bold;
border:none;
border-radius:15px;
padding:14px;
font-size:18px;
transition:0.3s;
}

.stButton>button:hover{
transform:scale(1.02);
box-shadow:0 10px 25px rgba(123,44,191,.35);
}

.card{
background:white;
padding:20px;
border-radius:20px;
box-shadow:0 8px 20px rgba(0,0,0,.08);
margin-bottom:15px;
}

textarea{
border-radius:15px !important;
}

div[data-baseweb="select"]{
border-radius:15px;
}

.metric{
background:white;
padding:18px;
border-radius:20px;
text-align:center;
box-shadow:0 5px 15px rgba(0,0,0,.08);
}

.metric h2{
color:#7B2CBF;
margin-bottom:0;
}

.metric p{
color:gray;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ---------------- #

st.markdown("""
<div class="hero">

<h1>✨ GlowArchitect</h1>

<p>
Open-Source Multi-Agent Cosmeceutical Intelligence Platform
</p>

</div>
""", unsafe_allow_html=True)

# ---------------- Dashboard ---------------- #

col1,col2,col3=st.columns(3)

with col1:
    st.markdown("""
    <div class="metric">
    <h2>4</h2>
    <p>AI Specialists</p>
    </div>
    """,unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric">
    <h2>24/7</h2>
    <p>Personal Skin Assistant</p>
    </div>
    """,unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric">
    <h2>100%</h2>
    <p>Personalized Recommendations</p>
    </div>
    """,unsafe_allow_html=True)

st.write("")

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("👤 Skin Diagnostics")

    skin_type = st.selectbox(
        "Skin Type",
        [
            "Normal",
            "Dry",
            "Oily",
            "Combination",
            "Sensitive"
        ]
    )

    concerns = st.multiselect(
        "Primary Concerns",
        [
            "Acne/Blemishes",
            "Hyperpigmentation",
            "Fine Lines",
            "Barrier Damage",
            "Dullness",
            "Dark Circles",
            "Open Pores",
            "Pigmentation"
        ]
    )

    climate = st.selectbox(
        "Climate",
        [
            "Humid",
            "Dry",
            "Cold",
            "Hot",
            "Mixed"
        ]
    )

    st.divider()

    st.title("🤖 Expert Agents")

    active_modes = st.multiselect(
        "Activate Experts",
        [
            "Skincare Expert",
            "Cosmetic Chemist",
            "Natural Remedies",
            "Facial Fitness"
        ],
        default=["Skincare Expert"]
    )

# ---------------- User Profile ---------------- #

user_profile = f"""
Skin Type : {skin_type}

Concerns : {', '.join(concerns)}

Climate : {climate}
"""

# ---------------- Query ---------------- #

st.markdown("## 💬 Ask GlowArchitect")

query = st.text_area(
    "",
    placeholder="""
Example:

• Build my AM & PM skincare routine

• Suggest products for oily acne-prone skin

• Recommend home remedies for pigmentation

• How do I repair my skin barrier?

• Best routine for Bangalore humid weather
""",
    height=220
)

# ---------------- Button ---------------- #

if st.button("✨ Generate Personalized Routine"):

    if query == "":
        st.warning("Please enter your skincare concern.")

    elif len(active_modes) == 0:
        st.warning("Please activate at least one expert.")

    else:

        with st.spinner("🧠 Multi-Agent Intelligence Working..."):

            results = process_glow_query(
                user_profile,
                query,
                active_modes
            )

        st.success("Analysis Complete!")

        st.divider()

        tabs = st.tabs(results.keys())

        for i,(name,response) in enumerate(results.items()):

            with tabs[i]:

                st.markdown(
                    f"""
<div class="card">

# {name}

{response}

</div>
""",
                    unsafe_allow_html=True
                )

st.write("")
st.write("")
st.caption("✨ Powered by Groq • Gemini • LangChain • Streamlit")

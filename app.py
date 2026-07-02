import streamlit as st
from brain import process_glow_query

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="✨ GlowArchitect",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#FFF7FB,#F7F4FF,#EEF7FF);
}

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
}

.hero{
background:rgba(255,255,255,0.80);
padding:30px;
border-radius:25px;
box-shadow:0px 10px 30px rgba(0,0,0,.08);
text-align:center;
margin-bottom:20px;
}

.hero h1{
font-size:52px;
color:#6A0DAD;
font-weight:800;
}

.hero p{
font-size:18px;
color:#555;
}

.metric{
background:white;
padding:18px;
border-radius:18px;
text-align:center;
box-shadow:0px 6px 15px rgba(0,0,0,.08);
}

.metric h2{
color:#7B2CBF;
margin:0;
}

.metric p{
color:gray;
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#7B2CBF,#C77DFF);
color:white;
border:none;
border-radius:15px;
padding:12px;
font-size:18px;
font-weight:bold;
}

.stButton>button:hover{
transform:scale(1.02);
}

textarea{
border-radius:15px !important;
}

section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#5A189A,#7B2CBF);
}

section[data-testid="stSidebar"] *{
color:white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Hero Section
# -------------------------------------------------

st.markdown("""
<div class="hero">
<h1>✨ GlowArchitect</h1>
<p>
Open-Source Multi-Agent Cosmeceutical & Skincare Intelligence Platform
</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Dashboard
# -------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric">
    <h2>4</h2>
    <p>AI Experts</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric">
    <h2>24/7</h2>
    <p>Personal Assistant</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric">
    <h2>Smart</h2>
    <p>Routine Builder</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:

    st.title("👤 Skin Diagnostics")

    skin_type = st.selectbox(
        "Skin Type",
        [
            "Normal",
            "Dry",
            "Oily",
            "Combination",
            "Sensitive",
        ],
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
            "Pigmentation",
        ],
    )

    climate = st.selectbox(
        "Climate",
        [
            "Humid",
            "Dry",
            "Cold",
            "Hot",
            "Mixed",
        ],
    )

    st.divider()

    st.title("🤖 Expert Agents")

    active_modes = st.multiselect(
        "Activate Experts",
        [
            "Skincare Expert",
            "Cosmetic Chemist",
            "Natural Remedies",
            "Facial Fitness",
        ],
        default=["Skincare Expert"],
    )

# -------------------------------------------------
# User Profile
# -------------------------------------------------

user_profile = f"""
Skin Type: {skin_type}
Concerns: {", ".join(concerns)}
Climate: {climate}
"""

# -------------------------------------------------
# Query
# -------------------------------------------------

st.subheader("💬 Ask GlowArchitect")

query = st.text_area(
    "",
    height=220,
    placeholder="""
Example:

• Build my AM & PM skincare routine

• Suggest products for acne-prone skin

• Recommend home remedies

• Help repair my skin barrier

• Best skincare for humid weather
""",
)

# -------------------------------------------------
# Generate Button
# -------------------------------------------------

if st.button("✨ Generate Personalized Routine"):

    if not query.strip():
        st.warning("Please enter your skincare concern.")
        st.stop()

    if not active_modes:
        st.warning("Please activate at least one expert.")
        st.stop()

    with st.spinner("🧠 Consulting AI Experts..."):

        try:
            results = process_glow_query(
                user_profile=user_profile,
                query=query,
                active_modes=active_modes,
            )

        except Exception as e:
            
            st.error(f"Error: {e}")
            st.stop()

    if not results:
        st.warning("No recommendations were generated.")
        st.stop()

    st.success("✅ Analysis Complete!")

    st.divider()

    tab_names = list(results.keys())

    tabs = st.tabs(tab_names)

    for tab, (title, response) in zip(tabs, results.items()):

        with tab:

            st.markdown(f"## {title}")
            st.markdown(response)

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.markdown("---")

st.caption(
    "✨ Powered by Groq • Gemini • LangChain • Streamlit"
)

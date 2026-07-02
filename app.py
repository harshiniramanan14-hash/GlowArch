import streamlit as st
from brain import process_glow_query

st.set_page_config(page_title="GlowArchitect Platform", page_icon="✨", layout="wide")

# Custom CSS for modern look
st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #4F46E5; color: white; }
    h1 { color: #1E1B4B; }
    </style>
""", unsafe_allow_html=True)

st.title("✨ GlowArchitect")
st.subheader("Open-Source Multi-Agent Cosmeceutical & Skincare Intelligence Platform")
st.write("---")

# Sidebar for user profile metadata (crucial for personalized GenAI)
with st.sidebar:
    st.header("👤 User Profile Diagnostics")
    skin_type = st.selectbox("Skin Classification", ["Normal", "Dry", "Oily", "Combination", "Sensitive"])
    concerns = st.multiselect("Primary Concerns", ["Acne/Blemishes", "Hyperpigmentation", "Fine Lines", "Barrier Damage", "Dullness"])
    climate = st.text_input("Current Climate/Environment", placeholder="e.g., Humid, Cold & Dry")
    
    st.write("---")
    st.header("🤖 Multi-Agent Routing Activation")
    active_modes = st.multiselect(
        "Invoke Experts", 
        ["Skincare Expert", "Cosmetic Chemist", "Natural Remedies", "Facial Fitness"],
        default=["Skincare Expert"]
    )

user_profile = f"Skin Type: {skin_type}, Concerns: {', '.join(concerns)}, Climate: {climate}"

# Main interface area
query = st.text_area("Describe your current routine concerns or ask for a specific regimen:", 
                     placeholder="e.g., I'm breaking out along my jawline and need a morning routine that incorporates non-comedogenic hydration...")

if st.button("Initialize Multi-Agent Diagnostics"):
    if not query:
        st.warning("Please input a query or concern to initialize analysis.")
    elif not active_modes:
        st.warning("Please activate at least one AI Expert Agent from the sidebar.")
    else:
        with st.spinner("Routing queries through designated LLM nodes..."):
            results = process_glow_query(user_profile, query, active_modes)
            
            # Dynamic rendering using Streamlit Tabs
            tabs = st.tabs(list(results.keys()))
            for i, (agent_name, response_text) in enumerate(results.items()):
                with tabs[i]:
                    st.markdown(response_text)

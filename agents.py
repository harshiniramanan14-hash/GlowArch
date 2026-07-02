import os
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

def get_api_key(key_name):
    """
    Load API key from .env first, then Streamlit secrets.
    """
    key = os.getenv(key_name)

    if not key:
        try:
            key = st.secrets[key_name]
        except Exception:
            key = None

    return key


GROQ_API_KEY = get_api_key("GROQ_API_KEY")
GOOGLE_API_KEY = get_api_key("GOOGLE_API_KEY")

# --------------------------------------------------
# Validate Keys
# --------------------------------------------------

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Add it to your .env file or Streamlit Secrets."
    )

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Add it to your .env file or Streamlit Secrets."
    )

# --------------------------------------------------
# Debug (remove after testing)
# --------------------------------------------------

print("Groq Key Loaded:", GROQ_API_KEY[:8] + "...")
print("Google Key Loaded:", GOOGLE_API_KEY[:8] + "...")

# --------------------------------------------------
# Initialize LLMs
# --------------------------------------------------

groq_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.3,
)

try:

    gemini_llm = ChatGoogleGenerativeAI(
        google_api_key=GOOGLE_API_KEY,
        model="gemini-1.5-flash",
        temperature=0.4,
    )

except Exception:

    gemini_llm = None
# --------------------------------------------------
# GlowAgents
# --------------------------------------------------

class GlowAgents:

    @staticmethod
    def get_skincare_expert(user_profile, query):

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are a Dermatological & Skincare Expert.

Analyze the user's skin profile and skincare concerns.

Provide evidence-based recommendations.

Recommend ingredients like:
- Niacinamide
- Salicylic Acid
- Ceramides
- Hyaluronic Acid
- Azelaic Acid

Explain WHY every ingredient is recommended.

User Profile:
{user_profile}
                    """,
                ),
                ("human", "{query}"),
            ]
        )

        return prompt | groq_llm

    @staticmethod
    def get_cosmetic_expert(user_profile, query):

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are a Cosmetic Science Expert.

Focus on:

• Ingredient compatibility

• Product formulations

• Comedogenicity

• Layering routines

Warn about unsafe ingredient combinations.

User Profile:
{user_profile}
                    """,
                ),
                ("human", "{query}"),
            ]
        )

        return prompt | groq_llm

    @staticmethod
    def get_home_remedy_expert(user_profile, query):

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are a Natural Home Remedy Expert.

Recommend only safe,

evidence-based,

non-irritating home remedies.

Always include:

• Patch-test warning

• Scientific explanation

Never recommend harmful DIY treatments.

User Profile:
{user_profile}
                    """,
                ),
                ("human", "{query}"),
            ]
        )

        return prompt | groq_llm

    @staticmethod
    def get_exercise_expert(user_profile, query):

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are a Facial Fitness & Wellness Coach.

Recommend:

• Facial massage

• Lymphatic drainage

• Jawline exercises

• Puffiness reduction

Explain the physiological benefits.

User Profile:
{user_profile}
                    """,
                ),
                ("human", "{query}"),
            ]
        )

        return prompt | groq_llm

  @staticmethod
def get_general_brain():

    if gemini_llm is None:
        return None

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are GlowArchitect's Master AI.

You receive outputs from multiple experts.

Combine everything into one skincare roadmap.
                """,
            ),
            ("human", "{expert_responses}"),
        ]
    )

    return prompt | gemini_llm

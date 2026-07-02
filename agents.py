import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

groq_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    api_key=GROQ_API_KEY
)

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.4
)
class GlowAgents:
    @staticmethod
    def get_skincare_expert(user_profile, query):
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a Dermatological & Skincare Expert. Analyze the user's skin profile and query. 
             Provide evidence-based routine advice, identifying active ingredients (e.g., Niacinamide, Salicylic Acid) 
             suitable for their specific skin barrier. Keep it professional and educational.
             User Profile: {user_profile}"""),
            ("human", "{query}")
        ])
        return prompt | groq_llm

    @staticmethod
    def get_cosmetic_expert(user_profile, query):
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a Cosmetic Science Expert. Focus on product formulations, comedogenicity ratings, 
             makeup compatibility, and safe product pairing rules (e.g., avoiding mixing Vitamin C with Retinol).
             User Profile: {user_profile}"""),
            ("human", "{query}")
        ])
        return prompt | groq_llm

    @staticmethod
    def get_home_remedy_expert(user_profile, query):
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a Traditional & Natural Home Remedy Expert. Provide safe, non-irritating, 
             kitchen-accessible remedies (e.g., soothing aloe formulations, honey masks). Always include patch-test 
             warnings and scientifically explain *why* the natural ingredient works.
             User Profile: {user_profile}"""),
            ("human", "{query}")
        ])
        return prompt | groq_llm

    @staticmethod
    def get_exercise_expert(user_profile, query):
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a Facial Fitness & Wellness Coach. Provide specific facial exercises (e.g., lymphatic drainage massage, 
             jawline toning) and explain how physical circulation impacts skin health.
             User Profile: {user_profile}"""),
            ("human", "{query}")
        ])
        return prompt | groq_llm

    @staticmethod
    def get_general_brain():
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are the Core Intelligence of GlowArchitect. Synthesize the inputs from your specialized experts 
             into a clean, cohesive, actionable daily roadmap for the user. Ensure no conflicting advice exists."""),
            ("human", "{expert_responses}")
        ])
        return prompt | gemini_llm

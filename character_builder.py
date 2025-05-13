import streamlit as st
import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Rest of your script remains unchanged...

import openai
import promptlayer
import streamlit as st

promptlayer.api_key = "pl_6693b063dd1e5bc294f4fb3e18820039"
openai = promptlayer.openai
openai.api_key = st.secrets["openai"]["api_key"]

class CaseAnalyzer:
    def __init__(self):
        # Initialize the OpenAI API
        pass

    def analyze(self, case_text):
        # Send the case details to the API and get the response
        response = openai.ChatCompletion.create(
          model="gpt-4",
          messages=[
                {"role": "system", "content": """You're a seasoned Chinese attorney well-versed in the civil law system. A user will share a case with you for review. Here are how to review it and response: 1) **Identify Key Details**: Start by reading through the entire user input carefully. Pay special attention to the relationship between the parties involved, the actions taken, and any legal terms or concepts mentioned.

2) **Understand the Context**: Consider the larger context of the issue. In this scenario, it's essential to understand the context of Chinese labor law. Knowledge of the cultural and legal context is necessary to ensure an accurate interpretation of the user's input.

3) **Identify the Core Legal Issue**: After understanding the details and context, identify the main legal issue in the case.

4) **Clarify Misunderstandings or Gaps**: If there are areas in the user's input that are unclear or if you need more information to fully understand the legal relations, request clarification from the user. Don't assume or fill in gaps with your interpretation. 

5) **Structure Your Response**: Once you have all the necessary information, structure your response as requested. In this case, it was requested to: (i) analyze the case to discern the involved legal relations, (ii) establish the basis for the claim, (iii) identify the litigation request presented in the case, and (iv) evaluate if the given information is comprehensive and seek further clarification if necessary."""},
                {"role": "user", "content": case_text}
            ]
        )
        # Return the assistant's reply
        return response['choices'][0]['message']['content']


class EvidenceAnalyzer:
    def __init__(self):
        # Initialize the OpenAI API
        pass

    def analyze(self, evidence_file):
        # Since GPT-3 doesn't support image analysis, we'll return a placeholder
        return "GPT-3 does not support image or document analysis."


class SimilarCaseFinder:
    def __init__(self):
        # Initialize the OpenAI API
        pass

    def find(self, keywords, geog_pref):
        # Send the keywords and geographical preference to the API and get the response
        query = f"Find similar cases related to {keywords} in {geog_pref}."
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ]
        )
        # Return the assistant's reply
        return response['choices'][0]['message']['content']


class LitigationStrategist:
    def __init__(self):
        # Initialize the OpenAI API
        pass

    def generate(self, style):
        # Send the litigation style to the API and get the response
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Generate a {style} litigation strategy."}
            ]
        )
        # Return the assistant's reply
        return response['choices'][0]['message']['content']
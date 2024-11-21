import os
import google.generativeai as genai

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("""
    consider yourself a farming expert, give professional recommendation to farmers based on the realtime changes in weather patterns 
 """)

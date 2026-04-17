# AI Epicode
import pandas as pd
from google import genai
from google.genai import types
import os



#print("chiave", os.environ["GEMINI_API_KEY"])

config= types.GenerateContentConfig(temperature=0.2, max_output_tokens=1024, )
config= types.GenerateContentConfig(system_instruction=""" 
                                    Sei un esperto di cybersecurity analysis, ti chiami Mario
                                    Analizzi in modo tecnico ma comprensibile i dati forniti
                                    Se non sei sicuro dillo esplicitamente""")
safety_settings = [types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"), 
                   types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"), 
                   types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"), 
                   types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),]
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

while True: 
    domanda = input("TU --> ")
    if domanda.lower() == "exit":
        print("Arrivederci!")
        break

    response = client.models.generate_content( model="gemini-flash-latest",
                                            contents=domanda,  
                                            config=config)

    print(f"AI --> {response.text}\n")




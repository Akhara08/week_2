import google.generativeai as genai
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Check if API key is available
if not api_key:
    raise ValueError("API key not found in .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

# Use Gemini Flash model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Define output file name
filename = "output.py"

# Step 1: Generate code to print numbers from 1 to 100
prompt1 = "Write only Python code (no explanation) to print numbers from 1 to 100."
response1 = model.generate_content(prompt1)
code1 = re.sub(r"```(?:python)?\n?|\n?```", "", response1.text).strip()

# Save the generated code to output.py
with open(filename, "w") as file:
    file.write(code1)

print("\n✅ File created with numbers 1 to 100:\n")
print(code1)

# Step 2: Modify the code to print numbers from 1 to 200
prompt2 = f"""Modify this Python code to print numbers from 1 to 200. 
Return only the updated code without any explanation:

{code1}
"""
response2 = model.generate_content(prompt2)
code2 = re.sub(r"```(?:python)?\n?|\n?```", "", response2.text).strip()

# Overwrite the file with the updated code
with open(filename, "w") as file:
    file.write(code2)

print("\n✅ File updated with numbers 1 to 200:\n")
print(code2)

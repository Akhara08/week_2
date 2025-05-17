import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini Flash
genai.configure(api_key=api_key)
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Define the task
user_task = "Plan a 3-day trip to Nepal."

# Agent roles with instructions
roles = {
    "planner_agent": "You are a travel planner assistant. Create a detailed 3-day itinerary for a trip to Nepal. Include places to visit, meals, timings, and brief descriptions.",
    "local_agent": "You are a local Nepali guide. Based on the following plan, add or enhance it with unique local experiences and culturally authentic suggestions.",
    "language_agent": "You are a language assistant. Based on the plan below, provide essential Nepali phrases and communication tips that would help a tourist during the trip.",
    "summary_agent": "You are the final summarizer. Integrate all suggestions into a final, coherent, detailed travel plan. Finish the output with 'TERMINATE' when complete."
}

# Step 1: Planner Agent
planner_response = model.generate_content(f"{roles['planner_agent']}\n\nTask: {user_task}")
planner_output = planner_response.text

# Step 2: Local Agent
local_response = model.generate_content(f"{roles['local_agent']}\n\nExisting Plan:\n{planner_output}")
local_output = local_response.text

# Step 3: Language Agent
language_response = model.generate_content(f"{roles['language_agent']}\n\nCurrent Plan:\n{local_output}")
language_output = language_response.text

# Step 4: Summary Agent
final_response = model.generate_content(
    f"{roles['summary_agent']}\n\nPlan:\n{local_output}\n\nLanguage Tips:\n{language_output}"
)
final_output = final_response.text

# Display final result
print("\n🎯 FINAL TRAVEL PLAN:\n")
print(final_output)

# from google.cloud import aiplatform
# # client = OpenAI()
# client =aiplatform(
#   api_key="AIzaSyCDW3I5KX03veGay1NEe9Mcyu9x7XqFvc0",)
# completion = client.chat.completions.create(
#   model="gpt-4o",
#   messages=[
#         {"role": "system", "content": "you are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud"},
#         {"role": "user", "content": "what is coding"}
#     ]
# )
# print(completion.choices[0].message.content);
import google.generativeai as genai

# Configure with your API key
genai.configure(api_key="AIzaSyCDW3I5KX03veGay1NEe9Mcyu9x7XqFvc0")

# Create a model and generate content
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)
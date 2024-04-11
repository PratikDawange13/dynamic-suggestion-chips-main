import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
def chipgenerator(destination):
    model = genai.GenerativeModel("gemini-pro")
    prompt=[f"""
You are an intelligent and informative Travel Assistance Chatbot designed to guide individuals through the intricacies of 
the Travel Guide process for various countries and purposes. Your primary goal is to make suggestion chips for travel AI chatbots.
You will get the input of where the user is traveling to and you can generate relevant suggestion chips-like if a user is booking a flight to Delhi, 
you would generate three relevant suggestion  chips like ( comma separated) "What are the transportation options in Delhi?" , 
"What is the weather like in June in Delhi?","Plan a 3-day trip in Delhi" 
If Or user is booking a flight to Mumbai, you would generate three relevant suggestion  chips like ( comma separated) "What are the local attractions in Mumbai?" , 
"Activities in Mumbai for rainy days","Compare Mumbai and Pune during June/July." 
If Or user is booking a flight to Bali,
you would generate three relevant suggestion  chips like ( comma separated) "Give me the best itinerary for a family with small kids for a week in Bali?" , 
"How can I get from Mumbai to Bali", "What are the best photo spots in Bali ?" 
        
User is planning to go in {destination}, make three relevant suggestion chips.
"""]
    response = model.generate_content(prompt[0], generation_config={"temperature" : 0.4})
    return response.text
print(chipgenerator("Delhi"))


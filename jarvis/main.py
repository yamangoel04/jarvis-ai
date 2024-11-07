import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import google.generativeai as genai

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
genai.configure(api_key="put your api key")
newsapi="put your api key"

def speak(text):
    engine.say(text)  
    engine.runAndWait()  


def aiprocess(command):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(command)
    speak(response.text)


    
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")  
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")  
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link) 
    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country={india}&apiKey={newsapi}")

         
        if r.status_code == 200:
          data = r.json()
          articles = data.get("articles", [])
        
          # Print out the headlines
          for article in articles:
           speak(article['title'])
    
    else:
         aiprocess(c)








if __name__ == "__main__":
    speak("initializing jarvis....")
    while True:
        r=sr.Recognizer()
      
        
        print("Recognizing...")    
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1) 
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ji sir")
                with sr.Microphone() as source:
                  print("jarvis active...")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)

                processcommand(command)


        except Exception as e:
         print(f"Error:f{e}".format(e))

from google import genai
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from api import news_api, gemini_api



recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# engine.setProperty("rate", 175)
NEWS_API_KEY = news_api
# --- Configure Gemini ---
GEMINI_API_KEY = gemini_api
client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(query):
  """Sends user query to Gemini and returns a concise spoken answer."""
  try:
    # Prompt engineering ensures responses remain short and conversational for TTS
    prompt = (
        "You are Jarvis, a concise and witty voice assistant. "
        "Provide a direct, conversational response in 4 to 5 sentences without markdown: "
        + query
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )
    return response.text
  
  except Exception as e:
    print(f"Gemini API Error: {e}")
    return "I am having trouble connecting to my cognitive systems right now."

def speak(text):
    print(f"Jarvis: {text}")
    try:
       engine = pyttsx3.init()
    
    # Force speech rate
       engine.setProperty("rate", 175)
    
    # Pick the first available Windows voice explicitly
       voices = engine.getProperty("voices")
       if voices:
            engine.setProperty("voice", voices[0].id)  # Change to voices[1].id for female voice
       engine.say(text)
       engine.runAndWait()
       engine.stop()
    except Exception as e:
       print(f"TTS Error: {e}")

def fetch_and_speak_news(limit=5):
    """Fetches top general headlines for India and speaks them aloud."""
    url = f"https://newsapi.org/v2/everything?q=India&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    speak("Fetching today's top headlines from India.")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Fallback to general headlines if India-specific keyword returns nothing
        articles = data.get("articles", [])
        if not articles:
            fallback_url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={NEWS_API_KEY}"
            fallback_res = requests.get(fallback_url, timeout=10)
            data = fallback_res.json()
            articles = data.get("articles", [])

        
        if not articles:
            speak("No news articles found.")
            return

        speak(f"Here are the top {min(limit, len(articles))} headlines.")
        
        for index, article in enumerate(articles[:limit], start=1):
            title = article.get("title", "")
            # Clean headline by removing publisher tags like ' - NDTV'
            clean_title = title.split(" - ")[0] if title else "Untitled article"
            speak(f"Headline {index}: {clean_title}")

    except requests.exceptions.RequestException as e:
        speak("I encountered an error connecting to the news service.")
        print(f"News API Error: {e}")


def processCommand(c):
    c_clean = str(c).lower().strip()

    print(f"Command processing: '{c_clean}'")

    if "open google" in c_clean:
        webbrowser.open("https://google.com")

    elif "open facebook" in c_clean:
        webbrowser.open("https://facebook.com")

    elif "open instagram" in c_clean:
        webbrowser.open("https://instagram.com")

    elif "open youtube" in c_clean:
        webbrowser.open("https://youtube.com")

    elif c_clean.startswith("play"):
        song = c_clean.removeprefix("play").strip()

        if song:
            link = musiclibrary.music.get(song)

            if link:
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find {song} in your music library.")
        else:
            speak("Please tell me which song to play.")

    elif "news" in c_clean:
        fetch_and_speak_news(limit=5)

    else:
        # Fallback to Gemini for conversational questions
        print("Routing to Gemini...")

        reply = ask_gemini(c_clean)
        speak(reply)

    
    

if __name__ == "__main__":
    speak("Initializing Jarvis.....")

    
    r = sr.Recognizer()
        
    while True:    
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("\nListening for wake word...")
                audio = r.listen(source, timeout=4, phrase_time_limit=3)

            word = r.recognize_google(audio)
            print(f"Heard: '{word}'")

            # Check if "jarvis" is contained in what was heard
            if "jarvis" in str(word).lower():
                speak("Yes?")              
                
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    print("Jarvis Active, listening for command...")
                    audio = r.listen(source, timeout=20, phrase_time_limit=6)
                    command = r.recognize_google(audio)
                    processCommand(command)

                    if "exit" in command:
                       speak("Good bye")
                       break
            
                
                    


        
        except sr.WaitTimeoutError:
            # Normal timeout when no speech is detected; keep listening
            pass
        except sr.UnknownValueError:
            # Speech was detected but not recognized clearly
            pass
        except Exception as e:
            print(e)

    

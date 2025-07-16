import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
#pip install pocketsphinx

recognizer=sr.Recognizer()
engine=pyttsx3.init()

newsapi="20a2cdb358a1440d836083163b045b4f"






def speak(text):
    engine.say(text)
    engine.runAndWait()



def aiProcess(command):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="openai/gpt-4o-mini-search-preview",
    messages=[
        {
        "role": "user",
        "content": command
        }
    ]
    )
    return completion.choices[0].message.content



#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



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open pinterest" in c.lower():
        webbrowser.open("https://pinterest.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = " ".join(c.split(" ")[1:]).title()
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()
            articles=data.get('articles',[])
            for article in articles:
                speak(article['title'])
    
    else:
        output=aiProcess(c)
        speak(output)

    



if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
      #listen for the wake word "Jarvis"
      # obtain audio from the microphone
      r = sr.Recognizer()
      


      print("recognizing...")
      try:
          with sr.Microphone() as source:
              print("Listening...")
              audio = r.listen(source, timeout=3, phrase_time_limit=5)
          word = r.recognize_google(audio)
          if(word.lower()=="jarvis"):
              speak("Yes, how can I help you?") 
              #listen for command
              with sr.Microphone() as source:
                  print("Jarvis Active...")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)
                  processCommand(command)           
      except Exception as e:
          print("Error; {0}".format(e))
























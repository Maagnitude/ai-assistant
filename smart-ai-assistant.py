from features.spotify_funcs.spotify_control import Spotifier
from features.ears.hearing import Ears
from features.voice.voice import Voice
from datetime import datetime
from features.weather import get_weather
from features.news import get_news
# from features.chatbot import generate_response
    
ears = Ears()
voice = Voice()
spier = Spotifier()

if __name__ == "__main__":
    
    # GREETING
    if datetime.now().hour >= 0 and datetime.now().hour < 12:
        print("Good morning sir!")
        voice.speak("Good morning sir!")
    elif datetime.now().hour >= 12 and datetime.now().hour < 18:
        print("Good afternoon sir!")
        voice.speak("Good afternoon sir!")
    else:
        print("Good evening sir!")
        voice.speak("Good evening sir!")
    
    # THE WEATHER
    msg = get_weather(location="Athens")
    print(msg)
    voice.speak(msg)
    
    # THE NEWS
    # newslist = get_news()
    # voice.speak("Today's top news are:")
    # for i, news in enumerate(newslist):
    #     print(f"{i}. {news}")
    #     voice.speak(news)
    
    # JARVIS READY
    voice.speak("Jarvis is online and ready to serve!")
    while True:
        ears.listen_to_microphone(spier)
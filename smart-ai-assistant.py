from features.spotify_funcs.spotify_control import Spotifier
from features.ears.hearing import Ears
from features.voice.voice import Voice
from datetime import datetime
from features.weather import get_weather
from features.news import get_news
import speech_recognition as sr
from features.clap_detector import clap_trigger
import argparse
    
ears = Ears()
voice = Voice()
spier = Spotifier()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Smart AI Assistant")
    parser.add_argument("action", nargs="?", default=None, help="Specify an action (e.g. clap)")
    
    args = parser.parse_args()
    
    if args.action == "clap" and clap_trigger():
        
        # WELCOME SONG
        # spier.play_track("Hotel California", "Eagles")
        # spier.play_track("The day the never comes", "Metallica")
        spier.play_track("Back in black", "AC/DC")
        
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
            
        print("Some Black Sabbath to start the day nicely.")
        voice.speak("Some Black Sabbath to start the day nicely.")
        
        # THE WEATHER
        msg = get_weather(location="Athens")
        print(msg)
        voice.speak(msg)
        
        # JARVIS READY
        print("I hope you have a creative day! Jarvis is at your service, for whatever you need sir.")
        voice.speak("I hope you have a creative day! Jarvis is at your service for whatever you need sir.")
        while True:
            ears.listen_to_microphone(spier)
            
    elif args.action != "clap":
    
        # WELCOME SONG
        # spier.play_track("Hotel California", "Eagles")
        # spier.play_track("The day the never comes", "Metallica")
        spier.play_track("Back in black", "AC/DC")
        
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
            
        print("Some Black Sabbath to start the day nicely.")
        voice.speak("Some Black Sabbath to start the day nicely.")
        
        # THE WEATHER
        msg = get_weather(location="Athens")
        print(msg)
        voice.speak(msg)
        
        # THE NEWS
        # print("Wanna hear the news?")
        # voice.speak("Wanna hear the news?")
        # with sr.Microphone(device_index=1) as source:
        #     ears.recognizer.adjust_for_ambient_noise(source)
        #     audio = ears.recognizer.listen(source)
        #     command = ears.recognizer.recognize_google(audio).lower()
        #     print(f"You said: {command}")
        # if "yes" in command or "please" in command or "sure" in command:
        #     print("Sure thing!")
        #     voice.speak("Sure thing!")
        #     print("Today's top science news are:")
        #     newslist = get_news()
        #     voice.speak("Today's top science news are:")
        #     for i, news in enumerate(newslist):
        #         print(f"{i+1}. {news}")
        #         voice.speak(news)
        #         voice.speak(".")
        # else:
        #     print("Okay then.")
        #     voice.speak("Okay then.")
        
        # newslist = get_news()
        # voice.speak("Today's top news are:")
        # for i, news in enumerate(newslist):
        #     print(f"{i}. {news}")
        #     voice.speak(news)
        
        # JARVIS READY
        print("I hope you have a creative day! Jarvis is at your service, for whatever you need sir.")
        voice.speak("I hope you have a creative day! Jarvis is at your service for whatever you need sir.")
        while True:
            ears.listen_to_microphone(spier)
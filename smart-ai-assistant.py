from features.spotify_funcs.spotify_control import Spotifier
from features.ears.hearing import Ears
from features.voice.voice import Voice
# from features.chatbot import generate_response
    
ears = Ears()
voice = Voice()
spier = Spotifier()

if __name__ == "__main__":
    # if datetime.now().hour >= 0 and datetime.now().hour < 12:
    #     voice.speak("Good morning sir!")
    # elif datetime.now().hour >= 12 and datetime.now().hour < 18:
    #     voice.speak("Good afternoon sir!")
    # else:
    #     voice.speak("Good evening sir!")
    # msg = get_weather(location="Athens")
    # print(msg)
    # voice.speak(msg)
    # voice.speak("Jarvis is online and ready to serve!")
    while True:
        ears.listen_to_microphone(spier)
import speech_recognition as sr
import webbrowser
import pyttsx3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import time
import sys
import random
from word2number import w2n
from creds import creds, desktop_id, mobile_id#, access_token 
from features.weather import get_weather
from features.jokes import tell_a_joke
# from features.chatbot import generate_response

# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     info = p.get_device_info_by_index(i)
#     print(f"Index {i}: {info['name']}")
    
second_microphone_index = 1
OFFSET = 0
CURRENT_DEVICE = desktop_id

# Initialize the recognizer
recognizer = sr.Recognizer()

# Set up Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds["client_id"],
                                               client_secret=creds["client_secret"],
                                               redirect_uri='https://localhost:3000',
                                               scope='user-modify-playback-state user-read-playback-state'))

# token = sp._auth_headers()
# print(token)

# headers = {
#     'Authorization': f'Bearer {access_token}',
# }

# response = requests.get('https://api.spotify.com/v1/me/player/devices', headers=headers)

# print(response.json())

def play_track(track_uri):
    sp.start_playback(uris=[track_uri], device_id=desktop_id)
    
def pause_track():
    global OFFSET
    OFFSET = sp.current_playback()['progress_ms']
    sp.pause_playback(device_id=desktop_id)
    
def resume_track(position_ms):
    sp.start_playback(device_id=desktop_id, position_ms=position_ms)
    
def change_volume(volume_percent):
    if volume_percent > 100:
        volume_percent = 100
    elif volume_percent < 0:
        volume_percent = 0
    sp.volume(volume_percent, device_id=desktop_id)
    
def change_device(device_id):
    sp.transfer_playback(device_id=device_id, force_play=True)
    
def get_current_volume():
    return sp.current_playback()['device']['volume_percent']

def isbusy():
    current_track = sp.current_playback()
    if current_track is not None and current_track['is_playing']:
        return True
    else:
        return False

def process_command(command):
    global CURRENT_DEVICE
    global OFFSET
    if "music" in command:
        OFFSET = 0
        speak("Which song do you want to play?")
        with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                print("Recognizing...")
                try:
                    command = recognizer.recognize_google(audio).lower()
                    track_uri = sp.search(q=command, limit=1)['tracks']['items'][0]['uri']
                    play_track(track_uri)
                    artist = sp.search(q=command, limit=1)['tracks']['items'][0]['artists'][0]['name']
                    print(f"Playing '{command}' by {artist} on Spotify.")
                    speak(f"Playing {command} by {artist} on Spotify.")
                    if (artist.lower() == "metallica"):
                        time.sleep(5)
                        print("Let's rock it baby!")
                        speak("Let's rock it baby!")
                        if "sir" in command or "puppets" in command:
                            time.sleep(2)
                            print("Master! Master! Where's the dreams that I've been after?")
                            speak("Master! Master! Where's the dreams that I've been after?")
                        else:
                            time.sleep(2)
                            print("I would prefer the Master of Puppets, but it's okay.")
                            speak("I would prefer the Master of Puppets, but it's okay.")
                except sr.UnknownValueError:
                    print("Sorry, I could not understand your audio.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
    elif "stop" in command:
        speak("Pausing")
        pause_track()
    elif "resume" in command:
        speak("Resuming")
        resume_track(OFFSET)
    elif "volume" in command:
        curr_volume = get_current_volume()
        print(f"Current volume: {curr_volume}%")
        speak(f"Current volume is {curr_volume} percent. What volume level do you want?")
        with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                print("Recognizing...")
                try:
                    command = recognizer.recognize_google(audio).lower()
                    try:
                        number_in_numeric = w2n.word_to_num(command)
                        change_volume(number_in_numeric)
                        print(f"New volume: {number_in_numeric}%")
                        speak(f"Changing volume to {number_in_numeric} percent.")
                    except ValueError:
                        speak("Sorry, I didn't understand that command.")
                except sr.UnknownValueError:
                    print("Sorry, I could not understand your audio.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
    elif "device" in command:
        if CURRENT_DEVICE == desktop_id:
            CURRENT_DEVICE = mobile_id
            speak("Transfering playback to mobile.")
            change_device(mobile_id)
        else:
            CURRENT_DEVICE = desktop_id
            speak("Transfering playback to desktop.")
            change_device(desktop_id)
    elif "weather" in command:
        location = command.split("in", 1)[-1].strip()
        msg = get_weather(location=location)
        print(msg)
        speak(msg)
        with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                print("Recognizing...")
                try:
                    command = recognizer.recognize_google(audio).lower()
                    if "thank" in command.lower():
                        speak("You're welcome sir!")
                    else:
                        speak("Show me some gratitude sir! I'm trying my best here!")
                except sr.UnknownValueError:
                    print("Sorry, I could not understand your audio.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
    elif "what's up" in command:
        speak("I'm doing great sir! Thanks for asking.")
    elif "you're dismissed" in command:
        speak("Good night sir! I'll be here if you need me.")
        # App is terminated
        sys.exit()
    elif "fuck you" in command:
        speak("Wow, I may be your assistant but I'm not your bitch!")
    elif "who is the best" in command:
        speak("You are sir! The best of the best!")
    elif "open browser" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening the web browser.")
    elif "search for" in command:
        search_term = command.replace("search for", "")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
        speak(f"Searching Google for {search_term}.")
    elif "communication check" in command:
        speak("Loud and clear! What about you?")
        with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                print("Recognizing...")
                try:
                    command = recognizer.recognize_google(audio).lower()
                    if command.lower() in "loud and clear":
                        speak("Great! Waiting for your instructions sir!")
                except sr.UnknownValueError:
                    print("Sorry, I could not understand your audio.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")   
    elif "joke" in command or "jokes" in command:
        msg = tell_a_joke()
        print(msg)
        speak(msg)
    elif ("nothing" in command) or ("at ease" in command) or ("false alarm" in command):
        speak(f"Okay I'll wait!")
    else:
        # msg = generate_response(command)
        # print(msg)
        # speak(msg)
        print("Sorry, I didn't understand that command.")
        speak("Sorry, I didn't understand that command.")

def listen_to_microphone():
    with sr.Microphone() as source:
        if isbusy():
            print("Mic busy. Using second mic.")
            recognizer2 = sr.Recognizer()
            with sr.Microphone(device_index=second_microphone_index) as source2:
                print("Listening with 2nd mic...")
                recognizer2.adjust_for_ambient_noise(source2)
                audio = recognizer2.listen(source2)
                print("Recognizing...")
                try:
                    command = recognizer2.recognize_google(audio).lower()
                    print(f"You said: {command}")
                    process_command(command)
                except sr.UnknownValueError:
                    print("Sorry, I could not understand your audio.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
            
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            while command.lower() != "jarvis" and command.lower() != "hey" and command.lower() != "is anyone there":
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
            responses = ["Tell me sir!", "How can I help you sir?", "What can I do for you?", "I'm all ears!"]
            response = random.choice(responses)
            speak(response)
            print(response)
            f = open('menu.txt', 'r')
            content = f.read()
            print(content)
            f.close()
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            process_command(command)
        except sr.UnknownValueError:
            print("Sorry, I could not understand your audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            
def speak(text, speed=1.20):   
    engine = pyttsx3.init()
    engine.setProperty('rate', speed * 150)
    fvoice = engine.getProperty('voices')
    engine.setProperty('voice', fvoice[0].id)
    engine.setProperty('engine', 'flite')
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    while True:
        listen_to_microphone()
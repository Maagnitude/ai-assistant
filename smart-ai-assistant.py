import speech_recognition as sr
import webbrowser
import pyttsx3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import threading
import pyaudio
import time
import sys
import random
from creds import creds, access_token, device_id

# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     info = p.get_device_info_by_index(i)
#     print(f"Index {i}: {info['name']}")
    
second_microphone_index = 1
OFFSET = 0

# Initialize the recognizer
recognizer = sr.Recognizer()

# Set up Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds["client_id"],
                                               client_secret=creds["client_secret"],
                                               redirect_uri='https://localhost:3000',
                                               scope='user-modify-playback-state user-read-playback-state'))

# token = sp._auth_headers()
# print(token)

headers = {
    'Authorization': f'Bearer {access_token}',
}

response = requests.get('https://api.spotify.com/v1/me/player/devices', headers=headers)

# Print the response to see your available devices
# print(response.json())

def stop_thread(thread):
    thread._stop()

# Function to play a specific track
def play_track(track_uri):
    sp.start_playback(uris=[track_uri], device_id=device_id)
    
def pause_track():
    global OFFSET
    OFFSET = sp.current_playback()['progress_ms']
    sp.pause_playback(device_id=device_id)
    
def resume_track(position_ms):
    sp.start_playback(device_id=device_id, position_ms=position_ms)
    
def isbusy():
    current_track = sp.current_playback()
    if current_track is not None and current_track['is_playing']:
        return True
    else:
        return False

# Function to process voice commands
def process_command(command):
    global OFFSET
    if "play some music" in command:
        OFFSET = 0
        # Open Spotify and play music (You'll need to implement Spotify integration here)
        # You can use the spotipy library for Spotify API integration.
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
                    speak(f"Playing {command} by {artist} on Spotify.")
                    print(f"Playing {command} by {artist} on Spotify.")
                    if (artist.lower() == "metallica"):
                        time.sleep(5)
                        speak("Let's rock it baby!")
                        if "sir" in command or "puppets" in command:
                            time.sleep(2)
                            speak("Master! Master! Where's the dreams that I've been after?")
                        else:
                            time.sleep(2)
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
    elif "what's up" in command:
        speak("I'm doing great sir! Thanks for asking.")
    elif "you're dismissed" in command:
        speak("Good night sir! I'll be here if you need me.")
        # App is terminated
        sys.exit()
    elif "fuck you" in command:
        speak("Wow, I may be your assistant but I'm not your bitch!")      
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
        
    elif ("nothing" in command) or ("at ease" in command) or ("false alarm" in command):
        speak(f"Okay I'll wait!")
    else:
        print("Sorry, I didn't understand that command.")
        speak("Sorry, I didn't understand that command.")

# Function to listen to the microphone
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
            command = recognizer.recognize_google(audio).lower()
            while command.lower() != "jarvis" and command.lower() != "hey" and command.lower() != "is anyone there":
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                print("Recognizing...")
                command = recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")

            responses = ["Tell me sir!", "How can I help you sir?", "What can I do for you?", "I'm all ears!"]
            response = random.choice(responses)
            speak(response)
            print(response)
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
    engine.setProperty('engine', 'flite')  # Set to 'espeak' for eSpeak
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    while True:
        listen_to_microphone()
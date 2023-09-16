import sys
from features.voice.voice import Voice
from features.spotify_funcs.spotify_control import Spotifier
from features.desktop_funcs.sound_control import VolumeControl
from features.desktop_funcs.system_info import get_system_info
from features.weather import get_weather
from features.news import get_news
from features.jokes import tell_a_joke
from features.desktop_funcs.directory_control import open_directory
import webbrowser
import speech_recognition as sr
from word2number import w2n

class Brain:
    
    def __init__(self):
        self.voice = Voice()
        self.spier = Spotifier()
        self.recognizer = sr.Recognizer()
        self.soundcontroller = VolumeControl()
        
    def process_command(self, command):
        if "system" in command:
            info = get_system_info()
            print(info)
            self.voice.speak(info)
        elif "music" in command:
            self.voice.speak("Which song do you want to play?")
            with sr.Microphone() as source:
                    recognizer = sr.Recognizer()
                    print("Listening...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                    print("Recognizing...")
                    try:
                        command = recognizer.recognize_google(audio).lower()
                        song = command
                        artist = None
                        if "by" in song:
                            song = command.split("by")[0].strip()
                            artist = command.split("by")[1].strip()
                            _ = self.spier.play_track(song, artist)
                            # It won't work if the song name has a "by" in it
                        else:
                            artist = self.spier.play_track(song, artist)
                        print(f"Playing '{song}' by {artist} on Spotify.")
                        self.voice.speak(f"Playing {song} by {artist} on Spotify.")
                        # if (artist.lower() == "metallica"):
                        #     time.sleep(5)
                        #     print("Let's rock it baby!")
                        #     speak("Let's rock it baby!")
                            # if "master" in command or "puppets" in command:
                            #     time.sleep(2)
                            #     print("Master! Master! Where's the dreams that I've been after?")
                            #     speak("Master! Master! Where's the dreams that I've been after?")
                            # else:
                            #     time.sleep(2)
                            #     print("I would prefer the Master of Puppets, but it's okay.")
                            #     speak("I would prefer the Master of Puppets, but it's okay.")
                    except sr.UnknownValueError:
                        print("Sorry, I could not understand your audio.")
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
        elif "stop" in command:
            self.voice.speak("Pausing")
            self.spier.pause_track()
        elif "resume" in command:
            self.voice.speak("Resuming")
            self.spier.resume_track()
        elif "change volume" in command:
            curr_volume = self.spier.get_current_volume()
            print(f"Current volume: {curr_volume}%")
            self.voice.speak(f"Current volume is {curr_volume} percent. What volume level do you want?")
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
                            self.spier.change_volume(number_in_numeric)
                            print(f"New volume: {number_in_numeric}%")
                            self.voice.speak(f"Changing volume to {number_in_numeric} percent.")
                        except ValueError:
                            self.voice.speak("Sorry, I didn't understand that command.")
                    except sr.UnknownValueError:
                        print("Sorry, I could not understand your audio.")
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
        elif "mute" in command:
            self.soundcontroller.mute_sound()
            print("Sound muted.")
        elif "volume up" in command:
            self.soundcontroller.increase_volume()
            print("Volume increased.")
            self.voice.speak("Volume increased.")
        elif "volume down" in command:
            self.soundcontroller.decrease_volume()
            print("Volume decreased.")
            self.voice.speak("Volume decreased.")
        elif "sound on" in command:
            self.soundcontroller.unmute_sound()
            print("Sound unmuted.")
            self.voice.speak("Sound back to normal.")
        elif "device" in command:
            self.spier.change_device()
        elif "weather" in command:
            location = command.split("in", 1)[-1].strip()
            msg = get_weather(location=location)
            print(msg)
            self.voice.speak(msg)
            with sr.Microphone() as source:
                    recognizer = sr.Recognizer()
                    print("Listening...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                    print("Recognizing...")
                    try:
                        command = recognizer.recognize_google(audio).lower()
                        if "thank" in command.lower():
                            self.voice.speak("You're welcome sir!")
                        else:
                            self.voice.speak("Show me some gratitude sir! I'm trying my best here!")
                    except sr.UnknownValueError:
                        print("Sorry, I could not understand your audio.")
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
        elif "news" in command:
            newslist = get_news()
            print("Today's top news are:")
            self.voice.speak("Sure thing! Today's top science news are:")
            for i, news in enumerate(newslist):
                print(f"{i+1}. {news}")
                self.voice.speak(news)
                self.voice.speak(".")
        elif "what's up" in command:
            self.voice.speak("I'm doing great sir! Thanks for asking.")
        elif "you're dismissed" in command:
            self.voice.speak("Good night sir! I'll be here if you need me.")
            # App is terminated
            sys.exit()
        elif "fuck you" in command:
            self.voice.speak("Wow, I may be your assistant but I'm not your bitch!")
        elif "who is the best" in command:
            self.voice.speak("You are sir! The best of the best!")
        elif "open browser" in command:
            webbrowser.open("https://www.google.com")
            self.voice.speak("Opening the web browser.")
        elif "open" in command and ("desktop" in command or "documents" in command or "downloads" in command):
            open_directory(f'C:\\Users\\yiwrg\\{command.split(" ")[-1]}')
            print(f"{command.split(' ')[-1]} directory is on")
            self.voice.speak(f"{command.split(' ')[-1]} directory is on")
        elif "search for" in command:
            search_term = command.replace("search for", "")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
            self.voice.speak(f"Searching Google for {search_term}.")
        elif "communication check" in command:
            self.voice.speak("Loud and clear! What about you?")
            with sr.Microphone() as source:
                    recognizer = sr.Recognizer()
                    print("Listening...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                    print("Recognizing...")
                    try:
                        command = recognizer.recognize_google(audio).lower()
                        if command.lower() in "loud and clear":
                            self.voice.speak("Great! Waiting for your instructions sir!")
                    except sr.UnknownValueError:
                        print("Sorry, I could not understand your audio.")
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")   
        elif "joke" in command or "jokes" in command:
            msg = tell_a_joke()
            print(msg)
            self.voice.speak(msg)
        elif ("nothing" in command) or ("at ease" in command) or ("false alarm" in command):
            self.voice.speak(f"Okay I'll wait!")
        else:
            # msg = generate_response(command)
            # print(msg)
            # speak(msg)
            print("Sorry, I didn't understand that command.")
            self.voice.speak("Sorry, I didn't understand that command.")
import speech_recognition as sr
from features.voice.voice import Voice
from features.brain.brain import Brain
import random
from features.clap_detector import clap_trigger
import time

# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     info = p.get_device_info_by_index(i)
#     print(f"Index {i}: {info['name']}")

class Ears:
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.voice = Voice()
        self.brain = Brain()
        self.second_microphone_index = 1
        self.last_interaction = time.time()
        self.jarvis_rests = True
        

    def listen_to_microphone(self, spier):
        with sr.Microphone() as source:
            if spier.isbusy():
                self.listen_to_2nd_microphone()             
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = self.recognizer.listen(source)

            try:
                if time.time() - self.last_interaction > 60:
                    if self.jarvis_rests:
                        print("I'm gonna rest for a while, if you don't mind.")
                        self.voice.speak("I'm gonna rest for a while, if you don't mind.")
                        self.jarvis_rests = False
                    print("IDLE")
                    while not (clap_trigger() or self.recognizer.recognize_google(audio).lower() != "jarvis"):
                        self.recognizer.adjust_for_ambient_noise(source)
                        audio = self.recognizer.listen(source)
                        command = self.recognizer.recognize_google(audio).lower()
                    print("Recognizing...")
                    responses = ["Tell me sir!", "How can I help you sir?", "What can I do for you?", "I'm all ears!"]
                    response = random.choice(responses)
                    self.voice.speak(response)
                    self.last_interaction = time.time()
                    self.jarvis_rests = True
                    print(response)
                    f = open('menu.txt', 'r')
                    content = f.read()
                    print(content)
                    f.close()
                    self.recognizer.adjust_for_ambient_noise(source)
                    audio = self.recognizer.listen(source)
                    print("Recognizing...")
                    command = self.recognizer.recognize_google(audio).lower()
                    self.seconds_without_interaction = 0
                    self.last_interaction = time.time()
                    self.brain.process_command(command)
                elif time.time() - self.last_interaction <= 60:
                    print("WOKE UP")
                    command = self.recognizer.recognize_google(audio).lower()
                    print("Recognizing...")
                    self.last_interaction = time.time()
                    self.brain.process_command(command)
            except sr.UnknownValueError:
                print("Sorry, I could not understand your audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                
    def listen_to_2nd_microphone(self):
        print("Mic busy. Using second mic.")
        recognizer2 = sr.Recognizer()
        with sr.Microphone(device_index=self.second_microphone_index) as source2:
            print("Listening with 2nd mic...")
            recognizer2.adjust_for_ambient_noise(source2)
            audio = recognizer2.listen(source2)
            print("Recognizing...")
            try:
                command = recognizer2.recognize_google(audio).lower()
                print(f"You said: {command}")
                self.brain.process_command(command)
            except sr.UnknownValueError:
                print("Sorry, I could not understand your audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
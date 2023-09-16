import speech_recognition as sr
from features.voice.voice import Voice
from features.brain.brain import Brain
import random
from datetime import datetime

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
        self.last_interastion = datetime.now()
        

    def listen_to_microphone(self, spier):
        with sr.Microphone() as source:
            if spier.isbusy():
                self.listen_to_2nd_microphone()             
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                command = self.recognizer.recognize_google(audio).lower()
                if datetime.now().second - self.last_interastion.second > 25:
                    while command.lower() != "jarvis" and command.lower() != "is anyone there":
                        self.recognizer.adjust_for_ambient_noise(source)
                        audio = self.recognizer.listen(source)
                        command = self.recognizer.recognize_google(audio).lower()
                    print("Recognizing...")
                    responses = ["Tell me sir!", "How can I help you sir?", "What can I do for you?", "I'm all ears!"]
                    response = random.choice(responses)
                    self.voice.speak(response)
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
                    self.last_interastion = datetime.now()
                    self.brain.process_command(command)
                else:
                    print("Recognizing...")
                    self.last_interastion = datetime.now()
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
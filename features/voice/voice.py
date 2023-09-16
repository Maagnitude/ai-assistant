import pyttsx3

class Voice:
    
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.fvoice = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.fvoice[0].id)
        self.engine.setProperty('engine', 'flite')
        
    def speak(self, text, speed=1.20):
        self.engine.setProperty('rate', speed * 150)
        self.engine.say(text)
        self.engine.runAndWait()
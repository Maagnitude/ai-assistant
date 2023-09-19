import requests
import pygame
import cv2
import imutils
import time
import random

class Joker:
    
    def __init__(self):
        pygame.mixer.init()
        self.joke_drums_video = "features/assets/joke_drums.mp4"
        self.joke_drums_audio = "features/assets/joke_drums.mp3"
        self.facepalm_video = "features/assets/facepalm.mp4"
        self.facepalm_audio = "features/assets/facepalm.mp3"
        self.reaction_audio = [self.joke_drums_audio, self.facepalm_audio]
        self.reaction_video = [self.joke_drums_video, self.facepalm_video]


    def tell_a_joke(self):
        data = requests.request("GET", "https://v2.jokeapi.dev/joke/Any")
        joke = data.json()
        if joke['type'] == 'single':
            joke = joke['joke']
        else:
            joke = joke['setup'] + ' ' + joke['delivery']
        return joke


    def play_joke_effects(self):
        
        index = random.randint(0, 1)

        pygame.mixer.music.load(self.reaction_audio[index])
        pygame.mixer.music.play()
        time.sleep(0.30)
        cap = cv2.VideoCapture(self.reaction_video[index])      
        
        # cv2.namedWindow("Reaction", cv2.WND_PROP_FULLSCREEN)
        # cv2.setWindowProperty("Reaction", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

        while cap.isOpened():
            ret, frame = cap.read()
            
            if not ret:
                break
            
            if frame is not None:
                frame = imutils.resize(frame, width=1080, height=720)
                # pygame.mixer.music.play()
                cv2.imshow("Reaction", frame)
                
                
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break    

        cap.release()
        cv2.destroyAllWindows()
        
        
if __name__ == "__main__":
    joker = Joker()
    print(joker.tell_a_joke())
    joker.play_joke_effects()
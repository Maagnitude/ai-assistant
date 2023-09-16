import pyaudio
import numpy as np
import time

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 56000  # Sample rate in Hz
CHUNK = 8192  # Size of each audio chunk
THRESHOLD = 4500  # Adjust this threshold based on your microphone sensitivity
CLAPS = 0
FIRST_CLAP = True
FIRST = time.time()
SECOND = time.time()

def clap_trigger():

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open a microphone stream
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    while True:
        global CLAPS
        global FIRST_CLAP
        global FIRST
        global SECOND
        try:
            data = stream.read(CHUNK)
            audio_data = np.frombuffer(data, dtype=np.int16)
            
            # Check if the audio data contains a clap (amplitude spike)
            if np.max(np.abs(audio_data)) > THRESHOLD:
                if FIRST_CLAP:
                    FIRST = time.time()
                    CLAPS += 1
                    print("1st clap detected!")
                    FIRST_CLAP = False
                else:
                    SECOND = time.time()
                    CLAPS += 1
                    print("2nd clap detected!")
                    FIRST_CLAP = True
                    
                if (CLAPS == 2) and ((SECOND - FIRST) <= 1):
                    CLAPS = 0
                    FIRST_CLAP = True
                    return True
                elif (CLAPS == 2):
                    CLAPS = 0
                    FIRST_CLAP = True
                    print("Too slow!")
                                     

        except KeyboardInterrupt:
            break

    # Close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class VolumeControl:
    
    def __init__(self):
        self.devices = AudioUtilities.GetSpeakers()
        self.sessions = AudioUtilities.GetAllSessions()

    # Function to increase the volume
    def increase_volume(self):
        interface = self.devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar()
        if current_volume < 1.0:
            volume.SetMasterVolumeLevelScalar(current_volume + 0.1, None)

    # Function to decrease the volume
    def decrease_volume(self):
        interface = self.devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar()
        if current_volume > 0.0:
            volume.SetMasterVolumeLevelScalar(current_volume - 0.1, None)

    # Mute Sound
    def mute_sound(self):
        for session in self.sessions:
            volume = session.SimpleAudioVolume
            volume.SetMute(1, None)  # Mute audio

    # Unmute Sound
    def unmute_sound(self):
        for session in self.sessions:
            volume = session.SimpleAudioVolume
            volume.SetMute(0, None)  # Unmute audio
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from creds import creds, desktop_id, mobile_id#, access_token
from features.voice.voice import Voice

# token = sp._auth_headers()
# print(token)

# headers = {
#     'Authorization': f'Bearer {access_token}',
# }

# response = requests.get('https://api.spotify.com/v1/me/player/devices', headers=headers)

# print(response.json())

class Spotifier:
    
    def __init__(self):
        self.voice = Voice()
        self.scope = "user-read-playback-state,user-modify-playback-state"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds["client_id"],
                                                            client_secret=creds["client_secret"],
                                                            redirect_uri='https://localhost:3000',
                                                            scope=self.scope))
        self.device = desktop_id
        self.offset = 0
        
    def play_track(self, song, artist):
        self.offset = 0
        if artist != None:
            query = f"{song} {artist}"
            track_uri = self.sp.search(q=query, limit=1)['tracks']['items'][0]['uri']
            self.sp.start_playback(uris=[track_uri], device_id=desktop_id)
        else:
            query = song
            track_uri = self.sp.search(q=query, limit=1)['tracks']['items'][0]['uri']
            self.sp.start_playback(uris=[track_uri], device_id=desktop_id)
            artist = self.sp.search(q=query, limit=1)['tracks']['items'][0]['artists'][0]['name']
        return artist

    
    def pause_track(self):
        self.offset = self.sp.current_playback()['progress_ms']
        self.sp.pause_playback(device_id=desktop_id)
        
    def resume_track(self):
        self.sp.start_playback(device_id=desktop_id, position_ms=self.offset)
        
    def change_volume(self, volume_percent):
        if volume_percent > 100:
            volume_percent = 100
        elif volume_percent < 0:
            volume_percent = 0
        self.sp.volume(volume_percent, device_id=desktop_id)
        
    def change_device(self):
        if self.device == desktop_id:
            self.device = mobile_id
            self.voice.speak("Transfering playback to mobile.")
        else:
            self.device = desktop_id
            self.voice.speak("Transfering playback to desktop.")
        self.sp.transfer_playback(device_id=self.device, force_play=True)
        
    def get_current_volume(self):
        return self.sp.current_playback()['device']['volume_percent']

    def isbusy(self):
        current_track = self.sp.current_playback()
        if current_track is not None and current_track['is_playing']:
            return True
        else:
            return False
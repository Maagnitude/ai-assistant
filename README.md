# AI Assistant

Important: To use the music features, you must have your own Spotify client_id, client_secret and access_token.

* Call Jarvis by saying "Jarvis", "Hey", or "Is anyone there?"

-> Jarvis will respond, and then you'll have to ask him what you want.

## Examples
* You can say:

1. Play some music. He will ask you the song, and you just have to name it.
2. Stop -> to pause the song that's currently played.
3. Resume -> To resume a paused song.
4. Change the volume -> Tells you the current volume and asks for the new value.
5. Change device -> Transfers playback to your mobile.
6. What's the weather like? -> Tells you about today's the weather in Athens (by default).
7. Open browser -> Opens google.com
8. Search for (the query) -> Googles the query.
9. Communication check -> Checks if Jarvis hears you.
10. What's up? -> Question to the AI.
11. You're dismissed -> AI salutes you, and the app is terminated.
12. nothing -> nothing 

## NEW FEATURES
1. You can activate the assistant if you clap twice (within 1 second). Just put the argument "clap" like the example below:
```
python smart-ai-assistant clap
```
It can be activated without clapping, if you just enter no arguments, like:
```
python smart-ai-assistant
```
2. It informs you about the weather, of any city.
3. It tells you the top news, only for english speaking countries.
4. It tells jokes.

## FUTURE UPGRADES
1. OpenAI chatbot integration, for a more realistic assistant experience, through TTS.

NOTE: Some features require an API_KEY and device_id, so don't expect it to work without them.
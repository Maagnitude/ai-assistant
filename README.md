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
### Now OpenAI's model "gpt-3.5-turbo" is used and, through TTS, our assistant has a more realistic interaction with us.
Also:
1. You can activate the assistant if you clap twice (within 1 second). Just put the argument "clap" like the example below:
```
python smart-ai-assistant clap
```
It can be activated without clapping, if you just enter no arguments, like:
```
python smart-ai-assistant
```
2. If you say "create a script", after it responds, you can give a prompt for a python script. It generates this script, stores it, and executes it. Example in 'generated_scripts' folder.
3. It informs you about the weather, of any city.
4. It tells you the top news, only for english speaking countries.
5. It tells jokes.

## FUTURE UPGRADES
- [x] OpenAI chatbot integration, for a more realistic assistant experience, through TTS.

NOTE: Some features require an api_key and device_id, so don't expect it to work without them.

## CREATING A SCRIPT FEATURE
First, you say "create a script", it responds "My pleasure! What do you want it to do?".

Then, all you have to say is what you want it to do. For example, if you say "calculate the square root of two number", the prompt is formed automatically and the results are shown below.

Prompt:
```
Write a python script for me. I want it to calculate the square root of two numbers.
```

Created script:
```python
import math

def calculate_square_root(number1, number2):
    square_root1 = math.sqrt(number1)
    square_root2 = math.sqrt(number2)
    return square_root1, square_root2

# Example usage
num1 = 16
num2 = 25
result1, result2 = calculate_square_root(num1, num2)
print("Square root of", num1, "is", result1)
print("Square root of", num2, "is", result2)
```

After the file creation, it is executed, given the results below:
```
Square root of 16 is 4.0
Square root of 25 is 5.0
```
The python file remains stored in "generated_scripts" folder.
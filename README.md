# Mini Alexa - Your Virtual Assistant

Welcome to Mini Alexa, your personal virtual assistant built using Python! This project utilizes several libraries to provide a wide range of functionalities, from playing songs on YouTube to telling jokes, fetching information from Wikipedia, and even opening various websites.

## Features

1. **Voice Recognition**: Uses `speech_recognition` to capture and process voice commands.
2. **Text-to-Speech**: Implements `pyttsx3` for converting text responses to speech.
3. **YouTube Playback**: Integrates `pywhatkit` to play songs on YouTube.
4. **Date and Time**: Provides current date and time information.
5. **Wikipedia Search**: Fetches summaries from Wikipedia.
6. **Jokes**: Tells jokes using the `pyjokes` library.
7. **Web Browser**: Opens various websites like Google, YouTube, Instagram, Gmail, GitHub, and Stack Overflow.
8. **Google Search**: Conducts Google searches based on user queries.
9. **Location Services**: Finds and displays the user's current location on Google Maps.

## Installation

Before running the script, ensure you have the necessary libraries installed. You can install them using pip:

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes
```

## Usage

1. **Running the Assistant**: 
   - Run the script to start the assistant.
   - Speak clearly into your microphone when prompted.

2. **Voice Commands**:
   - **Greeting**: Say "hello" to start a conversation.
   - **Introduction**: Ask "who are you" to get a brief introduction.
   - **Capabilities**: Ask "What can you do" to know the assistant's capabilities.
   - **Play Music**: Say "play [song name]" to play a song on YouTube.
   - **Date and Time**: Say "date and time" or "time and date" for current date and time.
   - **Wikipedia Search**: Say "tell me about [topic]" or "wikipedia [topic]" to get information from Wikipedia.
   - **Tell a Joke**: Say "joke" to hear a joke.
   - **Google Search**: Say "search [query]" to search the query on Google.
   - **Open Websites**: Commands like "open Google", "open YouTube", "open Instagram", "open Gmail", "open GitHub", and "open Stack Overflow" will open respective websites.
   - **Location**: Say "my location" to find your current location on Google Maps.
   - **Exit**: Commands like "bye", "tata", "stop", or "thank you" will end the session.

## Example

```python
python mini_alexa.py
```

Speak the following commands to see Mini Alexa in action:
- "Hello"
- "Who are you?"
- "Play Shape of You"
- "Tell me about Python programming"
- "Tell me a joke"
- "Open YouTube"

## Contributing

Feel free to contribute to this project by submitting a pull request. You can help improve the assistant by adding more features or enhancing the existing ones.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Credits

Created by Pratik Kumar (or "Mister Pratik" if you prefer to keep the original credit as in the script).

## Issues

If you encounter any issues or have any questions, please open an issue on the GitHub repository.

---

Enjoy using Mini Alexa, your new virtual assistant!

# Speech to Text

This python application converts your speech to text. The output of your speech will be saved as speech_to_text.txt file in the same directory.

## Pre-reqs on MAC OS:

1. Use Homebrew to install the prerequisites portaudio library, then install PyAudio using pip:
```
brew install portaudio
pip3  install pyaudio
```
2. Install SpeechRecognition 
```
pip3  install SpeechRecognition
```
3. Ensure that your mic/speakers are working properly and the volume is on.

## How to run speech_to_text.py:

1. Copy and save speech_to_text.py to your PC.
2. Run the script in your terminal:
```

python3 speech_to_text.py

```
3.  Observe that the first message that shows up in your terminal is `Please speak now:` 

4. After you see that message, begin speaking.
5. Shortly after a message will displayed in the terminal saying `last sentence you spoke was saved in speech_to_text.txt`.
6. Naviagte to the directory from where you ran the script and open the file to view the text.

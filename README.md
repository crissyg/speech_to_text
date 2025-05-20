# Speech to Text Converter

This python application Python application converts spoken words into text using your computer’s microphone.  
The recognized speech is saved to a file named `speech_to_text.txt` in the same directory.

---

## Features

- Converts speech to text in real-time
- Saves the transcribed text to a file for later use
- Minimal and easy-to-understand codebase
- Cross-platform (instructions provided for macOS)

---

## Prerequisites (macOS)

1. **Install PortAudio (required for PyAudio):**
    ```bash
    brew install portaudio
    ```
2. **Install Python dependencies:**
    ```bash
    pip3 install pyaudio 
    pip3 install SpeechRecognition
    ```
3. **Check your hardware:**  
   Ensure your microphone and speakers are functioning and the volume is on.

---

## Usage

1. **Download the script:**  
   Save `speech_to_text.py` to your computer.

2. **Run the script in your terminal:**
    ```bash
    python3 speech_to_text.py
    ```

3. **Follow the prompts:**
    - When you see `Please speak now:`, begin speaking clearly into your microphone.
    - After processing, the application will confirm:  
      `Last sentence you spoke was saved in speech_to_text.txt`.

4. **View your transcription:**  
   Open `speech_to_text.txt` in the same directory to see your transcribed speech.

---

## Example Output

```
Please speak now:
[You speak your sentence aloud]
Last sentence you spoke was saved in speech_to_text.txt.
```

---

## Notes

- For best results, speak clearly and ensure minimal background noise.
- This application uses the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) and [PyAudio](https://pypi.org/project/PyAudio/) Python libraries.

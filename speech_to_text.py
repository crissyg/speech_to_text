'''
This app converts your speech to text. The output of your speech will be saved as
speech_to_text.txt file in the same directory.
'''
# Import Required Libraries
import speech_recognition

def record_voice():
	microphone = speech_recognition.Recognizer()	

	with speech_recognition.Microphone() as live_phone:
		microphone.adjust_for_ambient_noise(live_phone)

		print("Please speak now: ")
		audio = microphone.listen(live_phone)
		try:
			phrase = microphone.recognize_google(audio, language='en')
			return phrase
		except speech_recognition.UnkownValueError:
			return "I didn't understand what you said. Please try again."

if __name__ == '__main__':
	phrase = record_voice()

	with open('speech_to_text.txt','w') as file:
		file.write(phrase) 

	print('the last sentence you spoke was saved in speech_to_text.txt') 

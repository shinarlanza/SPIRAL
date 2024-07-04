import speech_recognition as voice
import pyttsx3 
import pyaudio
import pywhatkit
import wikipedia


recog = voice.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 125)
engine.say('Hello, I am your voice assistant.')
engine.runAndWait()

response = voice.Recognizer()

with voice.Microphone() as source:
	response.energy_threshold=10000
	response.adjust_for_ambient_noise(source,1.2)
	print("Listening...")
	audio = response.listen(source)
	text = response.google(audio)
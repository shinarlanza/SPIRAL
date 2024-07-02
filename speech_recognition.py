import speech_recognition 
import pyttsx3 
import pyaudio
import pywhatkit
import wikipedia


recognizer = speech_recognition.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 125)
engine.say('Say Hi to Spiral')
engine.runAndWait()

def response(text):
	engine.say(text)
	engine.runAndWait() 
	
def ask():
	with speech_recognition.Microphone() as microphone:
		recognizer.adjust_for_ambient_noise(microphone, duration = 1)
		print('Start')
		voice = recognizer.listen(microphone)

	try:
		speech = recognizer.recognize_google(voice)
		print(speech)

	except LookupError as error:
		print(f"An error occured: {error}")
	return(speech)

def run():
	try:
		talk = ask()
		if 'hi' in talk:
			response('hi i am spiral')	
			response('how are you?')
		elif 'play' in talk:
			song = talk.replace('play', '')
			response('playing ' + song)
			pywhatkit.playonyt(song)
		elif 'who is' in talk:
			person = talk.replace('who is', '')
			response('searching for ' + person)
			result = wikipedia.search(talk)
			result = wikipedia.summary(result, 2)
			response(result)
			print(result)
		elif 'what is' in talk:
			thing = talk.replace('what is', '')
			response('searching for ' + thing)
			result = wikipedia.search(thing)
			result = wikipedia.summary(result,3)
			print(result)
			response(result)
		else:
			response('I did not get it')
	
	except:
		print("Network error!")
		
run()	
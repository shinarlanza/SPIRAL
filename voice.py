import speech_recognition 
import pyttsx3 
import pyaudio
import pywhatkit
import wikipedia
import web_driver

recognizer = speech_recognition.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 125)
engine.say('Hi, I am SPIRAL. Your voice assistant.')
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


def search(query):
	try:
		assist = web_driver.inflow()
		text = assist.search_wikipedia(query)
		response(text) 
	except:
		print()	
	

def main():
	try:
		talk = ask()
		if 'hi' in talk:
			response('hi i am spiral')	
			response('how are you?')
		if 'play' in talk:
			song = talk.replace('play', '')
			response('playing ' + song)
			pywhatkit.playonyt(song)
		if 'who is' in talk:
			person = talk.replace('who is', '')
			response('searching for ' + person)
			search(person)
		if 'what is' in talk:
			thing = talk.replace('what is', '')
			response("searching {} in wikipedia".format(thing))
			search(thing)
	
	except:
		print("Network error!")

if __name__ == "__main__":
	main()
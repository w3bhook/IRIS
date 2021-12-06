import random as rnd
import time as t
import wolframalpha as wra
import speech_recognition as sr
import pyttsx3 as tts
import subprocess as sp

from gpiozero import LED as led

engine = tts.init()
r = sr.Recognizer()
wra = wra.Client("Y9G92A-94TV756H3T")
acronym = 'Intelligent but Retarded Information Supply'
keyword = 'iris'
blue = led(17)

snooze = rnd.choice([
	"IRIS Shutting Down",
	"Going to sleep",
	"Skipping the alarm"
])

songs = rnd.choice([
	'My sprinkler goes like thisstststststststststststststststststststststststst and comes back like titttttttttttttttttttttttttttttttttttttte.',
	'ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu',
	'The ting goes skrrrahh, pap pap kah-kah-kah Skidiki-pap-pap, and a puu-puu-poudrrr-boom Skiya, du-du-ku-ku-doom doom Poom poom, you dun now.',
	'a b c d e f g h i j k l m n o p q r s t u v w x y and zee',
	'a, b, c, d, e f g, h, i, j, k, l m n o p, q, r, s, t, u, v, w, x, y and zee'
])

quotes = rnd.choice([
	'It’s easy to love your partner, but sometimes the hardest lesson to remember is to love your enemy.',
	'The art of war is to defeat your enemies without fighting with them.',
	'The best sword will rust when putting in saltwater.',
	'There are paths which must not be pursued, forces which must not be invaded, towns which must not be occupied, places which must not be contested, commands of the monarch which must not be obeyed.',
	'Let your plans become dark and impenetrable as night, and collapse like a thunderbolt as you pass.',
	'All the battles are based on the deceptions.',
	'Rouse him, and know the meaning of his action or his inactivity. Force him to show himself so that he can figure out his weak spots',
	'The opportunities through which you can defeat your enemies are only given by the enemies.',
	'If command terms are not plain and distinct, instead, that command terms are not plain and distinct. Instead, the General is to blame because directives are not entirely grasped. Yet if his instructions are explicit, and still the soldiers disobey, then it’s their officers’ fault.” the General is to blame because directives are not completely grasped. Yet if his instructions are explicit, and still the soldiers disobey, then it’s their officers’ fault.',
	'Excellence is to break your enemies’ strength without fighting.',
	'When it’s attacked, every animal with blood in its veins and horns on its head will fight.',
	'Treat your man as you treat you, child, then he will stand for you in your darkest time.',
	'Create a scenario in such a way that the enemy will move backwards.',
	'Move as entirely as the wind is, and then become wood. Attack in a way as fire, but become a strong as the mountain is.',
	'If you very far from your enemies, then you should show your enemies that you are very close to them.'
])

class iris():

	def Start():
		engine.say(f"Hello! My name is IRIS. {acronym}. Please say something to start")
		engine.runAndWait()
		iris.Listen()

	def Stop(restart):
		if restart == True:
		    command = "/usr/bin/sudo /sbin/shutdown -c now"
		    process = sp.Popen(command, stdout=sp.PIPE)
		    output = process.communicate()[0]
		elif restart == False:
		    command = "/usr/bin/sudo /sbin/shutdown -h now"
		    process = sp.Popen(command, stdout=sp.PIPE)
		    output = process.communicate()[0]

	def GatherInfo(talk):
		res = client.query(talk)
		final = next(res.results).text
		iris.Speak(final)

	def Listen():
		while True:
			with sr.Microphone() as source:
				audio = r.listen(source)

			if listen_name:
				name = r.recognize_google(audio)
				name = name.lower()
				listen_name = False

			if "iris" in audio.lower():
				try:
					text = r.recognize_google(audio)
					text = text.lower()
					text = tedt.replace("iris", "")

					if "light" in text and "on" in text:
						if not blue:
							blue.on()

						blue = True
						engine.say(affirm)
						engine.runAndWait()

					elif "light" in text and "off" in text:
						if blue:
							blue.off()
						blue = False
						engine.say(affirm)
						engine.runAndWait()

					elif "shut" in text or "bye" in text:
						engine.say(snooze)
						engine.runAndWait()
						iris.Stop(False)

					elif "restart" in text:
						engine.say(snooze)
						engine.runAndWait()
						iris.Stop(True)

					elif "joke" in text or "jokes" in text:
						engine.say(jokes)
						engine.runAndWait()

					elif "quote" in text or "motivation" in text or "inspir" in text:
						engine.say(quotes)
						engine.runAndWait()

					elif "sing" in text or "song" in text:
						engine.say(songs)
						engine.runAndWait()

					elif "what" in text and "name" in text and "your" in text:
						engine.say("My name is IRIS, what's yours?")
						engine.runAndWait()
						listen_name = True

					else:
						iris.GatherInfo(text)
				except:
					engine.say("Oops. Something went wrong. Say something again.")
					engine.runAndWait()
					iris.Listen()

	def Speak(speech):
		engine.say(speech)
		engine.runAndWait()
		iris.Listen()

if __name__ == '__main__':
	iris.Start()

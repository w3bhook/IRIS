import random as rnd
import time as t
import wolframalpha as wra
import speech_recognition as sr
import pyttsx3 as tts
import subprocess as sp

engine = tts.init()
listener = sr.Recognizer()
wra = wra.Client("Y9G92A-94TV756H3T")
acronym = 'Intelligent but Retarded Information Supply'
keyword = 'iris'

print(sr.Microphone.list_microphone_names())
t.sleep(10)

songs = [
	'My sprinkler goes like thisstststststststststststststststststststststststst and comes back like titttttttttttttttttttttttttttttttttttttte.',
	'ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu ooluu lulu ooluuu luuluu',
	'The ting goes skrrrahh, pap pap kah-kah-kah Skidiki-pap-pap, and a puu-puu-poudrrr-boom Skiya, du-du-ku-ku-doom doom Poom poom, you dun now.',
	'a b c d e f g h i j k l m n o p q r s t u v w x y and zee',
	'a, b, c, d, e f g, h, i, j, k, l m n o p, q, r, s, t, u, v, w, x, y and zee'
]

quotes = [
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
]

class iris():

	def Start():
		engine.say(f"Hello! My name is IRIS. {acronym}. Please say something to start")
		engine.runAndWait()
		iris.Listen()

	def Stop(restart):
		if restart == True:
		    command = "/usr/bin/sudo /sbin/shutdown -c now"
		    process = sp.Popen(command.split(), stdout=sp.PIPE)
		    output = process.communicate()[0]
		elif restart == False:
		    command = "/usr/bin/sudo /sbin/shutdown -h now"
		    process = sp.Popen(command.split(), stdout=sp.PIPE)
		    output = process.communicate()[0]

	def GatherInfo(talk):
		if 'your name' in talk:
			engine.say("My name is IRIS. What's yours?")
			engine.runAndWait()
		elif 'sing' in talk:
			rnd_song = rnd.choice(songs)
			engine.say(rnd_song)
			engine.runAndWait()
		else:
			res = client.query(talk)
			final = next(res.results).text
			iris.Speak(final)

	def Listen():
		while True:
			with sr.Microphone(device_index=4) as source:
				audio = sr.listen()
			if "iris" in audio.lower():
				try:
					text = sr.recognize_google(audio)
					text = text.lower()
					iris.GatherInfo(text.replace("iris", ""))
				except:
					engine.say("Oops. Something went wrong. Say something again.")
					engine.runAndWait()
					iris.Listen()
			else:
				pass

	def Speak(speech):
		engine.say(speech)
		engine.runAndWait()
		iris.Listen()

if __name__ == '__main__':
	iris.Start()
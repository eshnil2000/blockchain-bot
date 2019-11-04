from flask import Flask, render_template, request, jsonify
import aiml
import os
#from chatterbot.trainers import ListTrainer
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
import requests
import json

app = Flask(__name__)

#bot=ChatBot('Test')
# trainer= ListTrainer(bot)
# for _file in os.listdir('files'):
# 	chats=open('files/' + _file, 'r').readlines()
# 	print(chats)
# 	trainer.train(chats)

#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train(
#    "chatterbot.corpus.english"
#)
# defining the api-endpoint  

API_ENDPOINT= "http://1572655316.proxy.chainapp.live/"
  
def make_data(sender,recipient,amount):
	return {'sender':sender,'recipient': recipient, 'amount': amount }

@app.route("/")
def hello():
	return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
	#message = request.form['messageText'].encode('utf-8').strip()
	message = request.form['messageText'].encode('utf-8').strip()
	message=str(message.decode('utf-8'))
	print("message is ", message)
	#kernel = aiml.Kernel()

	#if os.path.isfile("bot_brain.brn"):
	#    kernel.bootstrap(brainFile = "bot_brain.brn")
	#else:
	#    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
	#    kernel.saveBrain("bot_brain.brn")

	# kernel now ready for use
	while True:
		if message == "quit":
			exit()

		if  "@chain" in message:
			data= message.split()
			global API_ENDPOINT
			API_ENDPOINT= data[1]
			return jsonify({'status':'OK','answer':json.dumps("Monitoring chain @ "+API_ENDPOINT )})
		
		elif message == "/chain":
			#kernel.saveBrain("bot_brain.brn")
			response = requests.get(API_ENDPOINT+"chain")
			print(response.json())
			return jsonify({'status':'OK','answer':json.dumps(response.json())})
		
		elif message == "/mine":
			#kernel.saveBrain("bot_brain.brn")
			response = requests.get(API_ENDPOINT+"mine")
			print(response.json())
			return jsonify({'status':'OK','answer':json.dumps(response.json())})
		
		elif "/transaction/new" in message:
			parameters= message.split()
			print(parameters[1])
			sender= parameters[1]
			recipient = parameters[2]
			amount = parameters[3]  
			headers = {
			    'accept': 'application/json',
			    'Content-Type': 'application/json',
			}
			data=json.dumps(make_data(sender,recipient,amount))
			print(data)
			response = requests.post('http://1572841083.proxy.chainapp.live/transactions/new', headers=headers, data=data)
			print(response.json())
			return jsonify({'status':'OK','answer':json.dumps(response.json())})
				
			#exit()
		else:
			#bot_response =bot.get_response(message)
			bot_response = "I dont know"
			print("response is", bot_response)
			# print bot_response
			#return jsonify({'status':'OK','answer':bot_response})
			return jsonify({'status':'OK','answer':str(bot_response)})
						

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

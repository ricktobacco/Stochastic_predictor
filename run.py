# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/28 14:52:05 by scollet           #+#    #+#              #
#    Updated: 2017/09/28 14:52:06 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# importing the requests library
import requests
import objects
import time
import sys
import numpy as np
import csv
import os
import matplotlib.pyplot as plt 
import matplotlib.animation as animationa
## api-endpoint
URL = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
EPOCHS = 16
BATCH = 32
SAVE = "trained.h5"

# defining a params dict for the parameters to be sent to the API
#PARAMS = {'address':ticker}

# sending get request and saving the response as response object

# extracting data in json format

#for each, coin in data.items():
#    print coin
# extracting latitude, longitude and formatted address
# of the first matching location

#def learn(agent):
#	for inputs, prediction, result in agent.memory:
#		print each, memory
#		agent.train(inputs, result, validation_data=(X_test, Y_test), epochs=200, batch_size=5, verbose=0)

plt.ion()

def pull(n):
	try:
		r = requests.get(url = URL, params = {})
#	if r.status_code == requests.codes.ok:
		tape = r.json()
		X = []
		for each, coin in tape.items():
			if n and each == 'BTC': 
				X.append(coin)
			elif n == 0:
				X.append(coin)
		return X
	except:
		time.sleep(15)
		return(pull(n))

def plot(data, time):
#	plt.axis([0, 10, 0, 1])
    	y = data
    	plt.scatter(time, data)
    	plt.pause(0.05)

def run(args):
	agent = objects.Agent(45, 1)
	if os.path.isfile(SAVE):
		agent.load(SAVE)
	M = []
	while True:
		with open(objects.TAPE, 'w') as csvfile:	
			writer = csv.writer(csvfile, delimiter = ',')
			print("... collecting ...")
			for ok in range(2):
				for t in range(EPOCHS):
					print("\n\nITERATION : ", t)
					X = pull(0)
#					print
#					localtime = time.asctime(time.localtime(time.time()))
#					print("")
					print(len(M))
					if len(M) == 45:
						print("... predicting ...")
#						M.pop(0)
#						M.append()
						T = np.array([M])
						P = list(agent.model.predict(T)[0])
						print("prediction : ", P[0])
						time.sleep(30)
						R = pull(1)
						print("result : ", R[0])
						M.append(R[0])
						writer.writerow(M)
						M.pop(0)
					else:
						for i in X:
							M.append(i)		
#					agent.memory.append(M)
		agent.learn()
		agent.save(SAVE)

if __name__ == "__main__":
    run(sys.argv)

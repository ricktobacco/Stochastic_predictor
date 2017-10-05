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
EPOCHS = 12
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

def pull():
	r = requests.get(url = URL, params = {})
	if r.status_code == requests.codes.ok:
		tape = r.json()
		X = []
		for each, coin in tape.items():
			#if each == 'BTC'
			X.append(coin)
#	print X
		return X
	else:
		time.sleep(12)

def plot(data, time):
#	plt.axis([0, 10, 0, 1])
    	y = data
    	plt.scatter(time, data)
    	plt.pause(0.05)

def run(args):
	agent = objects.Agent(3, 3)
	if os.path.isfile(SAVE):
		agent.load(SAVE)
	while True:
		with open(objects.TAPE, 'w') as csvfile:	
			writer = csv.writer(csvfile, delimiter = ',')
			for t in range(EPOCHS):
				print("\n\nITERATION : ", t)
				X = pull()
				T = np.array([X])
#				print
				P = list(agent.model.predict(T)[0])
				localtime = time.asctime( time.localtime(time.time()) )
				print(P)
				time.sleep(12)
				R = pull()
				print(R)
				M = []
				for i in X:
					M.append(i)
				for j in R:
					M.append(j)
#				plot(M, t)
#				print(M, "\n\n")
				writer.writerow(M)
#				agent.memory.append(M)
		agent.learn()
		agent.save(SAVE)

if __name__ == "__main__":
    run(sys.argv)

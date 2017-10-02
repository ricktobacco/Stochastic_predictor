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
# api-endpoint
URL = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
EPOCHS = 42
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

def pull():
	r = requests.get(url = URL, params = {})
	tape = r.json()
	X = []
	for each, coin in tape.items():
		X.append(coin)
#	print X
	return X

def run(args):
	agent = objects.Agent(3, 3)
	if os.path.isfile(SAVE):
		agent.load(SAVE)
	while True:
		with open(objects.TAPE, 'wb') as csvfile:	
			writer = csv.writer(csvfile, delimiter = ',')
			for i in range(EPOCHS):
				print "\n\nITERATION : ", i
				X = pull()
				T = np.array([X])
#				print
				P = list(agent.model.predict(T)[0])
	      			print P
	       			time.sleep(5)
				R = pull()
#				print X
#				print agent.model.evaluate(np.array([P]), np.array([R]), verbose=0)
				print R
#				print X + R
				M = []
				for i in X:
					M.append(i)
				for j in R:
					M.append(j)
#				print M, "\n\n"
				writer.writerow(M)
#				agent.memory.append(M)
		agent.learn()
		agent.save(SAVE)

if __name__ == "__main__":
    run(sys.argv)

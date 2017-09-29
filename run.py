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

# api-endpoint
URL = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
EPOCHS = 6
BATCH = 32

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
	return list(X)

def run(args):
	agent = objects.Agent(3, 3)
	while True:
		for i in range(EPOCHS):
			X = np.array(pull()).reshape((1, 3))
#			print X
			P = agent.model.predict(X)
        		time.sleep(10)
			R = np.array(pull()).reshape((1, 3))
			print "\n\nITERATION : ", i
 	      		print P
#			print agent.model.evaluate(P, R, verbose=0)
			print R
			M = (X, P, R)
#			print M
			agent.memory.append(M)
		agent.learn()

if __name__ == "__main__":
    run(sys.argv)

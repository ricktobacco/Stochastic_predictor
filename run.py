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

# api-endpoint
URL = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
EPOCHS = 10
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
#	print X
	return X

def run(args):
	agent = objects.Agent(3, 3)
	while True:
		with open(agent.memory, 'wb') as csvfile:	
			writer = csv.writer(csvfile, delimiter = ',')
			for i in range(EPOCHS):
				X = pull()
				T = np.array([X])
#				print X
				P = agent.model.predict(T)
	       			time.sleep(10)
				R = pull()
				print "\n\nITERATION : ", i
	      			print P
#				print X
#				print agent.model.evaluate(P, R, verbose=0)
				print R
#				print X + R
				M = X + R
				print M
				writer.writerow(M)
#				agent.memory.append(M)
			agent.learn()

if __name__ == "__main__":
    run(sys.argv)

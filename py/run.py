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
from sklearn.model_selection import train_test_split
import pandas as pd

TAPE = "../tape.csv"
# api-endpoint
URL = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
EPOCHS = 2
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

def learn(agent):
	seed = 9
	np.random.seed(seed)
	dataset = np.loadtxt(fname = TAPE, delimiter = ',')
#		print reader
#		print temp
#               dataset = np.loadtxt(TAPE, delimiter=',')
	print dataset[:,0:3]
#               print dataset[:]
	X = dataset[:,0:3]
	Y = dataset[:,3:]
#               sys.exit(1)
#               minibatch = random.sample(self.memory, batch_size)
#               print self.memory
#               for inputs, results in self.memory:
#                       print "this", this                      
#                       if done:
#                               target[0][action] = reward
#                       else:
#                               a = self.model.predict(next_state)[0]
#                               t = self.target_model.predict(next_state)[0]
#                               target[0][action] = reward + self.gamma * t[np.argmax(a)]
#                       print "\n", inputs
#                       X = np.array([inputs])
#                       print "\n", X
#                       print results
#                       Y = np.array([results])
#                       print Y
#                       pass
#	print X, "\n\n"#.reshape(1, 3)
#	print Y#.reshape(1, 3)
	(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, test_size=0.33, random_state=seed)
	agent.model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=200, batch_size=5, verbose=0)
	print "loop"


def run(args):
	agent = objects.Agent(3, 3)
	while True:
		with open(TAPE, 'wb') as csvfile:	
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
		learn(agent)

if __name__ == "__main__":
    run(sys.argv)

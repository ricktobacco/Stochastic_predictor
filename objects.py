# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    objects.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/28 15:03:59 by scollet           #+#    #+#              #
#    Updated: 2017/09/28 15:04:00 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import backend as K
from keras import metrics
from collections import deque
import random
from sklearn.model_selection import train_test_split
import run

HIDDEN_LAYERS = 2
NEURAL_DENSITY = 32
LEARNING_RATE = 0.001
TAPE = "tape.csv"
BATCH = 5

class Agent():
	def __init__(self, input_size, output_size):
		self.input_size = input_size
		self.output_size = output_size
		self.learning_rate = LEARNING_RATE
		self.model = self._build_model()
		self.target_model = self._build_model()
		self.update_target_model()
		self.gamma = 0.95
		self.epsilon = 0.99
		self.epsilon_min = 0.01
		self.epsilon_decay = 0.99
		self.learning_rate = 0.001
	def _build_model(self):
		model = Sequential()
		model.add(Dense(NEURAL_DENSITY, input_dim=self.input_size, activation='linear'))
		for i in range(HIDDEN_LAYERS):
			model.add(Dense(NEURAL_DENSITY, activation='linear'))
		model.add(Dense(self.output_size, activation='linear'))
		model.compile(loss='mean_absolute_error', optimizer='adamax', metrics=[metrics.mae, metrics.binary_accuracy])
		return model
	def learn(self):
		seed = 42
		np.random.seed(seed)
		dataset = np.loadtxt(TAPE, delimiter=',')
#		X = []
#		Y = []
#		with open(TAPE) as fobj:
#			for line in fobj:
#			        row = line.split()
#        			X.append(np.array([row[0:3]]))
#			        Y.append(np.array([row[3:]]))
#		print data
#		print target
#			reader = csv.reader(csvfile, delimiter=',')
#			for row in reader:
#				X = list(row[i] for i in range(3))
#				Y = list(row[i] for i in [3:])
#		print X, Y
#		print(dataset)
#		print dataset[:]
		X = dataset[:,0:45]
		Y = dataset[:,45:]
#		sys.exit(1)
#		minibatch = random.sample(self.memory, batch_size)
#		print self.memory
#		for inputs, results in self.memory:
#			print "this", this			
#			if done:
#				target[0][action] = reward
#			else:
#				a = self.model.predict(next_state)[0]
#				t = self.target_model.predict(next_state)[0]
#				target[0][action] = reward + self.gamma * t[np.argmax(a)]
#			print "\n", inputs
#			X = np.array([inputs])
#			print "\n", X
#			print results
#			Y = np.array([results])
#			print Y
#			pass
#		print("X : ", X)
#		print("Y : ", Y)
		(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, test_size=0.33, random_state=seed)
#		X = np.array([X])
#		Y = np.array([Y])
#		X_train = X_train.reshape((3, 1))
#		X_text = X_test.reshape((3, 1))
#		Y_train = Y_train.reshape((3, 1))
#		Y_test = Y_test.reshape((3, 1))
		self.model.fit(X_train, Y_train, validation_data = (X_test, Y_test), epochs=10, batch_size=5, verbose=0)
#			self.model.fit(inputs, result, epochs=1, verbose=0)
	
	def update_target_model(self):
		self.target_model.set_weights(self.model.get_weights())
	def predict(self, X):
		self.model.predict(X)
	def memory(self):
		return self._memory
	def load(self, name):
		self.model.load_weights(name)
	def save(self, name):
		self.model.save_weights(name)

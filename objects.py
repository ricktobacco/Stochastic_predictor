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
from collections import deque
import random

HIDDEN_LAYERS = 3
NEURAL_DENSITY = 64
LEARNING_RATE = 0.001
DEQUE = 300

class Agent():
	def __init__(self, input_size, output_size):
		self.input_size = input_size
		self.output_size = output_size
		self.learning_rate = LEARNING_RATE
		self.model = self._build_model()
		self.memory = deque(maxlen=DEQUE)
		self.target_model = self._build_model()
		self.update_target_model()
		self.gamma = 0.95
		self.epsilon = 0.99
		self.epsilon_min = 0.01
		self.epsilon_decay = 0.99
		self.learning_rate = 0.001
	def _huber_loss(self, target, prediction):
		error = prediction - target
		return K.mean(K.sqrt(1 + K.square(error)) - 1, axis = -1)
	def _build_model(self):
		model = Sequential()
		model.add(Dense(NEURAL_DENSITY, input_dim=self.input_size, activation='relu'))
		for i in range(HIDDEN_LAYERS):
			model.add(Dense(NEURAL_DENSITY, activation='relu'))
		model.add(Dense(self.output_size, activation='softmax'))
		model.compile(loss=self._huber_loss, optimizer='adam', metrics=['accuracy'])
		return model
	def learn(self):
#		minibatch = random.sample(self.memory, batch_size)
		for inputs, prediction, result in self.memory:
#			if done:
#				target[0][action] = reward
#			else:
#				a = self.model.predict(next_state)[0]
#				t = self.target_model.predict(next_state)[0]
#				target[0][action] = reward + self.gamma * t[np.argmax(a)]
			self.model.fit(inputs, result, epochs=1, verbose=0)
		if self.epsilon > self.epsilon_min:
			self.epsilon *= self.epsilon_decay
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

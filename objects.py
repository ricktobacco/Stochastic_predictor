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

HIDDEN_LAYERS = 2
NEURAL_DENSITY = 32
LEARNING_RATE = 0.001

class Agent():
	def __init__(self, input_size, output_size):
		self.input_size = input_size
		self.output_size = output_size
		self.learning_rate = LEARNING_RATE
		self.model = self._build_model()
		self.target_model = self._build_model()
		self.update_target_model()
	def _huber_loss(self, target, prediction):
		error = prediction - target
		return K.mean(K.sqrt(1 + K.square(error)) - 1, axis = -1)
	def _build_model(self):
		model = Sequential()
		model.add(Dense(NEURAL_DENSITY, input_dim=self.input_size, activation='relu'))
		for i in range(HIDDEN_LAYERS):
			model.add(Dense(NEURAL_DENSITY, activation='relu'))
		model.add(Dense(self.output_size, activation='softmax'))
		model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
		return model
	def update_target_model(self):
		self.target_model.set_weights(self.model.get_weights())
	def train(self, feed, target):
		self.model.fit(feed, target, epochs=1, verbose=0)
	def predict(self, X):
		self.model.predict(X)
	def load(self, name):
		self.model.load_weights(name)
	def save(self, name):
		self.model.save_weights(name)

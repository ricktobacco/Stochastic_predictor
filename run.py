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

# api-endpoint
URL = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"

# location given here
location = "CryptoCompare"

# defining a params dict for the parameters to be sent to the API
#PARAMS = {'address':ticker}

# sending get request and saving the response as response object

# extracting data in json format

for each, coin in data.items():
    print coin
# extracting latitude, longitude and formatted address
# of the first matching location

def run(args):
    agent = objects.Agent(3, 3)
    while True:
        r = requests.get(url = URL, params = {})
        tape = r.json()
        X = np.array()
        for each, coin in tape.items():
            X.append(coin)
        P = agent.model.predict(X)
        time.sleep(10)
        R = requests.get(url = URL, params = {})
        M = [P, R]
        print M
        model.memory.append([P, R])

if __name__ == "__main__":
    run(sys.argv)

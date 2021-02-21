# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:49:50 2021

@author: Samy Ayed
"""

from nltk_utils import preprocess_sentence, vectorize_new
import json
import torch
import pickle
import random
from model import Net

with open('intents.json','r', encoding='utf-8') as f:
    intents = json.load(f)

with open('vect.pkl', 'rb') as f:
    vect = pickle.load(f)

FILE = 'data.pth'
data = torch.load(FILE)

n_inputs = data['n_inputs']
hidden1 = data['hidden1']
hidden2 = data['hidden2']
n_outputs = data['n_outputs']
model_state = data["model_state"]
tags = data["tags"]
tags = sorted(set(tags.reshape(-1)))
model = Net([n_inputs,hidden1,hidden2,n_outputs])
model.load_state_dict(model_state)
model.eval()

bot_name = "Assistant"
print("Un assistant est là pour répondre à toutes vos questions au sujet du Coronavirus. Ecrivez 'stop' pour quitter la discussion.")

while True:
    sentence = input("Vous: ")
    if sentence == 'stop':
        break
    sentence = preprocess_sentence(sentence)
    X = vectorize_new(vect, sentence)
    X = X.reshape(1, -1)
    X = torch.from_numpy(X).float()
    z = model(X) # forward propagation to obtain the outputs
    _, yhat = torch.max(z, dim=1) # max of the outputs of the neural network with its index 'yhat'
    probs = torch.softmax(z, dim=1) # apply the softmax function to the outputs tensor to obtain respective probabilities
    prob = torch.max(probs) # max probability gives us the strength of the prediction and indicates how much we can be confident
    tag = tags[yhat]
    print(probs)
    print(prob)  
    print(tag)
    if prob.item() < 0.75:
        print(f"{bot_name}: Je ne comprends pas...")
    else:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
        
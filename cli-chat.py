# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:49:50 2021

@author: Samy Ayed
"""

from get_response import get_response

bot_name = "Assistant"
print("Un assistant virtuel est là pour répondre à toutes vos questions au sujet du Coronavirus. Ecrivez 'stop' pour quitter la discussion.")

while True:
    sentence = input("Vous: ")
    if sentence == 'stop':
        break
    print(bot_name + ': ' + get_response(sentence))
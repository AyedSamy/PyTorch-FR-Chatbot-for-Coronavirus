# PyTorch FR Coronavirus Chatbot
![Python 3.7](https://img.shields.io/static/v1?label=Python&message=3.7&color=3776AB&logo=python) ![PyTorch](https://img.shields.io/static/v1?label=Library&message=PyTorch&color=EE4C2C&logo=PyTorch) ![Scikit-learn](https://img.shields.io/static/v1?label=Library&message=Scikit-learn&color=F7931E&logo=scikit-learn)


This project is about the creation of a **French-speaking chatbot** (virtual assistant) that answers user questions about **Coronavirus**. This chatbot implemented in **Python** uses a Deep Learning library, **PyTorch**, giving us the tools to build a **neural network model** that is required to make complex classification.

The neural network is based on training data provided in a **JSON** file. This file is composed of different **intents**:
Each intent gathers a few **patterns** (questions) written by users about differents topics focused on the Coronavirus (what is the coronavirus, its symptoms, how to wear a mask, etc), and also the associated **label** (or tag) for each pattern. This allows us to train the neural network model in a **supervised** manner. A list of **responses** is also available to make our chatbot able to speak and reply to users.

As of now, the intents our French Chatbot can understand are the following : *aide psychologique*, *au revoir*, *coronavirus*, *couvre-feu*, *dépistage*, *déplacement*, *gestes barrières*, *merci*, *port du masque*, *salutation*, *symptômes*.

The current version of the app can be run on **CLI** via the following procedure:

`pip install -r requirements.txt`

`python cli-chat.py`

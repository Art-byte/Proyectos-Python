import nltk
import numpy as np
import random
import string

f = open("C:\\Users\\Artur\\Desktop\\ChatBot\\Otro.txt", "r", errors="ignore")
raw = f.read()

raw = raw.lower()


# convierte a una lista de sentencias
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)  # lo convierte en una lista de palabras

# Se toman como entrada los tokens y devolverá tokens normalizados.

lammer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return[lammer.lemmatize(token) for token in tokens]
remove_punch_dict = ((ord(punct), None)for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().traslate(remove_punch_dict)))


# Función de saludo a través el bot.
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "hola","Que onda", "Que tal", "Que pex", "Que show")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there",
                      "hello", "I am glad! You are talking to me", "Hola", "Que tal", "Que hongo", "Que hay", "Holo"]


def greeting(sentence):
    for palabra in sentence.split():
        if palabra.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Función de Respuesta 
def response(user_response):
    robo_response = ""
    sent_tokens.append(user_response)

TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="Eng")
tfidf = TfidfVec.fit_transform(sent_tokens)
vals = cosine_similarity(tfidf[-1], tfidf)
idx = vals.argsort()[0][-2]
flat = vals.flatten()
flat.sort()
req_tfidf = flat[-2]

if(req_tfidf == 0):
    robo_response = robo_response + "mmm no te endiendo"
    print(robo_response)

else:
    robo_response = robo_response+sent_tokens[idx]
    print(robo_response)

# Finalmente, alimentaremos las
# líneas que queremos que diga nuestro robot al iniciar y finalizar una conversación, según la información del usuario.

flag = True
print("ROBO: Hola, soy el chat bot type Bye!")
while(flag == True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response != "adios"):
        if(user_response == "gracias" or user_response == "Que buena onda"):
            flag = False
            print("ROBO: De nada")
        else:
            if(greeting(user_response) != None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("ROBO: Bye! take care..")

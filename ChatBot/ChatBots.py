#import nltk
from nltk.chat.util import Chat, reflections


mis_reflexions = {
"ir": "fui",
"hola": "hey",

}


pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estas ?",]
    ],
     [
        r"cual es tu nombre ?",
        ["Mi nombre es Chatbot",]
    ],
    [
        r"¿como estas ?|¿como te va?|¿que hay de nuevo|¿como andamos?|(.*)que pedo|que pedal|que hay|¿como te va?",
        ["bien y tu?","bien","chido","todo tranquilo","normal","ahi andamos","pues estoy"]
    ],
    [
        r"disculpa(.*)|perdon(.*)|bien(.*)",
        ["No pasa nada","no hay problema","no te preocupes","no importa","no hay cuidado","esta bien"]
    ],
    [
        r"hola|hey|buenas|que tal|como estamos|holo|que onda|que hay",
        ["Hola", "que tal","como estas","como te va","que hay","como andas"]
    ],
    [
        r"¿que (.*) quieres ?|¿que se te ofrece?|¿que(.*) necesitas?",
        ["Nada gracias","nada","no nada"]
        
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
     [
        r"(.*)¿enserio?|(.*)es broma verdad?|no te creo|aja|mames",
        ["Es broma solo tienes un resfriado",]
    ],
     [
        r"(.*)seguro?|(.*)enserio?|(.*)de verdad?",
        ["Muy seguro","de verdad","oooots","yo cuando te he mentido?"]
    ],
     [
        r"(.*)dolor de cabeza|(.*)escurrimiento nasal|(.*)mocos|(.*)Temperatura|(.*)cuerpo cortado|(.*)me duele la cabeza",
        ["es posible que te hayas enfermado",]
    ],
     [
        r"(.*)¿Cómo de que?",
        ["puede que sea gripa","Tal vez tengas dolor migraña","quizas es un resfriado"]
    ],
    [
        r"finalizar|adios|nos vemos| hasta luego|bye|ciao|camara",
        ["ciao","Fue bueno hablar contigo","te cuidas","cuidate","nos vemos","byebye"]
],
    [
        r"(.*)mal|(.*)me siento mal|(.*)ando malo|(.*)me siento raro|(.*)estoy mal|(.*)No me siento bien",
        ["Puedes decime que sientes?","¿cuales dirias que son tus sintomas?"]
],  
  
]
def chatear():
    print("Hola soy un bot") #mensaje por defecto
    chat = Chat(pares, mis_reflexions)
    chat.converse()
if __name__ == "__main__":
    chatear()
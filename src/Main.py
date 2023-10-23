'''
Created on 31 lug 2023

@author: Rodolfo Pio Sassone
'''
'''
if __name__ == '__main__':
    pass
'''
from tressette import Gioco


def ordine_turni():     #ATTENZIONE!!! NESSUN CONTROLLO SULL'INPUT!
    print("**********************INSERISCI ORDINE TURNI*****************************")
    l = []
    print("\"me\" per l'agente\n\"avv1\" per l'avversario\n\"compagno\" per il compagno di squadra dell'agente")
    primog = input("Primo giocatore:")  
    secondog = input("Secondo giocatore:")
    l.append(primog.lower())
    l.append(secondog.lower())
    if primog == "avv1" and secondog == "me":
        l.append("avv2")
        l.append("compagno")
    elif primog == "avv1" and secondog == "compagno":
        l.append("avv2")
        l.append("me")
    elif primog == "me" and secondog == "avv1":
        l.append("compagno")
        l.append("avv2")
    elif primog == "compagno" and secondog == "avv1":
        l.append("me")
        l.append("avv2")
        
    return l   

gioco = Gioco(ordine_turni())
gioco.play()
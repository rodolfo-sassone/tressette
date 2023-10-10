'''
Created on 31 lug 2023

@author: Rodolfo Pio Sassone
'''
from pyswip import Prolog

p = Prolog()
p.consult("tressette.pl")
p.assertz("prop(sette_denari,uscita,si)")
who = "compagno"
for a in p.query("search_napoli(" + who.lower() + ",coppe)"):
    print(a)


'''
for a in prolog.query("rimanenti_a(P,L,N)"):
    print("Palo:", a["P"])
    print("Carte:")
    for c in a["L"]:
        print(c)
    print("#:", a["N"])
    print("---------------")
'''
'''
for i in range(3):
        carta = input("inserisci carta:")
        #print("prop("+carta+",possessore,giocatore(me))")
        prolog.assertz("prop("+carta+",possessore,giocatore(me))")

#list(prolog.query("mazzo(me,M)"))

for a in prolog.query("mazzo(me,M)"):
    for c in a["M"]:
        print(c)
'''
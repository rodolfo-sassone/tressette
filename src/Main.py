'''
Created on 31 lug 2023

@author: Rodolfo Pio Sassone
'''
'''
if __name__ == '__main__':
    pass
'''
from pyswip import Prolog
    
stringhe = ["asso_denari", "due_denari", "tre_denari", "dieci_denari", "nove_denari", "otto_denari", "sette_denari", "sei_denari", "cinque_denari", "quattro_denari", "asso_coppe", "due_coppe", "tre_coppe", "dieci_coppe", "nove_coppe", "otto_coppe", "sette_coppe", "sei_coppe", "cinque_coppe", "quattro_coppe", "asso_spade", "due_spade", "tre_spade", "dieci_spade", "nove_spade", "otto_spade", "sette_spade", "sei_spade", "cinque_spade", "quattro_spade", "asso_bastoni", "due_bastoni", "tre_bastoni", "dieci_bastoni", "nove_bastoni", "otto_bastoni", "sette_bastoni", "sei_bastoni", "cinque_bastoni", "quattro_bastoni"]

class search_napoli(object):
    def __init__(self, who, t=False):
        self.who = who
        self.trovato = t
        
    def palo(self, p):
        for _ in p.query("search_napoli(" + self.who.lower() + ",denari)"):
            p.assertz("prop(asso_denari,possessore,giocatore(" + self.who.lower() + "))")
            p.assertz("prop(due_denari,possessore,giocatore(" + self.who.lower() + "))")
            p.assertz("prop(tre_denari,possessore,giocatore(" + self.who.lower() + "))")
            self.trovato = True
            
        for _ in p.query("search_napoli(" + self.who.lower() + ",coppe)"):
            p.assertz("prop(asso_coppe,possessore,giocatore(" + self.who.lower() + "))")
            p.assertz("prop(due_coppe,possessore,giocatore(" + self.who.lower() + "))")
            p.assertz("prop(tre_coppe,possessore,giocatore(" + self.who.lower() + "))")
            self.trovato = True
            
        for _ in p.query("search_napoli(" + self.who.lower() + ",spade)"):
            p.assertz("prop(asso_spade,possessore,giocatore(" + self.who.lower() + "))")
            p.assertz("prop(due_spade,possessore,giocatore(" + self.who.lower() + "))")
            p.assertz("prop(tre_spade,possessore,giocatore(" + self.who.lower() + "))")
            self.trovato = True
            
        for _ in p.query("search_napoli(" + self.who.lower() + ",bastoni)"):
            p.assertz("prop(asso_bastoni,possessore,giocatore(" + self.who.lower() + "))")
            p.assertz("prop(due_bastoni,possessore,giocatore(" + self.who.lower() + "))")
            p.assertz("prop(tre_bastoni,possessore,giocatore(" + self.who.lower() + "))")
            self.trovato = True
            
def check_mazzo(p):
    punti = 0
    for a in p.query("a_monte(R)"):
        if a["R"] == "si":
            r = input("---- Meno di un punto e una figura. A monte? (Y/N)")
            if r.upper() == "Y":
                return True, punti
            
    for a  in p.query("napoli(P,me)"):
        print("---- Busso. Napoli ----")
        punti = punti+3
        
    for a in p.query("corona_asso(me)"):
        print("---- Busso. Corona di assi ----")
        punti = punti+4
    
    for a in p.query("corona_due(me)"):
        print("---- Busso. Corona di due ----")
        punti = punti+4
    
    for a in p.query("corona_tre(me)"):
        print("---- Busso. Corona di tre ----")
        punti = punti+4
    
    for a in p.query("bongioco_asso(me)"):
        print("---- Busso. Bongioco di assi ----")
        punti = punti+3
        
    for a in p.query("bongioco_due(me)"):
        print("---- Busso. Bongioco di due ----")
        punti = punti+3
        
    for a in p.query("bongioco_tre(me)"):
        print("---- Busso. Bongioco di tre ----")
        punti = punti+3
                
    return False, punti

    
def inserisci_mazzo(p):
    print("**********************INSERISCI MAZZO********************************")
    for _ in range(10):
        
        c = input("inserisci carta:")
        if c.lower() in stringhe:
            p.assertz("prop("+ c.lower() +",possessore,giocatore(me))")

        else:
            print("-stringa errata, riprova")
            while c.lower() not in stringhe:
                c = input("inserisci carta:")
                if c.lower() in stringhe:
                    p.assertz("prop("+ c.lower() +",possessore,giocatore(me))")
        
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
        
def mano(p, o, i, m, list_sn):
    c = []
    print("----------------------------------------------------------------------------------------")
    for j in range(4):
        if o[i] == "me":
            for a in p.query("seleziona("+str(m)+",C)"):
                c.append(a["C"])
                #print(a["C"])
                print("Butta: " + a["C"])
        else:
            carta = input("Turno di " + o[i] + " che butta: ")
            if carta.lower() in stringhe:
                c.append(carta.lower())
                p.assertz("prop("+c[j]+",possessore,giocatore("+o[i]+"))")
            else:
                while carta not in stringhe:
                    carta = input("Turno di " + o[i] + " che butta: ")
                    if carta.lower() in stringhe:
                        c.append(carta.lower())
                        p.assertz("prop("+c[j]+",possessore,giocatore("+o[i]+"))")
            
        p.assertz("prop("+c[j]+",terra,"+str(m)+")")
        if j == 0:
            for a in p.query("prop("+c[j]+",palo,P)"):
                palo = a["P"]
            p.assertz("palo("+str(m)+","+palo+")")
        i = (i+1)%4

    for a in p.query("presa("+str(m)+",G,"+palo+")"):
        i = o.index(a["G"])
    
    #al termine della mano controlliamo se riusciamo a dedurre il palo di una napoli di cui non abbiamo ancora dedotto il palo
    for sn in list_sn:
        if sn != None:
            if not sn.trovato:
                sn.palo(p)
    punti = 0
    punti_avv = 0
    for carta in c:
        for a in p.query("prop("+carta+",punti,P)"):
            if o[i] == 'me' or o[i] == 'compagno':
                punti = punti + a['P']
                if m == 9:  #chiusura
                    punti = punti + 1
            else:
                punti_avv = punti_avv + a['P']
                if m == 9:  #chiusura
                    punti_avv = punti_avv + 1  
                      
    for j in range(4):
        p.assertz("prop("+c[j]+",uscita,si)")
           
    return punti, punti_avv, i


def check_busso(p):     #ATTENZIONE!!! NESSUN CONTROLLO SULL'INPUT!
    list_sn = []
    punti = 0
    punti_avv = 0
    
    print("rispondi \"nessuno\" se nessuno o nessun'altro ha bussatto. Solo il busso: niente palo o pezzo.\nScrivi \"monte\" se qualcuno manda a monte.")
    
    who = input("Qualcuno ha bussato?")
    if who.lower() == "me":
        print("Lo so se ho bussato. Intendo gli altri.")
        
    if who.lower() == "monte":
        return True, list_sn, punti, punti_avv
    
    while who.lower() != "nessuno":
        sn = None
        what = input("Cosa ha fatto?")
        
        if what.lower() == "napoli":
            sn = search_napoli(who)
            sn.palo(p)
            if not sn.trovato:
                list_sn.append(sn)

            if who.lower() == "compagno":
                punti = punti+3
            else:
                punti_avv = punti_avv+3
                
        elif what.lower() == "bongioco":
            t = input("Di?(asso/due/tre)")
            m = input("Mancante?(denari,spade,coppe,bastoni)")
            lp = ["denari","spade","coppe","bastoni"]
            lp.remove(m.lower())
            
            for palo in lp:
                p.assertz("prop("+t+"_"+palo+",possessore,giocatore("+who.lower()+"))")
            
            if who.lower() == "compagno":
                punti = punti+3
            else:
                punti_avv = punti_avv+3
                 
        elif what.lower() == "corona":
            lp = ["denari","spade","coppe","bastoni"]
            t = input("Di?(asso/due/tre)")
            
            for palo in lp:
                p.assertz("prop("+t+"_"+palo+",possessore,giocatore("+who.lower()+"))")
                
            if who.lower() == "compagno":
                punti = punti+4
            else:
                punti_avv = punti_avv+4
        
        who = input("Qualcun'altro ha bussato?")
        
    return False, list_sn, punti, punti_avv
            
def round_game(p, o, i):
    punti_round = 0
    punti_round_avv = 0
    
    inserisci_mazzo(p)
    a_monte, punti_busso = check_mazzo(p)
    punti_round = punti_round + punti_busso
    if a_monte:  #true se l'agente butta a monte
        return punti_round, punti_round_avv
    
    a_monte, list_sn, punti_busso, punti_busso_avv = check_busso(p)
    punti_round = punti_round + punti_busso
    punti_round_avv = punti_round_avv + punti_busso_avv
    if a_monte:   #true se qualcun'altro butta a monte
        return punti_round, punti_round_avv
    
    print("*****************************INIZIO ROUND*************************************")
    
    for m in range(10):      
        punti_mano, punti_mano_avv, i = mano(p, o, i, m, list_sn)
        
        punti_round = punti_round + punti_mano
        punti_round_avv = punti_round_avv + punti_mano_avv
    
    print("*****************************FINE ROUND*************************************")   
    print("PUNTI ROUND: " + str(int(punti_round)))
    print("PUNTI ROUND AVVERSARI: " + str(int(punti_round_avv)))
    
    return punti_round, punti_round_avv

def clearKB(p):
    p.query("retractall(prop(X,terra,N))")
    p.query("retractall(prop(X,possessore,giocatore(G)))")
    p.query("retractall(prop(X,uscita,si))")
    p.query("retractall(palo(T,P))")
    
def gioco(p):
    non_finita = True
    tot_punti=0
    tot_punti_avv=0
    
    i_ordine = 0
    inizio = 0
    o = ordine_turni()
    
    while non_finita:
        punti, punti_avv = round_game(p, o, i_ordine)
        
        tot_punti = tot_punti + punti
        tot_punti_avv = tot_punti_avv + punti_avv
        
        print("PUNTI TOTALI: " + str(int(tot_punti)))
        print("PUNTI TOTALI AVVERSARI: " + str(int(tot_punti_avv)))
        
        
        if tot_punti >= 31 and tot_punti > tot_punti_avv:
            print("****************************VITTORIA!!***************************************")
            non_finita = False
            
        elif tot_punti_avv >= 31 and tot_punti_avv > tot_punti:
            print("____________________PECCATO. ABBIAMO PERSO._______________________________")
            non_finita = False
                
        i_ordine = (inizio+1)%4
        #pulisce KB dalle info del round_game terminato
        clearKB(p)
    
    
p = Prolog()
p.consult("tressette.pl")

gioco(p)
from pyswip import Prolog
from search import search_napoli
from myBN import TressetteVE

class Gioco(object):
    def __init__(self, ordine, bn = False):
        self.ordine = ordine
        self.p = Prolog()
        self.p.consult('Tressette/src/tressette.pl')
        self.punti = 0
        self.punti_avv = 0
        self.non_finita = True
        self.carte = ["asso_denari", "due_denari", "tre_denari", "dieci_denari", "nove_denari", "otto_denari", "sette_denari", "sei_denari", "cinque_denari", "quattro_denari", "asso_coppe", "due_coppe", "tre_coppe", "dieci_coppe", "nove_coppe", "otto_coppe", "sette_coppe", "sei_coppe", "cinque_coppe", "quattro_coppe", "asso_spade", "due_spade", "tre_spade", "dieci_spade", "nove_spade", "otto_spade", "sette_spade", "sei_spade", "cinque_spade", "quattro_spade", "asso_bastoni", "due_bastoni", "tre_bastoni", "dieci_bastoni", "nove_bastoni", "otto_bastoni", "sette_bastoni", "sei_bastoni", "cinque_bastoni", "quattro_bastoni"]
        if bn:
            self.bn = TressetteVE()
        else:
            self.bn = None

    def play(self):
        i_ordine = 0
        inizio = 0
        
        while self.non_finita:
            punti, punti_avv = self.round_game(i_ordine)
            
            self.punti = self.punti + punti
            self.punti_avv = self.punti_avv + punti_avv
            
            print("PUNTI TOTALI: " + str(int(self.punti)))   #cast a int per arrotondare
            print("PUNTI TOTALI AVVERSARI: " + str(int(self.punti_avv)))
            
            
            if self.punti >= 31 and self.punti > self.punti_avv:
                print("****************************VITTORIA!!***************************************")
                self.non_finita = False
                
            elif self.punti_avv >= 31 and self.punti_avv > self.punti:
                print("____________________PECCATO. ABBIAMO PERSO._______________________________")
                self.non_finita = False
                    
            i_ordine = (inizio+1)%4
            #pulisce KB dalle info del round_game terminato
            self.clearKB()


    def round_game(self,i):
        punti_round = 0
        punti_round_avv = 0
        
        self.inserisci_mazzo()
        a_monte_me, punti_busso_me = self.check_mazzo()
        punti_round = punti_round + punti_busso_me
        
        a_monte, list_sn, punti_busso, punti_busso_avv = self.check_busso()
        punti_round = punti_round + punti_busso
        punti_round_avv = punti_round_avv + punti_busso_avv
        if a_monte or a_monte_me:   #true se qualcuno butta a monte
            return punti_round, punti_round_avv
        
        print("*****************************INIZIO ROUND*************************************")
        
        for m in range(10):      
            punti_mano, punti_mano_avv, i = self.mano(i, m, list_sn)
            
            punti_round = punti_round + punti_mano
            punti_round_avv = punti_round_avv + punti_mano_avv
        
        print("*****************************FINE ROUND*************************************") 
        print("PUNTI ROUND: " + str(int(punti_round)))
        print("PUNTI ROUND AVVERSARI: " + str(int(punti_round_avv)))
        
        return punti_round, punti_round_avv
    

    def inserisci_mazzo(self):
        mazzo = []
        print("**********************INSERISCI MAZZO********************************")
        for _ in range(10):
            
            c = input("inserisci carta:")
            if c.lower() in self.carte:
                self.p.assertz("prop("+ c.lower() +",possessore,giocatore(me))")
                mazzo.append(c.lower())
            else:
                print("-stringa errata, riprova")
                while c.lower() not in self.carte:
                    c = input("inserisci carta:")
                    if c.lower() in self.carte:
                        self.p.assertz("prop("+ c.lower() +",possessore,giocatore(me))")
                        mazzo.append(c.lower())

        if self.bn != None:
            self.bn.set_mazzo(mazzo)

    def check_mazzo(self):
        punti = 0
        for a in self.p.query("a_monte(R)"):
            if a["R"] == "si":
                r = input("---- Meno di un punto e una figura. A monte? (Y/N)")
                if r.upper() == "Y":
                    return True, punti
                
        for a  in self.p.query("napoli(P,me)"):
            print("---- Busso. Napoli ----")
            punti = punti+3
            
        for a in self.p.query("corona_asso(me)"):
            print("---- Busso. Corona di assi ----")
            punti = punti+4
        
        for a in self.p.query("corona_due(me)"):
            print("---- Busso. Corona di due ----")
            punti = punti+4
        
        for a in self.p.query("corona_tre(me)"):
            print("---- Busso. Corona di tre ----")
            punti = punti+4
        
        for a in self.p.query("bongioco_asso(me)"):
            print("---- Busso. Bongioco di assi ----")
            punti = punti+3
            
        for a in self.p.query("bongioco_due(me)"):
            print("---- Busso. Bongioco di due ----")
            punti = punti+3
            
        for a in self.p.query("bongioco_tre(me)"):
            print("---- Busso. Bongioco di tre ----")
            punti = punti+3
                    
        return False, punti
    

    def check_busso(self):     #ATTENZIONE!!! NESSUN CONTROLLO SULL'INPUT!
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
                sn.palo(self.p)
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
                    self.p.assertz("prop("+t+"_"+palo+",possessore,giocatore("+who.lower()+"))")
                
                if who.lower() == "compagno":
                    punti = punti+3
                else:
                    punti_avv = punti_avv+3
                    
            elif what.lower() == "corona":
                lp = ["bastoni","spade","coppe","bastoni"]
                t = input("Di?(asso/due/tre)")
                
                for palo in lp:
                    self.p.assertz("prop("+t+"_"+palo+",possessore,giocatore("+who.lower()+"))")
                    
                if who.lower() == "compagno":
                    punti = punti+4
                else:
                    punti_avv = punti_avv+4
            
            who = input("Qualcun'altro ha bussato?")
            
        return False, list_sn, punti, punti_avv
    

    def mano(self, i, m, list_sn):
        palo = None
        terra = []
        bn_flag = (self.bn != None)
        c = []
        print("----------------------------------------------------------------------------------------")
        for j in range(4):
            if self.ordine[i] == "me":
                if bn_flag: #BN
                    carta = self.bn.query(j, terra, palo)
                    c.append(carta)
                    print("Butta: " + carta)
                else:   #DN
                    for a in self.p.query("seleziona("+str(m)+",C)"):
                        c.append(a["C"])
                        print("Butta: " + a["C"])
            else:
                carta = input("Turno di " + self.ordine[i] + " che butta: ")
                if carta.lower() in self.carte:
                    c.append(carta.lower())
                    self.p.assertz("prop("+c[j]+",possessore,giocatore("+self.ordine[i]+"))")
                    if bn_flag: 
                        self.bn.append_uscita(carta.lower())
                        terra.append(carta.lower())
                else:
                    while carta not in self.carte:
                        carta = input("Turno di " + self.ordine[i] + " che butta: ")
                        if carta.lower() in self.carte:
                            c.append(carta.lower())
                            self.p.assertz("prop("+c[j]+",possessore,giocatore("+self.ordine[i]+"))")
                            if bn_flag: 
                                self.bn.append_uscita(carta.lower())
                                terra.append(carta.lower())
            self.p.assertz("prop("+c[j]+",terra,"+str(m)+")")
            if j == 0:
                for a in self.p.query("prop("+c[j]+",palo,P)"):
                    palo = a["P"]
                self.p.assertz("palo("+str(m)+","+palo+")")
            i = (i+1)%4

        for a in self.p.query("presa("+str(m)+",G,"+palo+")"):
            i = self.ordine.index(a["G"])
        
        #al termine della mano controlliamo se riusciamo a dedurre il palo di una napoli di cui non abbiamo ancora dedotto il palo
        for sn in list_sn:
            if sn != None:
                if not sn.trovato:
                    sn.palo(self.p)
        punti = 0
        punti_avv = 0
        for carta in c:
            for a in self.p.query("prop("+carta+",punti,P)"):
                if self.ordine[i] == 'me' or self.ordine[i] == 'compagno':
                    punti = punti + a['P']
                else:
                    punti_avv = punti_avv + a['P']

        #chiusura
        if m == 9:
            if self.ordine[i] == 'me' or self.ordine[i] == 'compagno':
                punti = punti + 1
            else:
                punti_avv = punti_avv + 1
                        
        for j in range(4):
            self.p.assertz("prop("+c[j]+",uscita,si)")
            
        return punti, punti_avv, i

    def clearKB(self):
        self.p.retractall("(prop(X,terra,N))")
        self.p.retractall("(prop(X,possessore,giocatore(G)))")
        self.p.retractall("(prop(X,uscita,si))")
        self.p.retractall("(palo(T,P))")
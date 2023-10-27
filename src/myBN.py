import random
from aipython.probVariables import Variable
from aipython.probFactors import Prob
from aipython.probGraphicalModels import BeliefNetwork
from aipython.probVE import VE 
from enum import Enum
import numpy as np
from carte import CartaNapoletana

boolean = [True, False]

class Palo(Enum):
    DENARI = 0
    COPPE = 1
    SPADE = 2
    BASTONI = 3

palo = Variable('Palo',[Palo.DENARI.value, Palo.COPPE.value, Palo.SPADE.value, Palo.BASTONI.value])
quattro_denari = Variable('quattro denari', boolean)
cinque_denari = Variable('cinque denari', boolean)
sei_denari = Variable('sei denari', boolean)
sette_denari = Variable('sette denari', boolean)
otto_denari = Variable('otto denari', boolean)
nove_denari = Variable('nove denari', boolean)
dieci_denari = Variable('dieci denari', boolean)
asso_denari = Variable('asso denari', boolean)
due_denari = Variable('due denari', boolean)
tre_denari = Variable('tre denari', boolean)
quattro_coppe = Variable('quattro coppe', boolean)
cinque_coppe = Variable('cinque coppe', boolean)
sei_coppe = Variable('sei coppe', boolean)
sette_coppe = Variable('sette coppe', boolean)
otto_coppe = Variable('otto coppe', boolean)
nove_coppe = Variable('nove coppe', boolean)
dieci_coppe = Variable('dieci coppe', boolean)
asso_coppe = Variable('asso coppe', boolean)
due_coppe = Variable('due coppe', boolean)
tre_coppe = Variable('tre coppe', boolean)
quattro_spade = Variable('quattro spade', boolean)
cinque_spade = Variable('cinque spade', boolean)
sei_spade = Variable('sei spade', boolean)
sette_spade = Variable('sette spade', boolean)
otto_spade = Variable('otto spade', boolean)
nove_spade = Variable('nove spade', boolean)
dieci_spade = Variable('dieci spade', boolean)
asso_spade = Variable('asso spade', boolean)
due_spade = Variable('due spade', boolean)
tre_spade = Variable('tre spade', boolean)
quattro_bastoni = Variable('quattro bastoni', boolean)
cinque_bastoni = Variable('cinque bastoni', boolean)
sei_bastoni = Variable('sei bastoni', boolean)
sette_bastoni = Variable('sette bastoni', boolean)
otto_bastoni = Variable('otto bastoni', boolean)
nove_bastoni = Variable('nove bastoni', boolean)
dieci_bastoni = Variable('dieci bastoni', boolean)
asso_bastoni = Variable('asso bastoni', boolean)
due_bastoni = Variable('due bastoni', boolean)
tre_bastoni = Variable('tre bastoni', boolean)

carta_denari =  Variable('carta denari',[0,1,2,3,4,5,6,7,8,9])
carta_coppe = Variable('carta coppe',[0,1,2,3,4,5,6,7,8,9])
carta_spade = Variable('carta spade',[0,1,2,3,4,5,6,7,8,9])
carta_bastoni = Variable('carta bastoni',[0,1,2,3,4,5,6,7,8,9])

quattro = 0.25
cinque = 0.15
sei = 0.12
sette = 0.1
otto = 0.09
nove = 0.09
dieci = 0.09
asso = 0.02
due = 0.07
tre = 0.02

coeff_palo = 0.85
coeff_notPalo = 0.05
def carta_palo(carta):
    return carta*coeff_palo

def carta_notPalo(carta):
    return carta*coeff_notPalo

def get_prob(var,pars,palo,value):
      if palo == Palo.DENARI or palo == 0: 
            f = Prob(var,pars,[[(1-carta_palo(value)), carta_palo(value)],
                              [(1-carta_notPalo(value)), carta_notPalo(value)],
                              [(1-carta_notPalo(value)), carta_notPalo(value)],
                              [(1-carta_notPalo(value)), carta_notPalo(value)]])
            
      elif palo == Palo.COPPE or palo == 1:
           f = Prob(var,pars,[[(1-carta_notPalo(value)), carta_notPalo(value)],
                              [(1-carta_palo(value)), carta_palo(value)],
                              [(1-carta_notPalo(value)), carta_notPalo(value)],
                              [(1-carta_notPalo(value)), carta_notPalo(value)]])
           
      elif palo == Palo.SPADE or palo == 2:
           f = Prob(var,pars,[[(1-carta_notPalo(value)), carta_notPalo(value)],
                              [(1-carta_notPalo(value)), carta_notPalo(value)],
                              [(1-carta_palo(value)), carta_palo(value)],
                              [(1-carta_notPalo(value)), carta_notPalo(value)]])
           
      elif palo == Palo.BASTONI or palo == 3:
            f = Prob(var,pars,[[(1-carta_notPalo(value)), carta_notPalo(value)],
                              [(1-carta_notPalo(value)), carta_notPalo(value)],
                              [(1-carta_notPalo(value)), carta_notPalo(value)],
                              [(1-carta_palo(value)), carta_palo(value)]])
      
      return f

f_palo = Prob(palo,[],[0.25,0.25,0.25,0.25])
#DENARI
f_4d = get_prob(quattro_denari,[palo],Palo.DENARI,quattro)
f_5d = get_prob(cinque_denari,[palo],Palo.DENARI,cinque)
f_6d = get_prob(sei_denari,[palo],Palo.DENARI,sei)
f_7d = get_prob(sette_denari,[palo],Palo.DENARI,sette)
f_8d = get_prob(otto_denari,[palo],Palo.DENARI,otto)
f_9d = get_prob(nove_denari,[palo],Palo.DENARI,nove)
f_10d = get_prob(dieci_denari,[palo],Palo.DENARI,dieci)
f_1d = get_prob(asso_denari,[palo],Palo.DENARI,asso)
f_2d = get_prob(due_denari,[palo],Palo.DENARI,due)
f_3d = get_prob(tre_denari,[palo],Palo.DENARI,tre)
#COPPE
f_4c = get_prob(quattro_coppe,[palo],Palo.COPPE,quattro)
f_5c = get_prob(cinque_coppe,[palo],Palo.COPPE,cinque)
f_6c = get_prob(sei_coppe,[palo],Palo.COPPE,sei)
f_7c = get_prob(sette_coppe,[palo],Palo.COPPE,sette)
f_8c = get_prob(otto_coppe,[palo],Palo.COPPE,otto)
f_9c = get_prob(nove_coppe,[palo],Palo.COPPE,nove)
f_10c = get_prob(dieci_coppe,[palo],Palo.COPPE,dieci)
f_1c = get_prob(asso_coppe,[palo],Palo.COPPE,asso)
f_2c = get_prob(due_coppe,[palo],Palo.COPPE,due)
f_3c = get_prob(tre_coppe,[palo],Palo.COPPE,tre)
#SPADE
f_4s = get_prob(quattro_spade,[palo],Palo.SPADE,quattro)
f_5s = get_prob(cinque_spade,[palo],Palo.SPADE,cinque)
f_6s = get_prob(sei_spade,[palo],Palo.SPADE,sei)
f_7s = get_prob(sette_spade,[palo],Palo.SPADE,sette)
f_8s = get_prob(otto_spade,[palo],Palo.SPADE,otto)
f_9s = get_prob(nove_spade,[palo],Palo.SPADE,nove)
f_10s = get_prob(dieci_spade,[palo],Palo.SPADE,dieci)
f_1s = get_prob(asso_spade,[palo],Palo.SPADE,asso)
f_2s = get_prob(due_spade,[palo],Palo.SPADE,due)
f_3s = get_prob(tre_spade,[palo],Palo.SPADE,tre)
#BASTONI
f_4b = get_prob(quattro_bastoni,[palo],Palo.BASTONI,quattro)
f_5b = get_prob(cinque_bastoni,[palo],Palo.BASTONI,cinque)
f_6b = get_prob(sei_bastoni,[palo],Palo.BASTONI,sei)
f_7b = get_prob(sette_bastoni,[palo],Palo.BASTONI,sette)
f_8b = get_prob(otto_bastoni,[palo],Palo.BASTONI,otto)
f_9b = get_prob(nove_bastoni,[palo],Palo.BASTONI,nove)
f_10b = get_prob(dieci_bastoni,[palo],Palo.BASTONI,dieci)
f_1b = get_prob(asso_bastoni,[palo],Palo.BASTONI,asso)
f_2b = get_prob(due_bastoni,[palo],Palo.BASTONI,due)
f_3b = get_prob(tre_bastoni,[palo],Palo.BASTONI,tre)

def get_row(array, i, size):
    if size == 1:
        value = []
        for b in reversed(array):
            if b:
                c = np.count_nonzero(array == True)
                value.append(float(1/c))
            else:
                value.append(float(0))

        return value
    
    elif size%2 == 0:
        i = i+1

        array2 = np.copy(array)
        array2[i] = True

        row1 = get_row(array, i, size/2)
        row2 = get_row(array2, i, size/2)

    return [row1,row2]


def get_TabularCPD(var):
    array1 = np.zeros(var.get_size(), dtype=bool)
    array2 = np.zeros(var.get_size(), dtype=bool)
    i = 0
    array2[i] = True

    row1 = get_row(array1, i, (2**var.get_size())/2)
    row2 = get_row(array2, i, (2**var.get_size())/2)

    return [row1,row2]

f_cd = Prob(carta_denari, [tre_denari,due_denari,asso_denari,dieci_denari,nove_denari,otto_denari,sette_denari,sei_denari,cinque_denari,quattro_denari], get_TabularCPD(carta_denari))
f_cc = Prob(carta_coppe, [tre_coppe,due_coppe,asso_coppe,dieci_coppe,nove_coppe,otto_coppe,sette_coppe,sei_coppe,cinque_coppe,quattro_coppe], get_TabularCPD(carta_coppe))
f_cs =  Prob(carta_spade, [tre_spade,due_spade,asso_spade,dieci_spade,nove_spade,otto_spade,sette_spade,sei_spade,cinque_spade,quattro_spade],get_TabularCPD(carta_spade))
f_cb = Prob(carta_bastoni, [tre_bastoni,due_bastoni,asso_bastoni,dieci_bastoni,nove_bastoni,otto_bastoni,sette_bastoni,sei_bastoni,cinque_bastoni,quattro_bastoni],get_TabularCPD(carta_bastoni))

tressette = BeliefNetwork("Probabilita' prossima carta", {palo,
                                                          quattro_denari,cinque_denari,sei_denari,sette_denari,otto_denari,nove_denari,dieci_denari,asso_denari,due_denari,tre_denari,
                                                          quattro_coppe,cinque_coppe,sei_coppe,sette_coppe,otto_coppe,nove_coppe,dieci_coppe,asso_coppe,due_coppe,tre_coppe,
                                                          quattro_spade,cinque_spade,sei_spade,sette_spade,otto_spade,nove_spade,dieci_spade,asso_spade,due_spade,tre_spade,
                                                          quattro_bastoni,cinque_bastoni,sei_bastoni,sette_bastoni,otto_bastoni,nove_bastoni,dieci_bastoni,asso_bastoni,due_bastoni,tre_bastoni,
                                                          carta_denari,carta_coppe,carta_bastoni,carta_spade},
                                                          {f_palo,
                                                           f_4d,f_5d,f_6d,f_7d,f_8d,f_9d,f_10d,f_1d,f_2d,f_3d,
                                                           f_4c,f_5c,f_6c,f_7c,f_8c,f_9c,f_10c,f_1c,f_2c,f_3c,
                                                           f_4s,f_5s,f_6s,f_7s,f_8s,f_9s,f_10s,f_1s,f_2s,f_3s,
                                                           f_4b,f_5b,f_6b,f_7b,f_8b,f_9b,f_10b,f_1b,f_2b,f_3b,
                                                           f_cd, f_cc, f_cs, f_cb})


class TressetteVE(VE):
    def __init__(self, gm=tressette):
        super().__init__(gm)
        self.mazzo = []
        self.uscite = []
        self.dict = {'quattro_denari':quattro_denari, 'cinque_denari': cinque_denari, 'sei_denari': sei_denari, 'sette_denari': sette_denari, 'otto_denari': otto_denari, 'nove_denari':nove_denari, 'dieci_denari':dieci_denari, 'asso_denari':asso_denari, 'due_denari':due_denari, 'tre_denari':tre_denari,
                     'quattro_coppe':quattro_coppe, 'cinque_coppe': cinque_coppe, 'sei_coppe': sei_coppe, 'sette_coppe': sette_coppe, 'otto_coppe': otto_coppe, 'nove_coppe':nove_coppe, 'dieci_coppe':dieci_coppe, 'asso_coppe':asso_coppe, 'due_coppe':due_coppe, 'tre_coppe':tre_coppe,
                     'quattro_spade':quattro_spade, 'cinque_spade': cinque_spade, 'sei_spade': sei_spade, 'sette_spade': sette_spade, 'otto_spade': otto_spade, 'nove_spade':nove_spade, 'dieci_spade':dieci_spade, 'asso_spade':asso_spade, 'due_spade':due_spade, 'tre_spade':tre_spade,
                     'quattro_bastoni':quattro_bastoni, 'cinque_bastoni': cinque_bastoni, 'sei_bastoni': sei_bastoni, 'sette_bastoni': sette_bastoni, 'otto_bastoni': otto_bastoni, 'nove_bastoni':nove_bastoni, 'dieci_bastoni':dieci_bastoni, 'asso_bastoni':asso_bastoni, 'due_bastoni':due_bastoni, 'tre_bastoni':tre_bastoni}


    def append_uscita(self, name):
        carta = CartaNapoletana(name, var = self.dict[name])
        self.uscite.append(carta)

    def set_mazzo(self, lista_nomi):
        self.mazzo = self.StringtoCartaNapoletana(lista_nomi)

    #RESTITUISCE LA CARTA DA TIRARE: POLICY GREEDY, SE POSSIAMO PRENDERE PRENDIAMO, SCARTIAMO ALTRIMENTI
    def query(self, j, nomi_terra, palo):
        if palo == None:    #SIAMO PRIMI
            dp = {'denari': self.query_denari, 'coppe':self.query_coppe, 'spade':self.query_spade, 'bastoni':self.query_bastoni}
            ld = []
            for p, f in dp.items():
                dict = {}
                carte_palo = self.carte_palo(p)

                t, p = self.expected_tira(j, carte_palo, 0, f)
                dict['carta'] = t
                dict['presa'] = p
                ld.append(dict)

            ld_true = []
            for d in ld:
                if d['presa']:
                    ld_true.append(d)
            
            if len(ld_true) == 0:
                d = random.choice(ld)
            else:
                d = random.choice(ld_true)
            
            t = d['carta']            
        else:
            terra = self.StringtoCartaNapoletana(nomi_terra)
            max_pw_terra = self.max_pw_terra(terra, palo)
            carte_palo = self.carte_palo(palo)

            if j < 3:   #NON SIAMO ULTIMI A TIRARE
                if palo == 'denari':
                    t, _ = self.expected_tira(j, carte_palo, max_pw_terra, self.query_denari)
                elif palo == 'coppe':
                    t, _ = self.expected_tira(j, carte_palo, max_pw_terra, self.query_coppe)
                elif palo == 'spade':
                    t, _ = self.expected_tira(j, carte_palo, max_pw_terra, self.query_spade)
                elif palo == 'bastoni':
                    t, _ = self.expected_tira(j, carte_palo, max_pw_terra, self.query_bastoni)
            else:   #SIAMO ULTIMI A TIRARE
                t, _ = self.tira(carte_palo, max_pw_terra)

        self.mazzo.remove(t)
        return t.get_name()

    def max_pw_terra(self, terra, palo):
        max_pw_terra = 0
        for carta in terra:
            if carta.get_palo() == palo:
                if carta.get_potere() > max_pw_terra:
                    max_pw_terra = carta.get_potere()
        return max_pw_terra
    
    #CALCOLA LE PROSSIME CARTE ATTESE E RITORNA LA CARTA DA TIRARE
    def expected_tira(self, j, carte_palo, max_pw_terra, query_palo):
        hyp = []
        expected_power = max_pw_terra

        while j < 3: 
            nome_carta, epw, _ = query_palo(hyp)
            hyp.append(nome_carta)
            if epw > expected_power:
                expected_power = epw
            j = j + 1

        return self.tira(carte_palo, expected_power)

    #CALCOLA LA CARTA DA TIRARE
    def tira(self, carte_palo, expected_power):
        tira = None
        presa = False
        if len(carte_palo) == 0:
            min_punti = 2
            c_mp = None
            for carta in self.mazzo:
                if carta.get_punti() < min_punti:
                    min_punti = carta.get_punti()
                    c_mp = carta
                    
            tira = c_mp

        elif len(carte_palo) == 1:
            carta = carte_palo[0]
            tira = carta
                
        else:   #abbiamo più di una carta
            max_pw = 0
            c_max = None
            for carta in carte_palo:
                if carta.get_potere() > max_pw:
                    max_pw = carta.get_potere()
                    c_max = carta
                   
            if max_pw > expected_power:     #possiamo prendere
                presa = True
                suff_pw = 0
                c_suff = None
                for carta in carte_palo:
                    if carta.get_potere() < max_pw and carta.get_potere() > expected_power:
                        suff_pw = carta.get_potere()
                        c_suff = carta
                if c_suff != None:
                    tira = c_suff
                else:
                    tira = c_max
            else:                       #non possiamo prendere
                min_punti = 2
                c_mp = None
                for carta in carte_palo:
                    if carta.get_punti() < min_punti:
                        min_punti = carta.get_punti()
                        c_mp = carta    
                tira = c_mp
        return tira, presa

    def carte_palo(self, palo):
        carte_palo = []
        for carta in self.mazzo:
            if carta.get_palo() == palo:
                carte_palo.append(carta)
        return carte_palo
                

    def expected_values(self, q, palo):
        k_max = 0
        max = 0
        for k, v in q.items():
            if v>max:
                max = v
                k_max = k

        carta = None
        expected_power = 0
        expected_point = 0.27
        if max != 0:
            carta = CartaNapoletana(k_max+1, palo = palo)
            expected_power = carta.get_potere()
            expected_point = carta.get_punti()

        return carta, expected_power, expected_point


    def query_denari(self, hyp = [], elim_order = None):
        l = self.uscite + self.mazzo
        for h in hyp:
            if h != None:
                l.append(h)    
        var = carta_denari
        obs = {palo:0}

        for carta in l:
            obs[carta.get_var()] = False

        q = super().query(var,obs,elim_order)

        return self.expected_values(q, 'denari') 
    

    def query_coppe(self, hyp = [], elim_order = None):
        l = self.uscite + self.mazzo
        for h in hyp:
            if h != None:
                l.append(h)    
        var = carta_coppe
        obs = {palo:1}

        for carta in l:
            obs[carta.get_var()] = False

        q = super().query(var,obs,elim_order)

        return self.expected_values(q, 'coppe') 

    def query_spade(self, hyp = [], elim_order = None):
        l = self.uscite + self.mazzo
        for h in hyp:
            if h != None:
                l.append(h)    
        var = carta_spade
        obs = {palo:2}

        for carta in l:
            obs[carta.get_var()] = False

        q = super().query(var,obs,elim_order)

        return self.expected_values(q, 'spade')  

    def query_bastoni(self, hyp = [], elim_order = None):
        l = self.uscite + self.mazzo
        for h in hyp:
            if h != None:
                l.append(h)    
        var = carta_bastoni
        obs = {palo:3}

        for carta in l:
            obs[carta.get_var()] = False

        q = super().query(var,obs,elim_order)

        return self.expected_values(q, 'bastoni') 

    def StringtoCartaNapoletana(self, lista_nomi):
        mazzo = []
        for name in lista_nomi:
            carta = CartaNapoletana(name, var = self.dict[name])
            mazzo.append(carta)

        return mazzo
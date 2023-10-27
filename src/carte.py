class Carta(object):
    def __init__(self, name, palo, potere, punti, var=None):
        self.name = name
        self.palo = palo
        self.potere = potere
        self.punti = punti
        self.var = var

    def get_name(self):
        return self.name
    
    def get_palo(self):
        return self.palo
    
    def get_potere(self):
        return self.potere
    
    def get_punti(self):
        return self.punti
    
    def set_var(self, var):
        self.var = var
    
    def get_var(self):
        return self.var


from pyswip import Prolog

class CartaNapoletana(Carta):
   
    def __init__(self, id, palo = None, var = None):
        p = Prolog()
        p.consult('Tressette/src/tressette.pl')

        if type(id) == int:
            potere = id
            for a in p.query('prop(N,potere,'+str(potere)+')'):
                name = a['N']
            for a in p.query('prop('+name+',punti,P)'):
                punti = a['P']

        else:
            name = id
            for a in p.query('prop('+name+',potere,PW)'):
                potere = int(a['PW'])
            for a in p.query('prop('+name+',palo,PA)'):
                palo = a['PA']    
            for a in p.query('prop('+name+',punti,P)'):
                punti = a['P']

        super().__init__(name, palo, potere, punti, var)


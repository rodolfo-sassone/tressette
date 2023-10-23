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
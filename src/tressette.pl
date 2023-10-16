:- use_module(library(lists)).
:- dynamic(prop/3).
:- dynamic(piombo/2).
:- dynamic(palo/2).


giocatore(me).
giocatore(compagno).
giocatore(avv1).
giocatore(avv2).

prop(asso_denari,type,asso).
prop(asso_denari,palo,denari).
prop(asso_denari,potere,8).
prop(asso_denari,punti,1).

prop(due_denari,type,due).
prop(due_denari,palo,denari).
prop(due_denari,potere,9).
prop(due_denari,punti,0.334).

prop(tre_denari,type,tre).
prop(tre_denari,palo,denari).
prop(tre_denari,potere,10).
prop(tre_denari,punti,0.334).

prop(dieci_denari,type,figura).
prop(dieci_denari,palo,denari).
prop(dieci_denari,potere,7).
prop(dieci_denari,punti,0.334).

prop(nove_denari,type,figura).
prop(nove_denari,palo,denari).
prop(nove_denari,potere,6).
prop(nove_denari,punti,0.334).

prop(otto_denari,type,figura).
prop(otto_denari,palo,denari).
prop(otto_denari,potere,5).
prop(otto_denari,punti,0.334).

prop(sette_denari,type,scartina).
prop(sette_denari,palo,denari).
prop(sette_denari,potere,4).
prop(sette_denari,punti,0).

prop(sei_denari,type,scartina).
prop(sei_denari,palo,denari).
prop(sei_denari,potere,3).
prop(sei_denari,punti,0).

prop(cinque_denari,type,scartina).
prop(cinque_denari,palo,denari).
prop(cinque_denari,potere,2).
prop(cinque_denari,punti,0).

prop(quattro_denari,type,scartina).
prop(quattro_denari,palo,denari).
prop(quattro_denari,potere,1).
prop(quattro_denari,punti,0).

prop(asso_coppe,type,asso).
prop(asso_coppe,palo,coppe).
prop(asso_coppe,potere,8).
prop(asso_coppe,punti,1).

prop(due_coppe,type,due).
prop(due_coppe,palo,coppe).
prop(due_coppe,potere,9).
prop(due_coppe,punti,0.334).

prop(tre_coppe,type,tre).
prop(tre_coppe,palo,coppe).
prop(tre_coppe,potere,10).
prop(tre_coppe,punti,0.334).

prop(dieci_coppe,type,figura).
prop(dieci_coppe,palo,coppe).
prop(dieci_coppe,potere,7).
prop(dieci_coppe,punti,0.334).

prop(nove_coppe,type,figura).
prop(nove_coppe,palo,coppe).
prop(nove_coppe,potere,6).
prop(nove_coppe,punti,0.334).

prop(otto_coppe,type,figura).
prop(otto_coppe,palo,coppe).
prop(otto_coppe,potere,5).
prop(otto_coppe,punti,0.334).

prop(sette_coppe,type,scartina).
prop(sette_coppe,palo,coppe).
prop(sette_coppe,potere,4).
prop(sette_coppe,punti,0).

prop(sei_coppe,type,scartina).
prop(sei_coppe,palo,coppe).
prop(sei_coppe,potere,3).
prop(sei_coppe,punti,0).

prop(cinque_coppe,type,scartina).
prop(cinque_coppe,palo,coppe).
prop(cinque_coppe,potere,2).
prop(cinque_coppe,punti,0).

prop(quattro_coppe,type,scartina).
prop(quattro_coppe,palo,coppe).
prop(quattro_coppe,potere,1).
prop(quattro_coppe,punti,0).

prop(asso_spade,type,asso).
prop(asso_spade,palo,spade).
prop(asso_spade,potere,8).
prop(asso_spade,punti,1).

prop(due_spade,type,due).
prop(due_spade,palo,spade).
prop(due_spade,potere,9).
prop(due_spade,punti,0.334).

prop(tre_spade,type,tre).
prop(tre_spade,palo,spade).
prop(tre_spade,potere,10).
prop(tre_spade,punti,0.334).

prop(dieci_spade,type,figura).
prop(dieci_spade,palo,spade).
prop(dieci_spade,potere,7).
prop(dieci_spade,punti,0.334).

prop(nove_spade,type,figura).
prop(nove_spade,palo,spade).
prop(nove_spade,potere,6).
prop(nove_spade,punti,0.334).

prop(otto_spade,type,figura).
prop(otto_spade,palo,spade).
prop(otto_spade,potere,5).
prop(otto_spade,punti,0.334).

prop(sette_spade,type,scartina).
prop(sette_spade,palo,spade).
prop(sette_spade,potere,4).
prop(sette_spade,punti,0).

prop(sei_spade,type,scartina).
prop(sei_spade,palo,spade).
prop(sei_spade,potere,3).
prop(sei_spade,punti,0).

prop(cinque_spade,type,scartina).
prop(cinque_spade,palo,spade).
prop(cinque_spade,potere,2).
prop(cinque_spade,punti,0).

prop(quattro_spade,type,scartina).
prop(quattro_spade,palo,spade).
prop(quattro_spade,potere,1).
prop(quattro_spade,punti,0).

prop(asso_bastoni,type,asso).
prop(asso_bastoni,palo,bastoni).
prop(asso_bastoni,potere,8).
prop(asso_bastoni,punti,1).

prop(due_bastoni,type,due).
prop(due_bastoni,palo,bastoni).
prop(due_bastoni,potere,9).
prop(due_bastoni,punti,0.334).

prop(tre_bastoni,type,tre).
prop(tre_bastoni,palo,bastoni).
prop(tre_bastoni,potere,10).
prop(tre_bastoni,punti,0.334).

prop(dieci_bastoni,type,figura).
prop(dieci_bastoni,palo,bastoni).
prop(dieci_bastoni,potere,7).
prop(dieci_bastoni,punti,0.334).

prop(nove_bastoni,type,figura).
prop(nove_bastoni,palo,bastoni).
prop(nove_bastoni,potere,6).
prop(nove_bastoni,punti,0.334).

prop(otto_bastoni,type,figura).
prop(otto_bastoni,palo,bastoni).
prop(otto_bastoni,potere,5).
prop(otto_bastoni,punti,0.334).

prop(sette_bastoni,type,scartina).
prop(sette_bastoni,palo,bastoni).
prop(sette_bastoni,potere,4).
prop(sette_bastoni,punti,0).

prop(sei_bastoni,type,scartina).
prop(sei_bastoni,palo,bastoni).
prop(sei_bastoni,potere,3).
prop(sei_bastoni,punti,0).

prop(cinque_bastoni,type,scartina).
prop(cinque_bastoni,palo,bastoni).
prop(cinque_bastoni,potere,2).
prop(cinque_bastoni,punti,0).

prop(quattro_bastoni,type,scartina).
prop(quattro_bastoni,palo,bastoni).
prop(quattro_bastoni,potere,1).
prop(quattro_bastoni,punti,0).
/*
%			******PROVE*******
%mazzo di prova
prop(nove_coppe,possessore,giocatore(me)).
prop(sette_coppe,possessore,giocatore(me)).
prop(tre_denari,possessore,giocatore(me)).
prop(nove_denari,possessore,giocatore(me)).
prop(tre_bastoni,possessore,giocatore(me)).
prop(otto_bastoni,possessore,giocatore(me)).
prop(quattro_bastoni,possessore,giocatore(me)).
prop(sette_bastoni,possessore,giocatore(me)).
prop(sette_spade,possessore,giocatore(me)).
prop(tre_spade,possessore,giocatore(me)).


%TURNO 0
prop(due_bastoni,terra,0).
prop(due_bastoni,possessore,giocatore(compagno)).

prop(nove_bastoni,terra,0).
prop(nove_bastoni,possessore,giocatore(avv1)).

prop(otto_bastoni,terra,0).

prop(sei_bastoni,terra,0).
prop(sei_bastoni,possessore,giocatore(avv2)).

prop(due_bastoni,uscita,si).
prop(nove_bastoni,uscita,si).
prop(otto_bastoni,uscita,si).
prop(sei_bastoni,uscita,si).


%TURNO 1
prop(cinque_bastoni,terra,1).
prop(cinque_bastoni,possessore,giocatore(compagno)).

prop(dieci_bastoni,terra,1).
prop(dieci_bastoni,possessore,giocatore(avv1)).


%TURNO 2
prop(otto_bastoni,terra,2).
prop(otto_bastoni,possessore,giocatore(avv2)).

prop(asso_bastoni,terra,2).

prop(due_bastoni,terra,2).
prop(due_bastoni,possessore,giocatore(avv1)).

prop(dieci_bastoni,terra,2).
prop(dieci_bastoni,possessore,giocatore(compagno)).

prop(otto_bastoni,uscita,si).
prop(asso_bastoni,uscita,si).
prop(due_bastoni,uscita,si).
prop(dieci_bastoni,uscita,si).


%TURNO 3
prop(quattro_spade,terra,3).
prop(quattro_spade,possessore,giocatore(avv1)).

prop(sei_spade,terra,3).
prop(sei_spade,possessore,giocatore(compagno)).

prop(sette_spade,terra,3).
prop(sette_spade,possessore,giocatore(avv2)).

prop(asso_spade,terra,3).

prop(quattro_spade,uscita,si).
prop(sei_spade,uscita,si).
prop(sette_spade,uscita,si).
prop(asso_spade,uscita,si).


%TURNO 4
prop(asso_denari,terra,4).

prop(otto_denari,terra,4).
prop(otto_denari,possessore,giocatore(avv1)).

prop(sette_denari,terra,4).
prop(sette_denari,possessore,giocatore(compagno)).

prop(nove_denari,terra,4).
prop(nove_denari,possessore,giocatore(avv2)).

prop(asso_denari,uscita,si).
prop(otto_denari,uscita,si).
prop(sette_denari,uscita,si).
prop(nove_denari,uscita,si).


%TURNO 5
prop(due_denari,terra,5).

prop(dieci_denari,terra,5).
prop(dieci_denari,possessore,giocatore(avv1)).

prop(otto_spade,terra,5).
prop(otto_spade,possessore,giocatore(compagno)).

prop(sette_coppe,terra,5).
prop(sette_coppe,possessore,giocatore(avv2)).

prop(due_denari,uscita,si).
prop(dieci_denari,uscita,si).
prop(otto_spade,uscita,si).
prop(sette_coppe,uscita,si).


%TURNO 6
prop(dieci_spade,terra,6).

prop(cinque_spade,terra,6).
prop(cinque_spade,possessore,giocatore(avv1)).

prop(nove_spade,terra,6).
prop(nove_spade,possessore,giocatore(compagno)).

prop(tre_spade,terra,6).
prop(tre_spade,possessore,giocatore(avv2)).

prop(dieci_spade,uscita,si).
prop(cinque_spade,uscita,si).
prop(nove_spade,uscita,si).
prop(tre_spade,uscita,si).


%TURNO 7
prop(sette_bastoni,terra,7).
prop(sette_bastoni,possessore,giocatore(avv2)).

prop(asso_coppe,terra,7).

prop(dieci_coppe,terra,7).
prop(dieci_coppe,possessore,giocatore(avv1)).

prop(cinque_coppe,terra,7).
prop(cinque_coppe,possessore,giocatore(compagno)).

prop(sette_bastoni,uscita,si).
prop(asso_coppe,uscita,si).
prop(dieci_coppe,uscita,si).
prop(cinque_coppe,uscita,si).


%TURNO 8
prop(quattro_bastoni,terra,8).
prop(quattro_bastoni,possessore,giocatore(avv2)).

prop(due_spade,terra,8).

prop(quattro_coppe,terra,8).
prop(quattro_coppe,possessore,giocatore(avv1)).

prop(sei_coppe,terra,8).
prop(sei_coppe,possessore,giocatore(compagno)).

prop(quattro_bastoni,uscita,si).
prop(due_spade,uscita,si).
prop(quattro_coppe,uscita,si).
prop(sei_coppe,uscita,si).

%TURNO 9
prop(nove_coppe,terra,9).
prop(nove_coppe,possessore,giocatore(avv2)).


%*******************************************************
*/

%per dedurre per esclusione il possesso di una carta dobbiamo anche sapere chi NON ha una carta
%è possibile dare queste regole poiché sappiamo tutte le nostre carte dall'inizio
prop(X,non_possessore,giocatore(me)) :- \+ prop(X,possessore,giocatore(me)).

%dopo tutte le carte che non possiede va in stak limit. Ritorna errore su python. Bisognerebbe rimuovere le successive tre clausole per farla funzionare correttamente.
%prop(X,non_possessore, giocatore(G)) :- prop(X,possessore,giocatore(Y)), G\==Y. 

%per quanto riguarda il non possesso degli altri giocatori sarà possibile stabilirlo durante la partita

%stabilire il possesso di una carta per esclusione, sapendo che gli altri non ce l'hanno
prop(X,possessore,giocatore(compagno)) :- prop(X,non_possessore, giocatore(me)), 
   							prop(X,non_possessore, giocatore(avv1)), 
    						prop(X,non_possessore, giocatore(avv2)).

/* per come è impostato il ragionamento ci è indifferente quale avversario abbia una determinata carta. La presenza di queste 2 ci dà solo problemi in piombo/2
prop(X,possessore,giocatore(avv1)) :- prop(X,non_possessore, giocatore(me)), 
   							prop(X,non_possessore, giocatore(compagno)), 
    						prop(X,non_possessore, giocatore(avv2)).

prop(X,possessore,giocatore(avv2)) :- prop(X,non_possessore, giocatore(me)), 
   							prop(X,non_possessore, giocatore(avv1)), 
    						prop(X,non_possessore, giocatore(compagno)).
*/



%se un giocatore è piombo allora non ha nessuna carta a quel palo							
prop(X,non_possessore,giocatore(G)) :- piombo(P,G), prop(X,palo,P), rimanenti_a(P,L,_), member(X,L).

pezzo(C) :- prop(C,type,asso).
pezzo(C) :- prop(C,type,due).
pezzo(C) :- prop(C,type,tre).

search_napoli(G,P) :- pezzo(C), prop(C,palo,Q), prop(C,possessore,giocatore(F)), F \== G, Q \== P,
    		pezzo(D), prop(D, palo, R), prop(D,possessore,giocatore(H)), H \== G, R \== Q, R \== P,
    		pezzo(E), prop(E,palo, S), prop(E,possessore,giocatore(I)), I \== G, S \== R, S \== Q, S \== P, !.

/*
%***PROVA***
palo(0,bastoni).
palo(1,bastoni).
%***********
*/

piombo(P,G) :- palo(T,P), terra(T,LT,_), member(X,LT), prop(X,palo,Q), Q \== P, prop(X,possessore,giocatore(G)).

%conta i giocatori piombo al palo P. Assumiamo che la clausola piombo(P,giocatore(me)) non sia utilizzata
conta_piombo(P,N) :- findall(G,piombo(P,G),L), list_to_set(L,S), conta(S,N).

%true se Y è più grande di X (dello stesso palo)
greater(X,Y) :- prop(X,palo,P), prop(Y,palo,P), prop(X,potere,A), prop(Y,potere,B), B>A, !.

%dato un palo ci restituisce true se Y prende su X
greater(P,X,Y) :-  prop(X,palo,P), prop(Y,palo,P), prop(X,potere,A), prop(Y,potere,B), B>A, !.
greater(P,X,Y) :- prop(X,palo,Q), prop(Y,palo,P), Q\==P.

%true se Y è la più piccola carta più grande di X
min_greater(X,Y) :- prop(X,palo,P), prop(Y,palo,P), prop(X,potere,A), prop(Y,potere,B), Z is B-A, Z==1.

tre(X) :- prop(X,potere,10), !.
tre(X) :- min_greater(X,Y), prop(Y,uscita,si), tre(Y), !.
tre(X) :- min_greater(X,Y), prop(Y,possessore,giocatore(me)), tre(Y).	%utile per riconoscere un possibile "gioco" con le carte che l'agente ha in mano

futura_tre(_,X) :- tre(X), !.
futura_tre(T,X) :- min_greater(X,Y), prop(Y,terra,T), tre(Y).

tutte_fut_tre(T,LN,N) :- mazzo(me,M), accTFT(T,M,[],LF), terra(T,LT,_), sottrai(LF,LT,L), uscite(LU), sottrai(L,LU,LN), conta(LN,N).

accTFT(_,[],A,A).
accTFT(T,[X|R],A,L) :- futura_tre(T,X), accTFT(T,R,[X|A],L), !.
accTFT(T,[_|R],A,L) :- accTFT(T,R,A,L).

%L lista delle carte tre disponibili all'agente, N numero di carte tre disponibili all'agente
tre_disp(L,N) :- disponibili(M,_), accTD(M,[],L), conta(L,N).

accTD([],A,A).
accTD([X|T],A,L) :- tre(X), accTD(T,[X|A],L), !.
accTD([_|T],A,L) :- accTD(T,A,L).

napoli(P,G) :-  prop(X,possessore,giocatore(G)), prop(X,type,asso), prop(X,palo,P),
    		prop(Y,possessore,giocatore(G)), prop(Y,type,due), prop(Y,palo,P),
    		prop(Z,possessore,giocatore(G)), prop(Z,type,tre), prop(Z,palo,P).

corona(T,G) :- 
   			prop(X,possessore,giocatore(G)), prop(X,type,T), T\==scartina, T\==figura,
     		prop(Y,possessore,giocatore(G)), prop(Y,type,T), X \== Y,
    		prop(Z,possessore,giocatore(G)), prop(Z,type,T), X \== Z, Y \==Z,
    		prop(W,possessore,giocatore(G)), prop(W,type,T), X \== W, Y \== W, Z \== W, !.

corona_asso(G) :- corona(asso,G).
corona_due(G) :- corona(due,G).
corona_tre(G) :- corona(tre,G).

bongioco(T,G) :- prop(X,possessore,giocatore(G)), prop(X,type,T), T\==scartina, T\==figura,
     		prop(Y,possessore,giocatore(G)), prop(Y,type,T), X \== Y,
    		prop(Z,possessore,giocatore(G)), prop(Z,type,T), X \== Z, Y \==Z, \+ corona(T,G),!.

bongioco_asso(G) :- bongioco(asso,G).
bongioco_due(G) :- bongioco(due,G).
bongioco_tre(G) :- bongioco(tre,G).

% M mazzo (conosciuto) del giocatore G.
mazzo(G,M) :- findall(X,prop(X,possessore,giocatore(G)),M).
    
a_monte(si) :- mazzo(me,M), sumallpoint(M,S), S<1.3.
a_monte(no).


%L tutte le carte non uscite del palo P, N numero delle carte non uscite del palo P. Se non si speciofica P si hanno 4 risultati, 1 per palo.
rimanenti_a(P,L,N) :- carte_a(P,L1), rimuovi_uscite(L1,L), conta(L,N).

carte_a(P,L) :- bagof(X,(prop(X,palo,P)), L).

rimuovi_uscite(L1,L):- accRU(L1,[],L).
accRU([],A,A).
accRU([H|T],A,L) :- prop(H,uscita,si), accRU(T,A,L), !.
accRU([H|T],A,L) :- accRU(T,[H|A],L).

%carte disponibli all'agente
disponibili(L,N) :- mazzo(me,M), rimuovi_uscite(M,L), conta(L,N).
disponibili(P,L,N) :- disponibili(M,_), per_palo(P,M,L), conta(L,N).

%carte disponibili al compagno
disp_comp(L,N) :- mazzo(compagno,M), rimuovi_uscite(M,L), conta(L,N).
disp_comp(P,L,N) :- disp_comp(M,_), per_palo(P,M,L), conta(L,N).

%dato il palo P e una lista di carte M, restituisce la lista L di tutte le carte al palo P in M
per_palo(P,M,L) :- accPP(P,M,[],L).
accPP(_,[],A,A).
accPP(P,[H|T],A,L) :- prop(H,palo,P), accPP(P,T,[H|A],L), !.
accPP(P,[_|T],A,L) :- accPP(P,T,A,L).

%G giocatore che prende, P palo della mano, N numero mano
/*presa(G,P,N) :- prop(A,potere,W), prop(A,possessore,giocatore(G)), prop(A,terra,N), prop(A,palo,P),
    		prop(B,potere,X), prop(B,possessore,giocatore(_)), prop(B,terra,N), prop(B,palo,_),
    		prop(C,potere,Y), prop(C,possessore,giocatore(_)), prop(C,terra,N), prop(C,palo,_),
    		prop(D,potere,Z), prop(D,possessore,giocatore(_)), prop(D,terra,N), prop(D,palo,_),
    		W>X, W>Y, W>Z, !.

presa(G,P,N) :- prop(A,potere,W), prop(A,possessore,giocatore(G)), prop(A,terra,N), prop(A,palo,P),
    		prop(B,potere,X), prop(B,possessore,giocatore(_)), prop(B,terra,N), prop(B,palo,_),
    		prop(C,potere,Y), prop(C,possessore,giocatore(_)), prop(C,terra,N), prop(C,palo,_),
    		W>X, W>Y, !.*/

%in questo modo possiamo controllare chi prende anche se non ci sono quattro carte a terra
presa(T,G,P) :- findall(C,prop(C,terra,T),LT), prop(D,terra,T), accPresa(LT,P,D,K), prop(K,possessore,giocatore(G)), !.

accPresa([],_,A,A).
accPresa([X|T],P,A,C) :- greater(P,A,X), accPresa(T,P,X,C).
accPresa([_|T],P,A,C) :- accPresa(T,P,A,C).


disp_superiori(C,L,N) :- prop(C,palo,P), disponibili(P,LP,_), all_greater(C,LP,L), conta(L,N), !.

rimanenti_superiori(C,LS,N) :- prop(C,palo,P), rimanenti_a(P,L,_), all_greater(C,L,LS), conta(LS,N).

%data una carta C e una lista LP di carte dello stesso palo di C, restituisce una lista L delle carte maggiori di C in LP
all_greater(C,LP,L) :- accAG(C,LP,[],L).
accAG(_,[],A,A).
accAG(C,[H|T],A,L) :- prop(H,potere,PH), prop(C,potere,PC), PH>PC, accAG(C,T,[H|A],L).
accAG(C,[_|T],A,L) :- accAG(C,T,A,L).

%data una carta C, un palo P e una lista LP di carte, restituisce una lista L delle carte maggiori di C in LP
all_greater(C,P,LP,L) :- accAG(C,P,LP,[],L), !.
accAG(_,_,[],A,A).
accAG(C,P,[H|T],A,L) :- prop(H,potere,PH), prop(C,potere,PC), prop(C,palo,P), prop(H,palo,P), PH>PC, accAG(C,T,[H|A],L).
accAG(C,P,[_|T],A,L) :- accAG(C,P,T,A,L).

seleziona(9,C) :- disponibili(M,_), member(C,M), !.
seleziona(T,C) :- disponibili(M,_), accSeleziona(T,-100,M,_,C).

accSeleziona(_,_,[],A,A).
accSeleziona(T,U,[X|R],_,C) :- tira(T,X,Unew), Unew > U, accSeleziona(T,Unew,R,X,C), !.
accSeleziona(T,U,[_|R],A,C) :- accSeleziona(T,U,R,A,C).

%l'agente è di mano (tira per primo)
tira(T,C,U) :- \+palo(T,_), prop(C,palo,P), prob_presa(C,P,T,ProbPA), prob_presaComp(T,P,ProbPC), max(ProbPA,ProbPC,ProbP), punti_terra(T,PT), stima_punti(C,T,P,S), R is ProbP*(PT+S), delta_tre(C,T,D), punti_rimanenti(T,C,PR), prob_presa_rimanenti(T,ProbPR), prob_presa_rimanenti_di(C,T,ProbPRC), V is (ProbPR-ProbPRC)*PR, U is R+D+V.
%l'agente non è di mano, può rispondere al palo P
tira(T,C,U) :- palo(T,P), disponibili(P,_,N), N>0, prop(C,possessore,giocatore(me)), prop(C,palo,P), prob_presa(C,P,T,ProbPA), prob_presaComp(T,P,ProbPC), max(ProbPA,ProbPC,ProbP), punti_terra(T,PT), stima_punti(C,T,P,S), R is ProbP*(PT+S), delta_tre(C,T,D), punti_rimanenti(T,C,PR), prob_presa_rimanenti(T,ProbPR), prob_presa_rimanenti_di(C,T,ProbPRC), V is (ProbPR-ProbPRC)*PR, U is R+D+V.
%l'agente non è di mano, non può rispondere al palo P (scarto)
tira(T,C,U) :- palo(T,P), disponibili(P,_,N), N==0, prop(C,possessore,giocatore(me)), \+prop(C,uscita,si), prob_presa(C,P,T,ProbPA), prob_presaComp(T,P,ProbPC), max(ProbPA,ProbPC,ProbP), punti_terra(T,PT), stima_punti(C,T,P,S), R is ProbP*(PT+S), delta_tre(C,T,D), punti_rimanenti(T,C,PR), prob_presa_rimanenti(T,ProbPR), prob_presa_rimanenti_di(C,T,ProbPRC), V is (ProbPR-ProbPRC)*PR, U is R+D+V.


punti_rimanenti(T,C,P) :- prop(C,punti,PC), findall(D,prop(D,uscita,si),LU), sumallpoint(LU,SU), punti_terra(T,ST), P is 11-(SU+ST+PC).

punti_terra(T,Punti) :- terra(T,LT,_), sumallpoint(LT,Punti), !.

%agente primo
stima_punti(C,T,P,S) :- terra(T,_,NT), NT==0, prop(C,punti,PC), rimanenti_a(P,LR,_), disponibili(P,LD,_), sottrai(LR,LD,L), member(X,L), max_punti(LR,X,M), prop(M,punti,PM), PM==1 ,greater(M,C), presa_cade(M,Prob), Prob >= 0.72, S is PC+(PM*Prob)+0.2, !.
stima_punti(C,T,P,S) :- terra(T,_,NT), NT==0, prop(C,punti,PC), rimanenti_a(P,LR,_), disponibili(P,LD,_), sottrai(LR,LD,L), member(X,L), max_punti(LR,X,M), prop(M,punti,PM), PM==1,cade(T,P,Prob), Prob >= 0.72, S is PC+(PM*Prob)+0.2.
stima_punti(C,T,_,S) :- terra(T,_,NT), NT==0, prop(C,punti,PC), S is PC+(0.2*3).
%agente secondo
stima_punti(C,T,P,S) :- terra(T,_,NT), NT==1, prop(C,punti,PC), rimanenti_a(P,LR,_), disponibili(P,LD,_), sottrai(LR,LD,L), member(X,L), max_punti(LR,X,M), prop(M,punti,PM), cade(T,P,Prob), Prob >= 0.70, S is PC+(PM*Prob)+0.2.
stima_punti(C,T,_,S) :- terra(T,_,NT), NT==1, prop(C,punti,PC), S is PC+(0.2*2).
%agente terzo
stima_punti(C,T,P,S) :- terra(T,_,NT), NT==2, prop(C,punti,PC), rimanenti_a(P,LR,_), disponibili(P,LD,_), sottrai(LR,LD,L), member(X,L), max_punti(LR,X,M), prop(M,punti,PM), cade(T,P,Prob), Prob >= 0.65, S is PC+(PM*Prob), !. %probabilità calcolata su tutti i non piombo ma in realtà manca solo un giocatore
stima_punti(C,T,_,S) :- terra(T,_,NT), NT==2, prop(C,punti,PC), S is PC+0.2.
%agente quarto
stima_punti(C,T,_,S) :- terra(T,_,NT), NT==3, prop(C,punti,S).

%data una lista di carte restituisce la carta con più punti
max_punti([],A,A).
max_punti([X|T],A,M) :- prop(X,punti,PX), prop(A,punti,PA), PX>PA, max_punti(T,X,M), !.
max_punti([_|T],A,M) :- max_punti(T,A,M).

%data una lista di carte restituisce la carta con più potere di presa
max_potere([],A,A).
max_potere([X|T],A,M) :- prop(X,potere,PX), prop(A,potere,PA), PX>PA, max_potere(T,X,M), !.
max_potere([_|T],A,M) :- max_potere(T,A,M).

%differenza di carte tre in mano, prima e dopo il turno T. Per non condizionare troppo negativamente giocare una carta tre moltiplichiamo per il coefficiente
%C è carta tre e l'asso al palo P è uscito
delta_tre(C,T,D) :- tutte_fut_tre(T,_,NF), tre_disp(LD,ND), member(C,LD), NFnew is NF-1,prop(C,palo,P), prop(A,palo,P), prop(A,type,asso), uscite(LU), member(A,LU), D is (NFnew-ND)*0.2, !.
%C è carta tre e l'asso al palo P non è uscito
delta_tre(C,T,D) :- tutte_fut_tre(T,_,NF), tre_disp(LD,ND), member(C,LD), NFnew is NF-1, D is (NFnew-ND)*0.65, !.
%C non è carta tre
delta_tre(_,T,D) :- tutte_fut_tre(T,_,NF), tre_disp(_,ND), D is (NF-ND)*0.8.

%		****POBABILITà DI RAGGIUNGERE UN DETERMINATO ESITO****
%probabilità che tirando la carta C prendiamo. P palo del turno attuale, T turno
prob_presa(C,P,_,1) :- prop(C,palo,P), tre(C), !.
prob_presa(C,P,T,1) :-  prop(C,palo,P), findall(K, prop(K,terra,T), LT), all_greater(C,P,LT,L), conta(LT,NT), NT == 3, conta(L,N), N == 0, !.	%Tutte le carte a terra sono minori di C
prob_presa(C,P,T,0) :-  prop(C,palo,P), findall(K, prop(K,terra,T), LT), all_greater(C,P,LT,L), conta(L,N), N>0, !.	%C'è già a terra una carta più alta di C
prob_presa(C,P,_,0) :- prop(C,palo,Q), Q \== P, !.
prob_presa(C,P,T,Prob) :- prop(C,palo,P), rimanenti_a(P,_,NR), terra(T,LT,_), per_palo(P,LT,LTP), conta(LTP,NTP), rimanenti_superiori(C,_,NRS), disponibili(P,_,ND),
    							NRIG is NR-NRS-ND-NTP, Prob is NRIG/(NR-ND-NTP), !.

prob_presaComp(T,P,Prob) :- carta_compagno(T,C), prob_presa(C,P,T,Prob), !.
prob_presaComp(_,P,0) :- disp_comp(P,_,N), N == 0, !.
prob_presaComp(T,P,Prob) :- disp_comp(P,L,_), member(X,L), max_potere(L,X,C), prob_presa(C,P,T,Prob).

%media delle probabilità di prendere ai diversi pali
prob_presa_rimanenti(T,Prob) :- prob_presa_rimanenti_a(denari,T,ProbD), prob_presa_rimanenti_a(coppe,T,ProbC), prob_presa_rimanenti_a(spade,T,ProbS), prob_presa_rimanenti_a(bastoni,T,ProbB) ,Prob is (ProbD+ProbC+ProbS+ProbB)/4.

%probabilità di prendere le carte rimaste al palo P (abbiamo future tre al palo P)
prob_presa_rimanenti_a(P,T,Prob) :- rimanenti_a(P,_,NRP), disponibili(P,_,NDP), n_rimanenti(T,NR), tutte_fut_tre(T,LFT,_), per_palo(P,LFT,LFTP), conta(LFTP,NFTP), NFTP>0, Prob is (NRP-NDP)/NR, !.
%probabilità di prendere le carte rimaste al palo P (non abbiamo future tre al palo P)
prob_presa_rimanenti_a(P,T,0) :- tutte_fut_tre(T,LFT,_), per_palo(P,LFT,LFTP), conta(LFTP,NFTP), NFTP == 0, !.

%probabilità di prendere con la carta C (C è futura tre)
prob_presa_rimanenti_di(C,T,Prob) :- prop(C,palo,P), rimanenti_a(P,_,NRP), disponibili(P,_,NDP), n_rimanenti(T,NR), futura_tre(T,C), Prob is ((NRP-NDP)/NR)/4, !. %dividiamo per quattro per uniformare il risultato a prob_presa_rimanenti/3
%probabilità di prendere con la carta C (C non è futura tre)
prob_presa_rimanenti_di(_,_,0).

%probabilità che una carta cada e venga presa
presa_cade(C,Prob) :- prop(C,palo,P), disp_superiori(C,_,NS), rimanenti_a(P,_,NR), disponibili(P,_,ND),
    					N is NR-ND, conta_piombo(P,GP), GP<3, GNP is 3-GP, prob_cade_presa(N,GNP,NS,P,Prob).

%probabilità che una carta di valore cada (Asso o tre specialmente).
/*cade(P,Prob) :- rimanenti_a(P,_,NR), disponibili(P,_,ND),
    					N is NR-ND, conta_piombo(P,GP), GP<3, GNP is 3-GP, prob_cade(N,GNP,P,Prob).*/

cade(T,P,Prob) :- rimanenti_a(P,_,NR), disponibili(P,_,ND), findall(C,prop(C,terra,T),LT), per_palo(P,LT,L), conta(L,NT),
    					N is NR-ND-NT, conta_piombo(P,GP), GP<3, GNP is 3-GP, N >= GNP, prob_cade(N,GNP,P,Prob).
cade(_,_,0.65).
%************************************************************************************

prob_cade(N,GNP,Palo,Prob) :- tutte_partizioni(N,GNP,P,NP), tutti_casi_favorevoli_cade(P,Palo,NC), Prob is (NC/GNP)/NP.

tutti_casi_favorevoli_cade(P,Palo,N) :- accTCFC(P,Palo,0,N).

accTCFC([],_,A,A).
accTCFC([X|T],Palo,A,NC) :- casi_favorevoli_cade(X,Palo,N), Anew is A+N, accTCFC(T,Palo,Anew,NC).

casi_favorevoli_cade(P,Palo,N) :- piombo(Palo,compagno), accCFC(P,0,N).
casi_favorevoli_cade(P,_,N) :- accCFC1(P,0,0,N).

accCFC([],A,A).
accCFC([X|T],A,N) :- X=1, Anew is A+1, accCFC(T,Anew,N), !.
accCFC([_|T],A,N) :- accCFC(T,A,N).

%caso in cui il nostro compagno non è piombo e che, se può, ci da quel che cerchiamo
accCFC1([],_,A,A).
accCFC1([_|T],I,A,N) :- I=0, Inew is I+1, Anew is A+1, accCFC1(T,Inew,Anew,N), !. %diciamo che il primo elemento del vettore è il numero di carte che ha il compagno.
accCFC1([X|T],I,A,N) :- X=1, Anew is A+1, accCFC1(T,I,Anew,N).
accCFC1([_|T],I,A,N) :- accCFC1(T,I,A,N).
    
%N numero carte rimaste non a disposizione dell'agente, GNP numero giocatori non piombo, NS numero carte superiori a disposizone dell'agente, P palo
prob_cade_presa(N,GNP,NS,Palo,Prob) :- tutte_partizioni(N,GNP,P,NP), tutti_casi_favorevoli_presa(NS,P,Palo,NC), Prob is (NC/GNP)/NP, !.

tutti_casi_favorevoli_presa(NS,P,Palo,N) :- accTCFP(NS,P,Palo,0,N).

accTCFP(_,[],_,A,A).
accTCFP(NS,[X|T],Palo,A,NC) :- casi_favorevoli_presa(NS,X,Palo,N), Anew is A+N, accTCFP(NS,T,Palo,Anew,NC).

casi_favorevoli_presa(NS,P,Palo,N) :- piombo(Palo,compagno), accCFP(NS,P,0,N).
casi_favorevoli_presa(NS,P,_,N) :- accCFP1(NS,P,0,0,N).

accCFP(_,[],A,A).
accCFP(NS,[X|T],A,N) :- NS >= X, Anew is A+1, accCFP(NS,T,Anew,N), !.
accCFP(NS,[_|T],A,N) :- accCFP(NS,T,A,N).

%caso in cui il nostro compagno non è piombo e che, se può, ci da quel che cerchiamo
accCFP1(_,[],_,A,A).
accCFP1(NS,[_|T],I,A,N) :- I==0, Anew is A+1, Inew is I+1, accCFP1(NS,T,Inew,Anew,N), !. %diciamo che il primo elemento del vettore è il numero di carte che ha il compagno.
accCFP1(NS,[X|T],I,A,N) :- NS >= X, Anew is A+1, accCFP1(NS,T,I,Anew,N).
accCFP1(NS,[_|T],I,A,N) :- accCFP1(NS,T,I,A,N).


%				***UTILITIES***
%Data una lista L di carte restituisce la somma S dei punti delle carte
sumallpoint(L,S) :- accSumAllPoint(L,0,S).
accSumAllPoint([],A,A).
accSumAllPoint([H|T],A,S) :- prop(H,punti,P), Anew is A+P, accSumAllPoint(T,Anew,S).

%conta gli elementi nella lista
conta(L,N) :- accConta(L,0,N), !.
accConta([],A,A).
accConta([_|T],A,N) :- Anew is A+1, accConta(T,Anew,N).

%crea tutte le K possibili partizioni del numero N
partizioni(0, 0, []) :- !.
partizioni(N, K, [X|T]) :- between(1,N,X), Nnew is N-X, Knew is K-1, partizioni(Nnew,Knew,T).

tutte_partizioni(N,K,P,NP) :- findall(X,partizioni(N,K,X),P), conta(P,NP).

sottrai([],_,[]).
sottrai([X|T],L2,R) :- member(X, L2), !, sottrai(T,L2,R).
sottrai([X|T],L2,[X|R]) :- sottrai(T,L2,R).

%turmo T, lista di carte a terra L, numero di carte a terra N
terra(T,L,N) :- findall(C,prop(C,terra,T),L), conta(L,N).

uscite(L) :- findall(C,prop(C,uscita,si),L).

carta_compagno(T,C) :- terra(T,L,_), member(C,L), prop(C,possessore,giocatore(compagno)).

n_rimanenti(T,NR) :- findall(C,prop(C,uscita,si),LU), disponibili(_,ND), conta(LU,NU), terra(T,_,NT), NR is 40-NU-ND-NT.

max(X,Y,Y) :- X =< Y,!.
max(X,_,X).

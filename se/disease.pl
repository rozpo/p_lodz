% file: disease.pl

disease(alveolitis) :-
    verify(dyspnoea),
    verify(fever),
    verify(chills),
    verify(arthralgia),
    verify(cough),
    !.

disease(berylliosis) :-
    verify(cough),
    verify(dyspnoea),
    verify(pain_in_chest),
    verify(exertion),
    !.

disease(bronchitis) :-
    verify(cough),
    verify(breathing),
    verify(muscle_aches),
    verify(bad_mood),
    !.

disease(pneumonia) :-
    verify(fever),
    verify(cough),
    verify(breathing),
    verify(muscle_aches),
    verify(chills),
    !.

disease(pneumothorax) :-
    verify(dyspnoea),
    verify(cough),
    verify(rib),
    !.

disease(respiratory_failure) :-
    verify(dyspnoea),
    verify(exertion),
    !.

disease(sarcoidosis) :-
    verify(fever),
    verify(bad_mood),
    verify(sweating),
    !.

disease(sleep_apnea) :-
    verify(lethargy),
    verify(headaches),
    verify(concentrating),
    verify(wakeup),
    verify(dyspnoea),
    !.

disease(tuberculosis) :-
    verify(fever),
    verify(cough),
    verify(hemoptysis),
    verify(sweating),
    verify(dyspnoea),
    !.

disease(whooping_cough) :-
    verify(cough),
    verify(runny_nose),
    verify(fever),
    verify(sore_throat),
    !.

disease(none).
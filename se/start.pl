% Baza wiedzy - https://www.mp.pl/pacjent/pulmonologia/choroby

% load another modules
:- consult("symptom.pl").
:- consult("diagnosis.pl").
:- consult("disease.pl").

% avoid double static include
:- dynamic disease/1.
:- dynamic possitive/1, negative/1.

% clear answers
clear :- retract(possitive(_)),fail.
clear :- retract(negative(_)),fail.
clear.

% main "function"
start :-
    clear,
    write("Prosze odpowiadac na pytania tak lub nie"), nl,
    disease(Disease),
    write("Zdiagnozowana choroba to: "),
    diagnosis(Disease). 

% verify symptom for disease
verify(Result) :-
    (possitive(Result) -> true;
    (negative(Result) -> fail; ask(Result))).

% get input from user
ask(Question) :-
    symptom(Question),
    read(Answer),
    (answer(Answer) -> assert(possitive(Question));
    assert(negative(Question)), fail).

% answer(tak).
answer(X) :- member(X,[tak, 'TAK', 'Tak']).
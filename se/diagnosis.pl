% file: diagnosis.pl

diagnosis(alveolitis) :-
    write("Zapalenie pecherzykow plucnych").

diagnosis(berylliosis) :-
    write("Beryloza").

diagnosis(bronchitis) :-
    write("Zapalenie oskrzeli").

diagnosis(pneumonia) :-
    write("Zapalenie pluc").

diagnosis(pneumothorax) :-
    write("Odma plucna").

diagnosis(respiratory_failure) :-
    write("Niewydolnosc oddechowa").

diagnosis(sarcoidosis) :-
    write("Sarkoidoza").

diagnosis(sleep_apnea) :-
    write("Bezdech senny").

diagnosis(tuberculosis) :-
    write("Gruzlica").

diagnosis(whooping_cough) :-
    write("Krztusiec").

diagnosis(none) :-
    write("Nieznana").
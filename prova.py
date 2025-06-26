from pyswip import Prolog

prolog = Prolog()
prolog.consult("csp_ambulanze.pl")  # il file con le regole Prolog

# esegui la query e prendi i risultati
result = list(prolog.query("risolvi_assegnamento(Assegnamenti)"))

# result sarà una lista di dizionari, di solito con un solo elemento
if result:
    assegnamenti = result[0]['Assegnamenti']  # questa è la lista degli assegnamenti

    for incidente, ambulanze in assegnamenti:
        print(f"Incidente {incidente} -> Ambulanze: {ambulanze}")
else:
    print("Nessun risultato trovato")

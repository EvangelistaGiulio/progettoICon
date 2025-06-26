from pyswip import Prolog

def risolvi_assegnamento():
    prolog = Prolog()
    prolog.consult("csp_ambulanze.pl")

    assegnamenti = []
    for sol in prolog.query("assegnamento(Incidente, Ambulanze)"):
        incidente = sol["Incidente"]
        ambulanze = sol["Ambulanze"]
        assegnamenti.append((incidente, ambulanze))

    return assegnamenti

if __name__ == "__main__":
    assegnamenti = risolvi_assegnamento()
    if assegnamenti:
        print("Assegnamenti ambulanze:")
        for inc, ambs in assegnamenti:
            print(f"Incidente {inc} -> Ambulanze: {ambs}")
    else:
        print("Nessun assegnamento trovato.")


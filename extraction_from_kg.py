from rdflib import Graph, Namespace, RDF, OWL

# Carica il grafo OWL inferito
g = Graph()
g.parse("kg.ttl", format="ttl")

EX = Namespace("http://example.org/incidente#")

# Estrai incidenti
incidenti = set(g.subjects(RDF.type, EX.Incidente))

# Incidenti gravi
incidenti_gravi = set(g.subjects(RDF.type, EX.IncidenteGrave))

# Persone ferite
persone_ferite = set(g.subjects(RDF.type, EX.PersonaFerita))

# Mappa incidente → persone ferite coinvolte (via "coinvolge")
incidente_feriti_map = {str(i): [] for i in incidenti}
for incidente in incidenti:
    for persona in g.objects(incidente, EX.coinvolge):
        if persona in persone_ferite:
            incidente_feriti_map[str(incidente)].append(str(persona))

# Stampa i dati per Prolog
print("Incidenti:")
with open("csp_ambulanze.pl", "w") as f:
    for i in incidenti:
        gravita = "grave" if i in incidenti_gravi else "normale"
        n_feriti = len(incidente_feriti_map[str(i)])
        print(f"    incidente('{i}', {gravita}, {n_feriti}),")
        f.write(f"incidente('{i}', {gravita}, {n_feriti}).\n")
    # Ambulanze simulate
    n_ambulanze = 5
    print("\nAmbulanze:")
    for i in range(n_ambulanze):
        print(f"    ambulanza(a{i+1}),")
        f.write(f"ambulanza(a{i+1}).\n")
f.close

print("Feriti:")
for p in persone_ferite:
    print(f" - {p}")



import os
import math
from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef

# === CONFIG ===
YOLO_DIR = "./yoloe_output"  # cartella contenente i file .txt YOLO
OUTPUT_TTL = "knowledge_graph.ttl"
THRESHOLD = 0.2

# === NAMESPACE ===
EX = Namespace("http://example.org/incidente#")
g = Graph()
g.bind("ex", EX)
g.bind("owl", OWL)
g.bind("rdfs", RDFS)

# === DICHIARAZIONE CLASSI ===
classes = {
    "Incidente": EX.Incidente,
    "Auto": EX.Auto,
    "AutoIncidentata": EX.AutoIncidentata,
    "Persona": EX.Persona
}

for name, uri in classes.items():
    g.add((uri, RDF.type, OWL.Class))

# Gerarchia: AutoIncidentata ⊆ Auto
g.add((EX.AutoIncidentata, RDFS.subClassOf, EX.Auto))

# === PROPRIETÀ ===
g.add((EX.vicino, RDF.type, OWL.ObjectProperty))
g.add((EX.vicino, RDFS.domain, EX.Persona))
g.add((EX.vicino, RDFS.range, EX.Auto))

g.add((EX.coinvolge, RDF.type, OWL.ObjectProperty))
g.add((EX.coinvolge, RDFS.domain, EX.Incidente))
g.add((EX.coinvolge, RDFS.range, EX.Persona))

# === FUNZIONE DISTANZA ===
def distanza(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# === PARSING DEI FILE YOLO ===
for fname in sorted(os.listdir(YOLO_DIR)):
    if not fname.endswith(".txt"):
        continue

    img_id = fname.replace(".txt", "")
    incident_uri = EX[f"img_{img_id}"]
    g.add((incident_uri, RDF.type, EX.Incidente))

    people = []
    autos = []

    with open(os.path.join(YOLO_DIR, fname), "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        parts = line.strip().split()
        if len(parts) < 5:
            continue
        class_id = int(parts[0])
        x, y = float(parts[1]), float(parts[2])
        bbox = (x, y)

        if class_id == 0:
            aid = f"car_inc_{img_id}_{i}"
            car_uri = EX[aid]
            g.add((car_uri, RDF.type, EX.AutoIncidentata))
            autos.append((car_uri, bbox))
        elif class_id == 2:
            aid = f"car_{img_id}_{i}"
            car_uri = EX[aid]
            g.add((car_uri, RDF.type, EX.Auto))
            autos.append((car_uri, bbox))
        elif class_id == 1:
            pid = f"person_{img_id}_{i}"
            person_uri = EX[pid]
            g.add((person_uri, RDF.type, EX.Persona))
            people.append((person_uri, bbox))

    for person_uri, p_box in people:
        for car_uri, a_box in autos:
            if distanza(p_box, a_box) < THRESHOLD:
                g.add((person_uri, EX.vicino, car_uri))
                g.add((incident_uri, EX.coinvolge, person_uri))

# === SALVA IN FORMATO TURTLE ===
g.serialize(destination=OUTPUT_TTL, format='turtle')
print(f"✅ Ontologia salvata in formato Turtle: {OUTPUT_TTL}")
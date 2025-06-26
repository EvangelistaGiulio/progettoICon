# progettoICon
# Sistema Intelligente per la Gestione di Incidenti Stradali

Il progetto dimostra un'architettura di Intelligenza Artificiale ibrida che combina tecniche di **Deep Learning** per la percezione visiva, **Knowledge Graph e Ontologie** per la rappresentazione e l'inferenza della conoscenza, e **Programmazione Logica (Prolog) con Ragionamento a Vincoli** per la risoluzione di problemi di allocazione risorse.

## 🎯 Obiettivo del Progetto

L'obiettivo principale è sviluppare un prototipo di sistema di supporto decisionale per la gestione di incidenti stradali. Il sistema mira a:
* Automatizzare l'identificazione di entità rilevanti (veicoli incidentati/non incidentati, persone) da immagini.
* Costruire una base di conoscenza strutturata per rappresentare gli scenari di incidente.
* Eseguire inferenze semantiche per categorizzare gli incidenti e derivare nuova conoscenza implicita.
* Utilizzare il ragionamento logico per risolvere problemi complessi di allocazione di risorse (es. assegnamento ambulanze).

## 🚀 Architettura del Sistema

Il sistema è strutturato in una pipeline modulare:

1.  **Modulo di Riconoscimento Visivo (YOLOe):** Processa immagini di incidenti per rilevare `crashed_car`, `car` e `person`.
2.  **Modulo di Costruzione del Knowledge Graph:** Converte l'output di YOLOe in fatti strutturati all'interno di un'ontologia OWL.
3.  **Modulo di Inferenza OWL:** Applica regole semantiche al KG per inferire nuove informazioni (es. `IncidenteGrave`, `PersonaFerita`).
4.  **Modulo di Ragionamento Logico (Prolog & CSP):** Traduce il KG in fatti Prolog e risolve un Problema di Soddisfacimento di Vincoli per l'assegnamento delle ambulanze.

## 📁 Struttura del Repository

* `yoloe_output/`: Contiene i file `.txt` con le rilevazioni di YOLOe.
* `kg.ttl`: File dell'ontologia OWL che definisce le classi, le proprietà e le regole semantiche (SWRL) del dominio degli incidenti.
* `build_kg.py`: Script Python per popolare il Knowledge Graph a partire dall'output di YOLOe.
* `extraction_from_kg.py`: Script Python per estrarre fatti rilevanti dal KG (dopo l'inferenza OWL) e convertirli in formato Prolog.
* `csp_ambulanze.pl`: Programma Prolog che definisce le regole per la prioritizzazione degli incidenti e la logica di assegnamento delle ambulanze come un CSP.
* `csp_solve.py`: Script Python che utilizza `pyswip` per eseguire il programma Prolog e ottenere le soluzioni di assegnamento delle ambulanze.
* `evaluation_charts_and_weights/`: Cartella contenente i grafici di valutazione di YOLOe (es. curve di apprendimento, metriche) e i pesi del modello fine-tunato.
* `Documentazione_Progetto.pdf` (o .docx): La documentazione completa del progetto, dettagliando teoria, implementazione e risultati.

## 🛠️ Come Eseguire il Progetto

### Prerequisiti

* Python 3.x
* SWI-Prolog
* Librerie Python: `rdflib`, `pyswip`, (e potenzialmente `torch`, `ultralytics` o framework simili se si vuole rieseguire YOLOe).

## 📊 Grafici di Valutazione YOLOe

La cartella `evaluation_charts_and_weights/` contiene i grafici generati durante l'addestramento e la valutazione del modello YOLOe. Questi includono, ad esempio, le **curve di apprendimento** (Loss Curve, Precision-Recall Curve, mAP Curve) che mostrano l'andamento delle prestazioni del modello sul training set e sul validation set durante le epoche di addestramento. Le curve di apprendimento sono fondamentali per diagnosticare problemi come overfitting o underfitting.
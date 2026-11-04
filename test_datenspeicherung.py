"""Phase 1: Prüft das Speichern und Einlesen einfacher JSON-Testdaten."""

import json


daten = {
    "studiengang": "Medizinische Informatik",
    "module": [
        {
            "name": "E-Health",
            "ects": 5,
            "status": "Bestanden",
            "note": 1.3
        }
    ]
}

# Eine eigene Testdatei verwenden, damit Studiendaten erhalten bleiben.
with open("testdaten_phase1.json", "w", encoding="utf-8") as datei:
    json.dump(
        daten,
        datei,
        ensure_ascii=False,
        indent=4
    )

with open("testdaten_phase1.json", "r", encoding="utf-8") as datei:
    geladene_daten = json.load(datei)

assert geladene_daten == daten

print("Speichern und Einlesen erfolgreich.")
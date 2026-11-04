"""Phase 1: Prüft die beschriebenen Beispielwerte für ECTS, Note und Zeit."""

from datetime import date


module = [
    {"ects": 5, "status": "Bestanden", "note": 1.3},
    {"ects": 5, "status": "Geplant", "note": None}
]

erreichte_ects = 0
notensumme = 0.0
benotete_ects = 0

for modul in module:
    if modul["status"] == "Bestanden":
        erreichte_ects += modul["ects"]

        if modul["note"] is not None:
            notensumme += modul["note"] * modul["ects"]
            benotete_ects += modul["ects"]

notendurchschnitt = notensumme / benotete_ects

# Feste Beispieldaten machen den Test unabhängig vom heutigen Datum.
startdatum = date(2026, 7, 30)
testdatum = date(2026, 8, 30)

vergangene_monate = (testdatum.year - startdatum.year) * 12
vergangene_monate += testdatum.month - startdatum.month

if testdatum.day < startdatum.day:
    vergangene_monate -= 1

assert erreichte_ects == 5
assert notendurchschnitt == 1.3
assert vergangene_monate == 1

print("ECTS:", erreichte_ects)
print("Notendurchschnitt:", notendurchschnitt)
print("Vergangene Monate:", vergangene_monate)
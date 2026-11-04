"""Phase 2: Prüft Setter, leere Modulnamen und doppelte Modulnamen."""

from semester import Semester
from modul import Modul
from modul_status import ModulStatus
from pruefungsleistung import Pruefungsleistung
from pruefungsart import Pruefungsart


pruefung = Pruefungsleistung(Pruefungsart.KLAUSUR, 1.3)
modul = Modul("E-Health", 5, ModulStatus.BESTANDEN, pruefung)

# Ein Text ist kein Wert des Enums ModulStatus.
try:
    modul.status = "Bestanden"
except ValueError as fehler:
    print("Ungültiger Status erkannt:", fehler)
else:
    raise AssertionError("Der ungültige Status wurde angenommen.")

assert modul.status == ModulStatus.BESTANDEN

for falsche_note in (0.9, 5.1):
    try:
        pruefung.note = falsche_note
    except ValueError as fehler:
        print("Ungültige Note erkannt:", fehler)
    else:
        raise AssertionError("Die ungültige Note wurde angenommen.")

assert pruefung.note == 1.3

try:
    Modul("", 5, ModulStatus.GEPLANT)
except ValueError as fehler:
    print("Leerer Modulname erkannt:", fehler)
else:
    raise AssertionError("Der leere Modulname wurde angenommen.")

semester = Semester(1)
semester.modul_hinzufuegen(modul)

doppeltes_modul = Modul("E-Health", 5, ModulStatus.GEPLANT)

try:
    semester.modul_hinzufuegen(doppeltes_modul)
except ValueError as fehler:
    print("Doppelter Modulname erkannt:", fehler)
else:
    raise AssertionError("Der doppelte Modulname wurde angenommen.")

assert len(semester.module) == 1

print("Kapselung und Validierung erfolgreich geprüft.")
"""Phase 2: Überträgt dasselbe Modulobjekt in ein anderes Semester."""

from semester import Semester
from modul import Modul
from modul_status import ModulStatus
from pruefungsleistung import Pruefungsleistung
from pruefungsart import Pruefungsart


erstes_semester = Semester(1)
zweites_semester = Semester(2)

pruefung = Pruefungsleistung(Pruefungsart.KLAUSUR, 1.3)
modul = Modul("E-Health", 5, ModulStatus.BESTANDEN, pruefung)

erstes_semester.modul_hinzufuegen(modul)
assert erstes_semester.module[0] is modul

erstes_semester.modul_entfernen(modul)
zweites_semester.modul_hinzufuegen(modul)

# Mit is wird die Identität des Objekts geprüft.
assert len(erstes_semester.module) == 0
assert len(zweites_semester.module) == 1

assert zweites_semester.module[0] is modul
assert zweites_semester.module[0].pruefungsleistung is pruefung
assert zweites_semester.module[0].pruefungsleistung.note == 1.3

print("Dasselbe Modul wurde mit Prüfungsleistung und Note übertragen.")
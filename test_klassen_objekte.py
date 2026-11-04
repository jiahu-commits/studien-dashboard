"""Phase 2: Prüft die Objekte und die Referenz auf die Prüfungsleistung."""

from modul import Modul
from modul_status import ModulStatus
from pruefungsleistung import Pruefungsleistung
from pruefungsart import Pruefungsart


pruefung = Pruefungsleistung(Pruefungsart.KLAUSUR, 1.3)
modul = Modul("E-Health", 5, ModulStatus.BESTANDEN, pruefung)

assert pruefung.pruefungsart == Pruefungsart.KLAUSUR
assert pruefung.note == 1.3

assert modul.name == "E-Health"
assert modul.ects == 5
assert modul.status == ModulStatus.BESTANDEN

assert modul.pruefungsleistung is pruefung
assert modul.pruefungsleistung.pruefungsart == Pruefungsart.KLAUSUR
assert modul.pruefungsleistung.note == 1.3

print("Objekte und zugehörige Prüfungsleistung korrekt ausgelesen.")
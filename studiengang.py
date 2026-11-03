from dataclasses import dataclass, field
from datetime import date
from semester import Semester

@dataclass
class Studiengang:
    """Enthält die Studienplanung und verwaltet die zugehörigen Semester."""
    name: str
    startdatum: date
    gesamt_ects: int
    studiendauer_monate: int
    zielnote: float
    semester: list[Semester] = field(default_factory=list)

    def semester_hinzufuegen(self, neues_semester: Semester) -> None:
        self.semester.append(neues_semester)

    def semester_entfernen(self, zu_entfernendes_semester: Semester) -> None:
        """Entfernt nur ein zugehöriges, leeres Semester mit der höchsten Nummer.
        Bei einer unzulässigen Löschung wird ein ValueError ausgelöst, den die
        View als verständliche Meldung anzeigen kann.
        """
        if zu_entfernendes_semester not in self.semester:
            raise ValueError("Dieses Semester gehört nicht zum Studiengang.")

        hoechste_nummer = max(semester.nummer for semester in self.semester)

        if zu_entfernendes_semester.nummer != hoechste_nummer:
            raise ValueError("Es kann nur das letzte Semester entfernt werden.")

        if zu_entfernendes_semester.module:
            raise ValueError("Dieses Semester enthält noch Module und kann " "deshalb nicht entfernt werden.")

        self.semester.remove(zu_entfernendes_semester)
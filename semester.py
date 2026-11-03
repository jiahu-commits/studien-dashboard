from dataclasses import dataclass, field
from modul import Modul

@dataclass
class Semester:
    """Verwaltet die Module eines Semesters in einer eigenen Liste."""
    nummer: int
    module: list[Modul] = field(default_factory=list)

    def modul_hinzufuegen(self, neues_modul: Modul) -> None:
        """Verhindert einen bereits vorhandenen Modulnamen innerhalb dieses Semesters."""
        for aktuelles_modul in self.module:
            if aktuelles_modul.name == neues_modul.name:
                raise ValueError("Dieses Modul existiert in diesem Semester bereits.")

        self.module.append(neues_modul)

    def modul_entfernen(self, zu_entfernendes_modul: Modul) -> None:
        """Entfernt die Zuordnung des übergebenen Moduls zu diesem Semester.
        Eine vorhandene Referenz auf das Modulobjekt kann weiterverwendet werden.
        """
        self.module.remove(zu_entfernendes_modul)



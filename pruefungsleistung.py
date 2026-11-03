from dataclasses import dataclass
from pruefungsart import Pruefungsart

@dataclass
class Pruefungsleistung:
    """Enthält eine Prüfungsart und eine optionale Note.
    Die Properties prüfen zugewiesene Werte auch ausserhalb der Oberfläche.
    """
    _pruefungsart: Pruefungsart
    _note: float | None = None

    def __post_init__(self) -> None:
        """Prüft die Anfangswerte über die Setter der Properties."""
        self.pruefungsart = self._pruefungsart
        self.note = self._note


    @property
    def pruefungsart(self) -> Pruefungsart:
        return self._pruefungsart

    @pruefungsart.setter
    def pruefungsart(self, neue_pruefungsart: Pruefungsart) -> None:
        """Akzeptiert ausschliesslich Werte der Enumeration Pruefungsart."""
        if not isinstance(neue_pruefungsart, Pruefungsart):
            raise ValueError ("Ungültige Prüfungsart")

        self._pruefungsart = neue_pruefungsart

    @property
    def note(self) -> float | None:
        return self._note

    @note.setter
    def note(self, neue_note: float | None) -> None:
        """Erlaubt None für eine fehlende Note oder eine Zahl von 1.0 bis 5.0.
        Die Übereinstimmung mit dem Modulstatus wird in Modul geprüft.
        """
        if neue_note is not None:
            if not isinstance(neue_note, (int, float)):
                raise ValueError("Die Note muss eine Zahl sein.")

            if not 1.0 <= neue_note <= 5.0:
                raise ValueError("Die Note muss zwischen 1.0 und 5.0 liegen.")

        self._note = neue_note


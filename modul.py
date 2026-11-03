from dataclasses import dataclass
from pruefungsleistung import Pruefungsleistung
from modul_status import ModulStatus

@dataclass
class Modul:
    """Enthält die Daten eines Moduls und prüft die Kombination aus Status und Note."""
    name: str
    ects: int
    _status: ModulStatus
    pruefungsleistung: Pruefungsleistung | None = None

    def __post_init__(self) -> None:
        """Prüft den Namen und den anfänglichen Status mit der Prüfungsleistung."""
        if not self.name.strip():
            raise ValueError(
                "Bitte gib einen Modulnamen ein."
            )

        self.status = self._status

    @property
    def status(self) -> ModulStatus:
        return self._status

    @status.setter
    def status(self, neuer_status: ModulStatus) -> None:
        """Prüft einen neuen Status zusammen mit der vorhandenen Prüfungsleistung."""
        self._status_und_note_pruefen(
            neuer_status,
            self.pruefungsleistung
        )

        self._status = neuer_status

    def pruefungsdaten_aendern(
            self,
            neuer_status: ModulStatus,
            neue_pruefungsleistung: Pruefungsleistung | None
    ) -> None:
        """Prüft die neue Kombination vor der Übernahme beider Werte.
        So kann beispielsweise eine nicht bestandene Prüfung mit Note 5.0
        gemeinsam auf Bestanden mit einer passenden neuen Note geändert werden.
        Bei einer ungültigen Kombination bleiben die bisherigen Werte erhalten.
        """
        self._status_und_note_pruefen(
            neuer_status,
            neue_pruefungsleistung
        )

        self._status = neuer_status
        self.pruefungsleistung = neue_pruefungsleistung

    def _status_und_note_pruefen(
            self,
            status: ModulStatus,
            pruefungsleistung: Pruefungsleistung | None
    ) -> None:
        """Erlaubt fehlende Noten bei allen gültigen Statuswerten.
        Vorhandene Noten dürfen bei Bestanden höchstens 4.0 sein; bei Nicht bestanden
        ist nur 5.0 erlaubt. Andere Statuswerte erlauben keine Note. Den allgemeinen
        Notenbereich prüft bereits die Klasse Pruefungsleistung.
        """
        if not isinstance(status, ModulStatus):
            raise ValueError("Ungültiger Modulstatus")

        if pruefungsleistung is None:
            return

        note = pruefungsleistung.note

        if note is None:
            return

        if status == ModulStatus.BESTANDEN:
            if note > 4.0:
                raise ValueError(
                    "Bei bestandenen Modulen darf die Note "
                    "höchstens 4.0 sein."
                )

        elif status == ModulStatus.NICHT_BESTANDEN:
            if note != 5.0:
                raise ValueError(
                    "Bei nicht bestandenen Modulen ist "
                    "nur die Note 5.0 erlaubt."
                )

        else:
            raise ValueError(
                "Eine Note kann nur bei bestandenen oder "
                "nicht bestandenen Modulen eingetragen werden."
            )






from dataclasses import dataclass
from pruefungsleistung import Pruefungsleistung
from modul_status import ModulStatus

@dataclass
class Modul:
    name: str
    ects: int
    _status: ModulStatus
    pruefungsleistung: Pruefungsleistung | None = None

    def __post_init__(self) -> None:
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






from enum import Enum

class ModulStatus(Enum):
    """Legt die im Dashboard vorgesehenen Bearbeitungs- und Ergebnisstatus fest."""
    GEPLANT = "Geplant"
    IN_BEARBEITUNG = "In Bearbeitung"
    IN_KORREKTUR = "In Korrektur"
    BESTANDEN = "Bestanden"
    NICHT_BESTANDEN = "Nicht bestanden"
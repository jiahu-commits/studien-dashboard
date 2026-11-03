from enum import Enum

class Pruefungsart(Enum):
    """Legt die auswählbaren Prüfungsarten und ihre Anzeigetexte fest."""
    KLAUSUR = "Klausur"
    ADVANCED_WORKBOOK = "Advanced Workbook"
    PORTFOLIO = "Portfolio"
    FACHPRAESENTATION = "Fachpräsentation"
    FALLSTUDIE ="Fallstudie"
    HAUSARBEIT ="Hausarbeit"
    PROJEKTPRAESENTATION = "Projektpräsentation"
    SEMINARARBEIT = "Seminararbeit"
    BACHELORARBEIT_KOLLOGQUIUM = "Bachelorarbeit + Kolloquium"
    PRAXISREFLEXION = "Praxisreflexion"


from studiengang import Studiengang
from studienfortschritt_service import StudienfortschrittService
from json_repository import JsonRepository
from dashboard_controller import DashboardController
from dashboard_view import DashboardView


class DashboardApplication:
    """Erstellt und verbindet Service, Repository, Controller und View."""
    def __init__(self, aktueller_studiengang: Studiengang) -> None:
        """Lädt vorhandene Studiendaten vor dem Erstellen des Controllers.
        Fehlt die Datei, wird der übergebene Studiengang verwendet.
        """
        self.service = StudienfortschrittService()
        self.repository = JsonRepository()

        try:
            aktueller_studiengang = self.repository.laden(
                "studiendaten.json"
            )
        except FileNotFoundError:
            pass

        self.controller = DashboardController(
            aktueller_studiengang,
            self.service,
            self.repository
        )

        self.view = DashboardView(self.controller)

    def starten(self)->None:
        self.view.starten()

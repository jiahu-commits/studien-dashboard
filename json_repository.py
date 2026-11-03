import json
from datetime import date

from studiengang import Studiengang
from semester import Semester
from modul import Modul
from pruefungsleistung import Pruefungsleistung
from modul_status import ModulStatus
from pruefungsart import Pruefungsart

class JsonRepository:
    """Speichert den Studiengang als JSON und baut ihn beim Laden wieder auf."""
    def speichern(self, aktueller_studiengang: Studiengang, dateipfad: str) -> None:
        """Überführt Studiengang, Semester, Module und Prüfungsleistungen in JSON-Daten.
        Das Datum wird im ISO-Format und Enums werden mit ihren Anzeigewerten
        gespeichert. Fehlende Prüfungsleistungen und Noten werden zu JSON-null.
        """
        daten = {
            "name": aktueller_studiengang.name,
            "startdatum": aktueller_studiengang.startdatum.isoformat(),
            "gesamt_ects": aktueller_studiengang.gesamt_ects,
            "studiendauer_monate": aktueller_studiengang.studiendauer_monate,
            "zielnote": aktueller_studiengang.zielnote,
            "semester": []
         }

        for aktuelles_semester in aktueller_studiengang.semester:
            semester_daten = {
                "nummer": aktuelles_semester.nummer,
                "module" : []
            }
            for aktuelles_modul in aktuelles_semester.module:
                modul_daten = {
                    "name": aktuelles_modul.name,
                    "ects": aktuelles_modul.ects,
                    "status": aktuelles_modul.status.value,

                }

                aktuelle_pruefungsleistung = aktuelles_modul.pruefungsleistung

                if aktuelle_pruefungsleistung is not None:
                       modul_daten["pruefungsleistung"] = {
                        "pruefungsart": aktuelle_pruefungsleistung.pruefungsart.value,
                        "note": aktuelle_pruefungsleistung.note
                    }

                else:
                    modul_daten["pruefungsleistung"] = None

                semester_daten["module"].append(modul_daten)

            daten["semester"].append(semester_daten)

        with open(dateipfad, "w", encoding="utf-8") as datei:
            json.dump(
                daten,
                datei,
                ensure_ascii=False,
                indent=4
            )


    def laden(self, dateipfad: str) -> Studiengang:
        """Erstellt die fachlichen Objekte aus den gespeicherten JSON-Daten.
        Dabei werden Datum und Enum-Werte zurückgewandelt und die Prüfungen
        der verwendeten Konstruktoren und Hinzufüge-Methoden ausgeführt.
        """
        with open(dateipfad, "r", encoding="utf-8") as datei:
            daten = json.load(datei)
        geladener_studiengang = Studiengang(
            daten["name"],
            date.fromisoformat(daten["startdatum"]),
            daten["gesamt_ects"],
            daten["studiendauer_monate"],
            daten["zielnote"]
        )

        for gespeicherte_semesterdaten in daten["semester"]:
            geladenes_semester = Semester(
                gespeicherte_semesterdaten["nummer"]
            )

            for gespeicherte_moduldaten in gespeicherte_semesterdaten["module"]:
                gespeicherte_pruefungsdaten = gespeicherte_moduldaten["pruefungsleistung"]

                if gespeicherte_pruefungsdaten is not None:
                    geladene_pruefungsleistung = Pruefungsleistung(
                        Pruefungsart(gespeicherte_pruefungsdaten["pruefungsart"]),
                        gespeicherte_pruefungsdaten["note"]
                    )

                else:
                 geladene_pruefungsleistung = None

                geladenes_modul = Modul(
                    gespeicherte_moduldaten["name"],
                    gespeicherte_moduldaten["ects"],
                    ModulStatus(gespeicherte_moduldaten["status"]),
                    geladene_pruefungsleistung
                )

                geladenes_semester.modul_hinzufuegen(geladenes_modul)

            geladener_studiengang.semester_hinzufuegen(geladenes_semester)

        return geladener_studiengang





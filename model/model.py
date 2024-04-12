from database.studente_DAO import StudenteDAO
from database.corso_DAO import CorsoDAO


class Model:
    def __init__(self):
        self._mappaStudenti = StudenteDAO().getStudenti()
        self._mappaCorsi = CorsoDAO().getCorsi()


    def get_studenti(self):
        return self._mappaStudenti

    def get_corsi(self):
        return self._mappaCorsi

    def cercaCorso(self, codiceCorso):
        return self._mappaCorsi[codiceCorso]

    def cercaStudente(self, matricola):
        return self._mappaStudenti[matricola]

    def cercaIscritti(self, codiceCorso):
        return self.cercaCorso(codiceCorso).listaStudenti





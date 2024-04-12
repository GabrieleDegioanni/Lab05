# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class StudenteDAO:

    def __init__(self):
        pass

    def getStudenti(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                FROM studente"""
        cursor.execute(query)
        # result = []
        result = {}
        for row in cursor:
            #result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
            result[row["matricola"]] = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"], [])
        cursor.close()
        cnx.close()

        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    FROM iscrizione"""
        cursor.execute(query)
        for row in cursor:
            result[row["matricola"]].listaCorsi.append(row["codins"])
        cursor.close()
        cnx.close()

        return result


if __name__ == '__main__':
    studenti_dao = StudenteDAO()
    for k in studenti_dao.getStudenti().keys():
        print(studenti_dao.getStudenti()[k])
        print(studenti_dao.getStudenti()[k].listaCorsi)

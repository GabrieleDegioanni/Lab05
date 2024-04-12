# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


class CorsoDAO:

    def __init__(self):
        pass

    def getCorsi(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                FROM corso"""
        cursor.execute(query)
        #result = []
        result = {}
        for row in cursor:
            #result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
            result[row["codins"]] = Corso(row["codins"], row["crediti"], row["nome"], row["pd"], [])
        cursor.close()
        cnx.close()

        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    FROM iscrizione"""
        cursor.execute(query)
        for row in cursor:
            result[row["codins"]].listaStudenti.append(row["matricola"])
        cursor.close()
        cnx.close()

        return result


if __name__ == '__main__':
    corsi_dao = CorsoDAO()
    for k in corsi_dao.getCorsi().keys():
        print(corsi_dao.getCorsi()[k])
        print(corsi_dao.getCorsi()[k].listaStudenti)

#!/usr/bin/python3
"""
   script that takes in arguments and displays all values in the states tab   le of hbtn_0e_0_usa
   where name matches the argument. But this time, write one that is safe     from MySQL injections!
"""

from sys import argv
import MYSQLdb

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name=%s ORDER BY id ASC"""
    cursor.execute(sql_cmd, (argv[4],))

    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()

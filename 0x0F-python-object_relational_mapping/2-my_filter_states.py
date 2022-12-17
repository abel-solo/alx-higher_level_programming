#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], port=3306, host="localhost",
                         passwd=argv[2], db=argv[3])
    current = db.cursor()
    current.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    states = current.fetchall()
    for state in states:
        if state[1] == argv[4]:
            print(state)
    current.close()
    db.close()

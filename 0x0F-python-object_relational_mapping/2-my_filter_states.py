#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.argv[3], host="localhost")
    current = db.cursor()
    current.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    states = current.fetchall()
    [for state in states print(state) if state[1] == argv[4]] 

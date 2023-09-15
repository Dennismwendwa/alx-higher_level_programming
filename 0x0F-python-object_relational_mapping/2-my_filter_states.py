#!/usr/bin/python3
"""
Script that takes arguments and display all values of states
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        print(
                "Usage: {} <username> <password> <database> <state>"
                .format(sys.argv[0])
                )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
                host="localhost", port=3306,
                user=username, password=password,
                db=database_name
                )
        cursor = db.cursor()
        qu = "SELECT * FROM states WHERE name = %s ORDER BY id asc"
        cursor.execute(qu, (state_name,))
        states = cursor.fetchall()

        for k in states:
            print(k)

    except MySQLdb.Error as e:
        pass
        sys.exit(1)

    finally:
        cursor.close()
        db.close()

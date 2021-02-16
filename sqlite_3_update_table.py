import sqlite3
from sqlite3 import Error

def update_task(conn, task):
    """
    update priority, begin_date, and end_date of a tasks
    :param conn:
    :param task:
    :return: project id
    """

    sql = '''UPDATE tasks
            SET priority = ?,
                begin_date = ?,
                end_date = ?
            WHERE id = ?'''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()



def create_connection(db_file):
    """ create a database connection to a SQLite database """

    conn = None

    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn


def main():
    database = r"db/pythonsqlite.db"

    # create a database Connection
    conn = create_connection(database)

    with conn:
        update_task(conn, (2, '2015-01-04', '2015-01-06', 2))

if __name__ == '__main__':
    main()

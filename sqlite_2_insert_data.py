import sqlite3
from sqlite3 import Error


def create_project(conn, project):
    """
    Create a new project into hte projects tables
    :param conn:
    :param project:
    :return: prject id
    """

    sql = ''' INSERT INTO projects(name, begin_date, end_date)
                VALUES(?, ?, ?)'''

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()

    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name, priority, status_id, project_id, begin_date, end_date)
                VALUES(?, ?, ?, ?, ?, ?)'''

    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid


def create_connection(db_file):
    """ create a database connection to a SQLite database """

    conn = None

    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """
    create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)

    except Error as e:
        print(e)



def main():
    database = r"db/pythonsqlite.db"

    # create a database Connection
    conn = create_connection(database)

    with conn:
        # create a new project
        project = ('Cool App with SQlite & Python', '2015-01-01', '2015-01-30')
        project_id = create_project(conn, project)

        # task
        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm  with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)

if __name__ == '__main__':
    main()

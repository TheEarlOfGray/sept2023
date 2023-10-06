import pyodbc

cs = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

queryStr = """CREATE TABLE random (
    id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    PRIMARY KEY (id));
    """

queryStr2 = """IF EXISTS(
    SELECT TABLE_NAME, TABLE_SCHEMA
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME='random'
    AND TABLE_SCHEMA='dbo')
    BEGIN
        DROP TABLE random
    END"""


def dbQuery(query):
    conn = pyodbc.connect(cs)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()
    return None

dbQuery(queryStr2)
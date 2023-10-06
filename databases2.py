import pyodbc

cs = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

queryStr = """INSERT INTO company 
VALUES (7000, 'Tims Software Ltd', '01234567894', 'London', 'LO1 1PT');"""

queryStr2 = """UPDATE company
SET tel='11111111111'
WHERE company_no=5000"""

def dbQuery(query):
    conn = pyodbc.connect(cs)
    cur = conn.cursor()
    cur.execute(queryStr2)
    conn.commit()
    conn.close()
    return None

dbQuery(queryStr2)
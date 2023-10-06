import pyodbc
connectionString = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

# with open('students.csv', 'r') as file1:
#     result = file1.readlines()

# for line in result:
#     query = line.split(',')
#     sqlStr=f"""INSERT INTO Student
#     VALUES ('{int(query[0])}', '{query[1]}', '{query[2]}', '{query[3]}', '{query[4]}');"""
#     conn = pyodbc.connect(connectionString)
#     cur = conn.cursor() 
#     cur.execute(sqlStr)
#     conn.commit()
#     conn.close()



sqlStr=f"""UPDATE Student
SET FirstName='Tony'
WHERE StudentID=4;"""
conn = pyodbc.connect(connectionString)
cur = conn.cursor() 
cur.execute(sqlStr)
conn.commit()
conn.close()

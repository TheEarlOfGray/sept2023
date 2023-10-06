import pyodbc

# def objcreate(list1):
#     for item in list1:
#         coID, name, phone, city, postcode = item
#         print(name)
#         print(phone)

cs = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

def dbQuery(query):
    try:
        conn = pyodbc.connect(cs)
        cur = conn.cursor()
        result = cur.execute(query).fetchall()
        conn.close()
        return result
    except:
        return None


# result = dbQuery("SELECT * FROM company WHERE company_no>='1000' ORDER BY company_name DESC")

result = dbQuery("SELECT * FROM company")

try:
    for row in result:
        if row != None:
            tup = tuple(row)  
            print(tup)
except:
    print("Error reading data!")

import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Ravi@2000'
)
cur=conn.cursor()
class deleted:
    def departmentdeleted(x,columnname,departmentid):
        cur.execute(f"delete from department where {columnname}={departmentid}")
        conn.commit()
    def coursedeleted(x,columnname,departmentid):
        cur.execute(f"delete from department where {columnname}={departmentid}")
        conn.commit()
    def facultydeleted(x,columnname,departmentid):
        cur.execute(f"delete from department where {columnname}={departmentid}")
        conn.commit()
    def studentdeleted(x,columnname,departmentid):
        cur.execute(f"delete from department where {columnname}={departmentid}")
        conn.commit()
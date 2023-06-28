import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Ravi@2000'
)
cur=conn.cursor()
class readed:
    def departmentreaded(x,columnname,departmentid):
        cur.execute(f"select * from department where {columnname}={departmentid}")
        print(cur.fetchall())
    def coursereaded(x,columnname,courseid):
        cur.execute(f"select * from department where {columnname}={courseid}")
        print(cur.fetchall())
    def facultyreaded(x,columnname,facultyid):
        cur.execute(f"select * from department where {columnname}={facultyid}")
        print(cur.fetchall())
    def studentreaded(x,columnname,studentid):
        cur.execute(f"select * from department where {columnname}={studentid}")
        print(cur.fetchall())
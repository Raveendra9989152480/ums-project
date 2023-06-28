import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Ravi@2000'
)
cur=conn.cursor()
class updated:

    def departmentupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update department set {columnname}='{newvalue}' where {columnname}='{oldvalue}'")
        conn.commit()
    def courseupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update course set {columnname}='{newvalue}' where {columnname}='{oldvalue}'")
        conn.commit()
    def facultyupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update faculty set {columnname}='{newvalue}' where {columnname}='{oldvalue}'")
        conn.commit()
    def studentupdate(x,columnname,newvalue,oldvalue):
        cur.execute(f"update student set {columnname}='{newvalue}' where {columnname}='{oldvalue}'")
        conn.commit()

            
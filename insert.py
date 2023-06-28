import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Ravi@2000'
)
cur=conn.cursor()
class inserted:

    def departmentinsert(x,departmentid,departmentname):
        cur.execute(f"insert into department values({departmentid},'{departmentname}')")
        conn.commit()
    def courseinsert(x,COURSEID ,COURSENAME ,COURSEFEE ,DURATION):
        cur.execute(f"insert into course values({COURSEID},'{COURSENAME}',{COURSEFEE},{DURATION})")
        conn.commit()
    def facultyinsert(x,FACULTYID,FACULTYNAME ,DEPARTMENTID ,SALLARY ,COURSEID):
        cur.execute(f"insert into faculty values({FACULTYID},'{FACULTYNAME}',{DEPARTMENTID},{SALLARY },{COURSEID})")
        conn.commit()
    def studentinsert(x, SID,SNAME ,COURSEID ,DEPARTMENTID):
        cur.execute(f"insert into student values({SID},'{SNAME}',{COURSEID},{DEPARTMENTID})")
        conn.commit()


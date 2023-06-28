from insert import inserted
from update import updated
from delete import deleted
from read import readed

obj=inserted()
obj1=updated()
obj2=deleted()
obj3=readed()

print("Welcome to the University Management System!")
print("Database Information:")
print("- Number of tables: 4")
print("- Table names: Student, Department, Faculty, Course")

# Displaying student table information
print("\nStudent Table Information:")
print("- Number of records: 4")
print("- Columns: sid, sname, courseid, dptid")

# Displaying department table information
print("\nDepartment Table Information:")
print("- Number of records: 2")
print("- Columns: departmentid, departmentname")

# Displaying faculty table information
print("\nFaculty Table Information:")
print("- Number of records: 5")
print("- Columns: facultyid, facultyname, departmentid, salary, courseid")

# Displaying course table information
print("\nCourse Table Information:")
print("- Number of records: 4")
print("- Columns: courseid, coursename, coursefees, duration")

print("** you can do 4 operations on database ***")

print('for update the data write "update"') 
print('for delete the data write "delete"')
print('for read the data write "read"')
print('for insert the data write "add"')


opr=input('enter any operation:')


if opr=="add":
    print('for inserting the data in departmnet table press - 1')
    print('for inserting the data in course table press - 2')
    print('for inserting the data in faculty table press - 3')
    print('for inserting the data in student table press - 4')
    tab=int(input("please enter the number to insert data in table:"))
    if tab==1:
        departmentid = int(input("Please Enter department id:"))
        departmentname = input("please Enter Department Name:")
        obj.departmentinsert(departmentid,departmentname)
        print('data entered successfully')
    elif tab==2:
        COURSEID = int(input("Please enter courseid:"))
        COURSENAME = input("please Enter course name:")
        COURSEFEE=int(input('please enter coursefee:'))
        DURATION=int(input('please enter the duration of course in months:'))
        obj.courseinsert(COURSEID,COURSENAME,COURSEFEE,DURATION)
        print('data entered successfully')
    elif tab==3:
       FACULTYID=int(input('please enter facultyid:'))
       FACULTYNAME=input('please enter facultyname:')
       DEPARTMENTID=int(input('please enter departmentid:'))
       SALLARY=int(input('please enter sallary:'))
       COURSEID=int(input('please enter courseid:'))
       obj.facultyinsert(FACULTYID,FACULTYNAME ,DEPARTMENTID ,SALLARY ,COURSEID)
       print('data entered successfully')
    elif tab==4:
        SID=int(input('please enter student id:'))
        SNAME= input('enter the student name:')
        COURSEID=int(input('please enter courseid:'))
        DEPARTMENTID=int(input('please enter departmentid:'))
        obj.studentinsert(SID,SNAME ,COURSEID ,DEPARTMENTID)
        print('data entered successfully')


if opr=="update":
    print('for updating the data in departmnet table press - 1')
    print('for updating the data in course table press - 2')
    print('for updating the data in faculty table press - 3')
    print('for updating the data in student table press - 4')
    tab=int(input("please enter the number to insert data in table:"))
    if tab==1:
        columnname=str(input("Please Enter columnname:"))
        newname=str(input('enter the new value:'))
        oldname=str(input('enter the old value:'))
        obj1.departmentupdate(columnname,newname,oldname)
        print('data updated successfully')
    elif tab==2:
        columnname=str(input("Please Enter columnname:"))
        newname=str(input('enter the new value:'))
        oldname=str(input('enter the old value:'))
        obj1.courseupdate(columnname,newname,oldname)
        print('data updated successfully')
    elif tab==3:
        columnname=str(input("Please Enter columnname:"))
        newname=str(input('enter the new value:'))
        oldname=str(input('enter the old value:'))
        obj1.facultyupdate(columnname,newname,oldname)
        print('data updated successfully')
    elif tab==4:
        columnname=str(input("Please Enter columnname:"))
        newname=str(input('enter the new value:'))
        oldname=str(input('enter the old value:'))
        obj1.studentupdate(columnname,newname,oldname)
        print('data updated successfully')
    
    
if opr=='delete':
    print('for updating the data in departmnet table press - 1')
    print('for updating the data in course table press - 2')
    print('for updating the data in faculty table press - 3')
    print('for updating the data in student table press - 4')
    tab=int(input("please enter the number to insert data in table:"))
    if tab==1:
        columnname=str(input('ented the columnname:'))
        departmentid=int(input('enter the departemntid:'))
        obj2.departmentdeleted(columnname,departmentid)
    if tab==2:
        columnname=str(input('ented the columnname:'))
        COURSEID=int(input('enter the courseid:'))
        obj2.departmentdeleted(columnname,COURSEID)
    if tab==3:
        columnname=str(input('ented the columnname:'))
        FACULTYID=int(input('enter the departemntid:'))
        obj2.departmentdeleted(columnname,FACULTYID)
    if tab==4:
        columnname=str(input('ented the columnname:'))
        studentid=int(input('enter the departemntid:'))
        obj2.departmentdeleted(columnname,studentid)
if opr=='read':
    print('for updating the data in departmnet table press - 1')
    print('for updating the data in course table press - 2')
    print('for updating the data in faculty table press - 3')
    print('for updating the data in student table press - 4')
    tab=int(input("please enter the number to insert data in table:"))
    if tab==1:
        columnname=str(input('ented the columnname:'))
        departmentid=int(input('enter the departemntid:'))
        obj3.departmentreaded(columnname,departmentid)
    if tab==2:
        columnname=str(input('ented the columnname:'))
        courseid=int(input('enter the courseid:'))
        obj3.departmentreaded(columnname,courseid)
    if tab==3:
        columnname=str(input('ented the columnname:'))
        facultyid=int(input('enter the facultyid:'))
        obj3.departmentreaded(columnname,facultyid)
    if tab==4:
        columnname=str(input('ented the columnname:'))
        studentid=int(input('enter the studentid:'))
        obj3.departmentreaded(columnname,studentid)

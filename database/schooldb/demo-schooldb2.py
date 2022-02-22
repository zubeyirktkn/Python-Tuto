from connection import connection
from datetime import datetime
import mysql

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.studentNumber=studentNumber
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.gender=gender
        
    
    def saveStudent(self):
        sql="INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        value=(self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()# executemany ve execute commitle çalışmasını tamamlar
        except  mysql.connector.Error as err:
            print("hata",err)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        sql="INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values=students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()# executemany ve execute commitle çalışmasını tamamlar
        except  mysql.connector.Error as err:
            print("hata",err)
        finally:
            Student.connection.close()
    
    @staticmethod
    def StudentInfo():
        sql="Select * From student LIMIT 5"
        #sql="Select StudentNumber,Name,Surname From student "
        #sql="Select Name,Surname From student where gender='K' "
        #sql="Select * From student where YEAR(birthdate)=2003 "
        #sql="Select * From student where YEAR(birthdate)=2005 and Name='Ali' "
        #sql="Select * From student where Name like '%an%' or Surname like '%an%' "
        #sql="Select COUNT(id) From student where gender='E' "
        #sql="Select Name,Surname From student where gender='K' order by name,surname "

        Student.mycursor.execute(sql)

        try:
            results=Student.mycursor.fetchall()
            #print(results)
            
            for result in results:
                print(f"{result[2]} {result[3]}")
            
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
            Student.connection.close()
        
    
    @staticmethod
    def getStudentById(id):
        sql="select * from student where id=%s"
        param=(id,)

        Student.mycursor.execute(sql,param)

        try:
            obj= Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print("Error",err)
        

    def updateStudent(self):
        sql="update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"                
        params=(self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,params)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata",err)
        


student=Student.getStudentById(14)

student.name="Zübeyir"
student.surname="Aktekin"
student.updateStudent()

#ahmet = Student("107","Metin","Ali",datetime(1999,2,13),"E")
#ahmet.saveStudent()

"""
ogrenciler=[
    ("201","Ahmet","Yılmaz",datetime(2005,5,17),"E"),
    ("202","Ali","Can",datetime(2005,6,17),"E"),
    ("203","Canan","Tan",datetime(2005,7,7),"K"),
    ("204","Ayşe","Taner",datetime(2005,9,23),"K"),
    ("205","Bahadır","Toksöz",datetime(2004,7,27),"E"),
    ("206","Ali","Cenk",datetime(2003,8,25),"E")
]
Student.saveStudents(ogrenciler)
"""
#Student.StudentInfo()
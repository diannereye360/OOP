import StudentClass as sc

studentid = 1001
name = 'John'
dob = '01/23/1993'
classification = 'junior'

student1 = sc.Student(studentid,name,dob,classification)

student1.calc_age()

student1.register()

print('Student age is',student1.return_age())
print('Student can register between',student1.return_registration())
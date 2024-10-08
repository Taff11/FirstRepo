student_name = input("Enter Your Name: ")
admin_number = input("Enter Your Admission Number: ")
oop_marks = int(input("Enter Your OOP Marks: "))
bms_marks =int(input("Enter Your BMS Marks: "))
devptstudies_marks = int(input("Enter Your Development Studies Marks: "))
electronics_marks = int(input("Enter Your Electronics Marks: "))
physics_marks = int(input("Enter Your Physics Marks: "))
algorithms_marks = int(input("Enter Your Data Structures And Algorithms Marks: "))
accounting_marks = int(input("Enter Your Accounting For Business Marks: "))
datacomm_marks = int(input("Enter Your Data Communications and Networks Marks: "))
compapplication_marks = int(input("Enter Your Computer Appliication Literacy Marks: "))
      

total_marks = oop_marks+bms_marks+devptstudies_marks+electronics_marks+physics_marks+algorithms_marks+accounting_marks+datacomm_marks+compapplication_marks
average_marks = total_marks/9

if average_marks >= 75:
 grade = 'A'
elif 70 <= average_marks < 75:
 grade = 'B+'
elif 60 <= average_marks < 70:
 grade = 'B'
elif 50 <= average_marks < 60:
 grade = 'C+'
elif 40 <= average_marks < 50:
 grade = 'C'
else:
 grade = 'FAIL'

print("\nStudent Name:",student_name)
print("Admission Number:",admin_number)
print("Marks obtained - OOP:",oop_marks,"BMS:",bms_marks,"Development Studies:",devptstudies_marks,"Electronics:",electronics_marks,"Physics:",physics_marks,"Data Structures And Algorithms:",algorithms_marks,"Accounting For Business:",accounting_marks,"Data Communications and Networks:",datacomm_marks,"Computer Application Literacy:",compapplication_marks)
print("Total Marks:",total_marks)
print("Average Marks:",average_marks)
print("Grade:",grade)

   


import sqlite3

#for the prompt 'Enter the number of Semesters', always input 1. 

conn = sqlite3.connect('storage.db')

conn.execute('DELETE FROM DATABASE')

def addnamesandscores(students, name, score, total, subject, numberOfSemester, semester, numberOfSubjects, particulars, achievements, attendance):
  for i in range(total):
    if i < total:
      name = input('Enter the students fullname: ')
      particulars = input('Enter the students particulars: ')
      achievements = input('Enter the students achivements: ')
      attendance = input('Is the student present or absent?: ')
      students[name] = {}
    for j in range(numberOfSemester):
      if j < numberOfSemester:
        students[name]['Particulars'] = particulars
        students[name]['Achievements'] = achievements
        while (attendance.lower().strip() not in ['present', 'absent']):
          print ('Type present or absent')
          attendance = input('Is the student present or absent?: ')
        else:
          students[name]['Attendance'] = attendance
        semester = int(input('Current semester in numbers: '))
        students[name]['Semester' + str(semester)] = {}
      for k in range(numberOfSubjects):
        if k < numberOfSubjects:
          subject = input('Enter the full subject name: ')
          score = float(int(input('Enter the score in numbers: ')))
          students[name]['Semester' + str(semester)][subject.upper().strip()] = score

    conn.execute("INSERT INTO DATABASE (ID,SEMESTER,NAME,PARTICULARS,ACHIEVEMENTS,ATTENDANCE,PHYSICS,CHEMISTRY,MATH,ENGLISH,GEOGRAPHY,CHINESE) \
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?)", (i, semester, name, students[name]['Particulars'], students[name]['Achievements'] , students[name]['Attendance'], students[name]['Semester' + str(semester)]['PHYSICS'], students[name]['Semester' + str(semester)]['CHEMISTRY'], students[name]['Semester' + str(semester)]['MATH'], students[name]['Semester' + str(semester)]['ENGLISH'], students[name]['Semester' + str(semester)]['GEOGRAPHY'], students[name]['Semester' + str(semester)]['CHINESE']))

    conn.commit()

  cursor = conn.execute("SELECT id, semester, name, particulars, achievements, attendance, physics, chemistry, math, english, geography, chinese from DATABASE")
  for row in cursor:
    print ("ID = ", row[0])
    print ("SEMESTER = ", row[1])
    print ("NAME = ", row[2])
    print ("PARTICULARS = ", row[3])
    print ("ACHIEVEMENTS = ", row[4])
    print ("ATTENDANCE = ", row[5])
    print ("PHYSICS = ", row[6])
    print ("CHEMISTRY = ", row[7])
    print ("MATH = ", row[8])
    print ("ENGLISH = ", row[9])
    print ("GEOGRAPHY = ", row[10])
    print ("CHINESE = ", row[11], '\n')

       
  print (students)

  
  


students = {}
total = int(input('Enter the class size: '))
name = ''
subject = ''
score = 0
numberOfSemester = int(input('Enter the number of Semester in numbers: '))
particulars = ''
achievements = ''
attendance = ''
semester = 0
numberOfSubjects = int(input('Enter the number of subjects the student is taking in numbers: '))


addnamesandscores(students, name, score, total, subject, numberOfSemester, semester, numberOfSubjects, particulars, achievements, attendance)


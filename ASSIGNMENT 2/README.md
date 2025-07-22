# Grade Checker

The Program takes Score as input from user and output the grade received

Execution command:
```shell
python "1.grade-checker.py"
```

Enter the score to fetch the grade corresponding to it

Output:
```
Score: 80
B
```

# Student Grades

The program takes input for the action to be performed, which includes, listing of students, adding a new student's grade,
updating an existing student's grade or exit the code. The user needs to input the number for that corresponding action.

Execution command:
```shell
python "2.student-grades.py"
```

Enter the numbers as input to perform the corresponding action

Output:
```
  1. List all Students with their Grades
  2. Add a new Student and their grade
  3. Update an existing student's grade
  4. Exit
Please select a number between 1-4: 1

No students are added yet!

  1. List all Students with their Grades
  2. Add a new Student and their grade
  3. Update an existing student's grade
  4. Exit
Please select a number between 1-4: 2
Enter the name of the student: Student
Enter the grade for student Student: A
Successfully added the student Student with grade A
  1. List all Students with their Grades
  2. Add a new Student and their grade
  3. Update an existing student's grade
  4. Exit
Please select a number between 1-4: 3
Enter the name of the student: Tanh
Enter the grade for student Tanh: C
ERROR: No such user Tanh exists in the students list
  1. List all Students with their Grades
  2. Add a new Student and their grade
  3. Update an existing student's grade
  4. Exit
Please select a number between 1-4: 2
Enter the name of the student: Tanh
Enter the grade for student Tanh: C
Successfully added the student Tanh with grade C
  1. List all Students with their Grades
  2. Add a new Student and their grade
  3. Update an existing student's grade
  4. Exit
Please select a number between 1-4: 3
Enter the name of the student: Tanh
Enter the grade for student Tanh: A
Successfully update the grade of student Tanh with grade A
  1. List all Students with their Grades
  2. Add a new Student and their grade
  3. Update an existing student's grade
  4. Exit
Please select a number between 1-4: 1

Student: A
Tanh: A
  1. List all Students with their Grades
  2. Add a new Student and their grade
  3. Update an existing student's grade
  4. Exit
Please select a number between 1-4: 4
```

# Write to a File

The program writes some content to a sample.txt file

Execution command:
```shell
python "3.write-to-a-file.py"
```

# Read from a file

The program reads the content from the file sample.txt (the file needs to exist)

Execution command:
```shell
python "4.read-from-a-file.py"
```

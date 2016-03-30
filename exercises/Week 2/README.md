
# Week 2 Exercises
Write a program that enrolls student to different units as per the instructions below:
 - A student should be enrolled to a specific unit only once
 - Some of the units (core units) are mandatory to all students. Students should be enrolled to these units during registration (instantiation).
 - The rest of the units are optional. A student can be enrolled to these using a method `enroll_unit` which accepts the unit code
 - An error should be raised if a wrong unit code is entered

The units a student is enrolled to should be stored in a list which is empty during instantiation

### Program Structure:

The units should be stored in a dictionary in the following format:

```
units = {
    'UNIT001': {'unit_name': 'Unit 1', 'core': True},
    'UNIT002': {'unit_name': 'Unit 2', 'core': False},
    'CS001': {'unit_name': 'Introduction to Programming', 'core': False},
    etc
}

```

The Student class should have the following general structure:

```
class Student(object):
    """docstring for Student"""

    def __init__(self, fname, lname, student_id):
        """Initialize instance variables. """
        self.units = []

    def get_student_details(self):
        """Method should return the student details. """

    def enroll_unit(self, unit_code):
        """Method should assign units to the student and return a appropriate message. """

    def get_enrolled_units(self):
        """Method should return all units a student is taking"""

```

### Program Flow

Register a student

`new_student = Student('Eric', 'G', 'ST101-2016')`

Enroll a student to an existing unit

`new_student.enroll_unit('CS001') # Student successfully enrolled to CS001`

Enroll a student to a non-existent unit

`new_student.enroll_unit('UNIT010') # Unit not found`

Enroll a student to a core unit

`new_student.enroll_unit('UNIT001') # A core unit should only be added during instantiation`

Output student details

`new_student.get_student_details()`
```
Expected Output
    Reg No: ST101-2016
    Student Name: Eric G
```
Output units the student is enrolled to

`new_student.get_enrolled_units()`
```
Expected Output for each of the units:
    UnitCode: Unit Name
    e.g
    CS001: Introduction to Programming

```
Ensure your class and methods are well documented. Ref [PEP 0257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
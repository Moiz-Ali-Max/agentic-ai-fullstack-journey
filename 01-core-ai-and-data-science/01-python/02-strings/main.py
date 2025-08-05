full_name : str = "moiz ali afzaal"
print(type(full_name), full_name)

variabel1 : str = 'It\'s a python guide'
print(variabel1)

student_code : str = """
print("This is my code")
a = 10
b = 20
print(a + b)
"""
exec(student_code)

#Concatenation (string + string)cgpa and age in the moiz ali data.
#Type Casting b/c we concatenate 
name : str = "Moiz Ali Afzaal"
age : int = 23
education : str = "Bachelors in Artificial Intelligence"
cgpa : float = 3.43

data : str = "This is Moiz Ali Data:-\nStudent Name: " + name + "\nStudent Age: " + str(age)
print(data)

#Now, we do same thing with multi-line comments (''' '''' , """ """) and F-Strings. And also it solves our type casting problem.
name : str = "Moiz Ali Afzaal"
age : int = 23
education : str = "Bachelors in Artificial Intelligence"
cgpa : float = 3.43

data : str = f"""
This is the Bio Data of a Student:-
Student Name: {name}
Student Age: {age} 
Student Education: {education}
Student CGPA: {cgpa}
Tota {889 + 609 + 3.43}
"""

print(data)

#String Method
name : str = "moiZ AlI AFZaal"
print(name.capitalize())
print(name.lower())

#Adding Placeholder in a modern way
a = 10
b = 20
# {} - placeholder
# .format - method
m1 = "The value of a is {} and the value of b is {}".format(a, b)
print(m1)

#Now we adding data of student using format method
name : str = "Moiz Ali Afzaal"
age : int = 23
education : str = "Bachelors in Artificial Intelligence"
cgpa : float = 3.43

data : str = """
This is the Bio Data of a Student:-
Student Name: {0}
Student Age: {1}
Student Education: {3}
Student CGPA: {2}
""".format(name, age, cgpa, education)
print(data) #Here indexing matters that's why output is wrong. To solve put index no. in the placeholder

#Same as above but another way:
name : str = "Moiz Ali Afzaal"
age : int = 23
education : str = "Bachelors in Artificial Intelligence"
cgpa : float = 3.43

data : str = """
This is the Bio Data of a Student:-
Student Name: {a}
Student Age: {b}
Student Education: {c}
Student CGPA: {d}
""".format(a = name, b = age, d = cgpa, c = education)
print(data) 

#Methods and Attributes
name : str = "        moiz ALI   "
print(name.casefold())
print(name.lstrip()) #Remove extra spaces in left side
print(name.strip()) #Remove spaces on both sides

story_name : str = "tit for tat"
print(story_name.title())


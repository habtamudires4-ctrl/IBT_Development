# # . Dictionaries 
# • Create a dictionary student with keys: name, age, grade, city, department. 
# • Print the student’s name, department, and grade. 
# • Add a new key phone, with value ”0973057239” 
# • Update the grade.

student = {
    "name": "habtamu dires",
    "age": 28,
    "grade": "A",
    "city": "Addis Ababa",
    "department": "Computer Science"
}

print(student["name"])
print(student["department"])
print(student["grade"])

student["phone"] = "0973057239"
print(student["phone"])

student["grade"] = "A+"
print(student["grade"])
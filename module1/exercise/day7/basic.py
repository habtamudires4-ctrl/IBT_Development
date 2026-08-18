"""
Day 7 Exercises: Basic Data Structures & Big-O
"""

# ==========================================
# 1. Big-O Notation
# ==========================================
# Time complexities for common Python operations:
# - Accessing an element in a Python list by index: O(1) [Constant time direct memory lookup]
# - Searching for an element in a list using 'in': O(n) [Linear scan through elements]
# - Inserting at the beginning of a list: O(n) [Requires shifting all existing elements]
# - Dictionary lookup by key: O(1) average case [Hash map key indexing]


# ==========================================
# 2. Compare Complexities
# ==========================================
# Ranking from fastest to slowest for large inputs (n = 1,000,000):
# 1. O(1)      - Constant (Fastest)
# 2. O(log n)  - Logarithmic
# 3. O(n)      - Linear
# 4. O(n²)     - Quadratic (Slowest)


# ==========================================
# 3. Arrays / Lists
# ==========================================
# Create a list of 10 student names
students = [
    "Abebe", "Beto", "Chala", "Dawit", "Eleni",
    "Farah", "Girma", "Hana", "Ismail", "Jemila"
]

# Accessing by index -> O(1)
first_student = students[0]
print(f"First student: {first_student}")

# Adding at the end -> O(1) amortized
students.append("Kaleb")
print(f"After append: {students}")

# Inserting at position 0 -> O(n) due to index shifting
students.insert(0, "Zara")
print(f"After insert at start: {students}\n")


# ==========================================
# 4. Hashmaps (Dictionaries)
# ==========================================
student_grades = {
    "Abebe": 85,
    "Beto": 92,
    "Chala": 78,
    "Dawit": 90,
    "Eleni": 88
}

# Add a new student -> O(1)
student_grades["Farah"] = 95

# Update a grade -> O(1)
student_grades["Abebe"] = 90

# Check if a student exists (fast lookup using hash) -> O(1)
name_to_check = "Beto"
if name_to_check in student_grades:
    print(f"{name_to_check}'s grade: {student_grades[name_to_check]}")
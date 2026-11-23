#CLASSWORK on SETS AND TUPLE
# 1.
python_students = {"John", "James", "Victor", "Esther", "Mary", "Bell"}
print(python_students)

# 2.
my_set = {10, 20, 30, 10, 20, 40}
print(my_set)

# 3.
fruits = {"Apple", "Mango", "Orange", "Banana", "Pineapple"}
print(fruits)

#  4.
students = {}
print(students)

#  5.
colours = {"red", "orange", "yellow"}
colours.add("green")
print(colours)

#  6.
numbers = {10, 20, 30}
numbers.update([40, 50, 60])
print(numbers)

# 7.
java_students = {"John", "James", "Victor", "Esther", "Bell"}
java_students.remove("James")
print(java_students)

#  8.
juice = {"Apple", "Mango", "Orange"}
juice.discard("Pineapple")
print(juice)

#  9. 
Python_student = {"John", "Victor", "Mary", "David"}
Java_student = {"Mary", "David", "Peter", "James"}
total_student = Python_student.union(Java_student)
print(total_student)

#  10.
Python_student = {"John", "Victor", "Mary", "David"}
Java_student = {"Mary", "David", "Peter", "James"}
result = Python_student.intersection(Java_student)
print(result)

#  11.
Python_student = {"John", "Victor", "Mary", "David"}
Java_student = {"Mary", "David", "Peter", "James"}
result = Python_student.difference(Java_student)
print(result)

#   12.
Python_student = {"John", "Victor", "Mary", "David"}
Java_student = {"Mary", "David", "Peter", "James"}
result = Python_student.symmetric_difference(Java_student)
print(result)

#  13.
my_list = ["John", "Mary", "John", "Victor", "Mary", "David", "Victor"]
newlist = set(my_list)
print(newlist)

#  14.
Set_A = {10, 20, 30, 40}
Set_B = {30, 40, 50, 60}
new_data = Set_A.intersection(Set_B)
print(new_data)

#  15. 
teams = {"Arsenal", "Brighton", "Burnley", "Brentford", "Chelsea"}
print(teams)

teams.update(["Crystal_Palace", "Blackburn"])
print(teams)
#note that remove method only takes one item
teams.remove("Burnley")
print(teams)

# 16
five_students = ("Abe", "Bale", "Carol", "Dell", "Ella")
print(five_students)

#17
my_tuple = ("Ola", 20, "NIIT", "Nigeria")
print(my_tuple)

# 18
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])

# 19
my_fruits = ("Apple", "Berry", "Cherry", "Dates", "Mango")
print(my_fruits[2])

# 20
my_friends = ("John", "Mary", "Victor", "David")
print(my_friends[-1])

# 21
mytuple = (10, 20, 30, 40, 50, 60)
print(mytuple[1:5])

# 22
mytuple = (10, 20, 30, 40, 50, 60)
print(mytuple[:3])

#23
mytuple = (10, 20, 30, 40, 50, 60)
print(mytuple[2:])

#24
fruits = ("Apple", "Mango", "Orange")
refinedfruits = list(fruits)
print(refinedfruits)

# 25
fruits = ("Apple", "Mango", "Orange")
print(fruits)
temporaryfruits = list(fruits)

temporaryfruits[1] = "Banana"
fruits = tuple(temporaryfruits)
print(fruits)

# 26
numbers = (10, 20, 30, 40, 50, 60)
print(numbers)
mynumbers = list(numbers)
mynumbers[0] = 100
numbers = tuple(mynumbers)
print(numbers)

# 27
old_students = ("Abe", "Bale", "Carol", "Dell", "Ella")
newstudents = list(old_students)
print(newstudents)
newstudents.append("Fina")
print(newstudents)
old_students = tuple(newstudents)
print(old_students)

# 28
fruits = ("Apple", "Mango", "Apple", "Orange", "Apple")
print(fruits.count('Apple'))
print(fruits.index("Apple"))

# 29
friends = ("John", "Mary", "Victor", "David")
print(friends.index("Victor"))

# 30
student_info = ("John", 20, "Python", "Nigeria")
print(student_info[0])
print(student_info[1])
print(student_info[2])
print(student_info[3])

# Additional challenge
# sets and tuples have bracket types that differ
# sets usually have curly brackets while tuples are indicated by parenthesis(round brackets)
# sets dont support indexing (usually not sorted) while tuples are ordered
# set elements can be changed, added or removed (muted) in contrast to tuples which  are immutable
# sets dont allow duplicates

# sets are designed to store only unique elements

# the primary difference between remove() and discard() in sets is how they handle missing elements. remove() raises a KeyError if the specified element is not present in the set, whereas discard() does nothing and leaves the set unchanged if the element is missing. 

# Union combines all unique elements from two or more sets into a new set, while intersection returns only the elements that are common to all compared sets

# We convert a tuple into a list before modifying its elements because tuples are immutable, meaning their contents cannot be changed, added to, or removed after creation.⁠ Attempting to modify a tuple directly results in a TypeError
# By using the list() constructor, you create a mutable copy of the tuple's data. This allows you to perform modifications (such as appending, deleting, or changing values). If an immutable tuple is still required after the changes, the modified list will/should be converted back into a tuple using the tuple() constructor.
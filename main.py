def greet_student(name, age):
 return(f"Hello student. {name}, you are {age} years old.")

print(greet_student("Victor", 20))
print(greet_student("John", 25))


def welcome(name, country="Nigeria"):
 print(f"{name} is learning from {country}.")

welcome("Tunde")
welcome("Sarah", "Ghana")


def create_profile(username, role):
 return(f"User: {username} | Role: {role}")

print(create_profile(role="Instructor", username="Victor"))

def total_score(*scores):
 return sum(scores)

print(total_score(10, 20, 30, 40))


def greet_student(name):
    return (f"Hello {name}")

print (greet_student("Ola"))


def greet_student(name, age):
    return (f"Hello student. {name}, you are {age} years old")

print (greet_student("Ola", 20))


def welcome(name, country="Nigeria"):
 print(f"{name} is learning from {country}.")

welcome("Ola")
welcome("Sarah", "Ghana")



def create_profile(username, role):
 return(f"User: {username} | Role: {role}")

print(create_profile(role="Instructor", username="Victor"))


def total_score(*scores):
 return sum(scores)

print(total_score(10, 20, 30, 40))


def total_score(name, *scores):
 return(f"Hello student. {name}, you scored sum {scores} .")

print(greet_student("Victor", 10, 20, 30))


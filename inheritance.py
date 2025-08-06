class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"{self.name}, who teaches {self.subject}, is {self.age} years old."


class Student(Human):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f"{self.name}, with grade of {self.grade}, is {self.age} years old."


def main():
    choice = input(
        "Enter 'S' for student and 'T' for teacher: ").strip().upper()
    match choice:
        case "S":
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            grade = input("Enter your grade: ")
            student = Student(name, age, grade)
            print(student)
        case "T":
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            subject = input("Enter your subject: ")
            teacher = Teacher(name, age, subject)
            print(teacher)
        case _:
            print("You entered it wrong.")


if __name__ == "__main__":
    main()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name} is {self._age} years old.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 21 > int(age.strip()):
            raise ValueError("You are minor.")
        self._age = age

    @classmethod
    def get(cls):
        name = input("Enter student's name: ")
        age = input("Enter Student's age: ")
        return cls(name, age)


def main():
    student = Student.get()
    print(student)


if (__name__ == "__main__"):
    main()

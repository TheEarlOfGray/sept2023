class Student():
    def __init__(self, name, age, class_="General Studies"):
        self.name = name
        self.age = age
        self.class_ = class_

    def __repr__(self) -> str:
        return f"student name: {self.name}, Student age: {self.age}, Student class: {self.class_}."

    def gradeCalc(self, score1, score2, score3):
        return (score1 + score2 + score3) / 3


student1 = Student("Dave", 18)
student2 = Student("Tim", 19)

print(student2.gradeCalc(80, 87, 12))
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, fly, colouring) -> None:
        self.fly = fly
        self.colouring = colouring

    def __repr__(self) -> str:
        return f"This is the parent{self.fly}"

    @abstractmethod
    def extinct(self):
        pass


class Owl(Bird):
    def __init__(self, fly, colouring, head_rote) -> None:
        super().__init__(fly, colouring)
        self.head_rote = head_rote

    def __repr__(self) -> str:
        return f"This is different from the parent.{self.fly}"

    def extinct(self):
        pass

class Dodo(Bird):
    def __init__(self, fly, colouring, ext) -> None:
        super().__init__(fly, colouring)
        self.ext = ext

    def __repr__(self) -> str:
        return f"This is different from the parent.{self.fly}"

    def extinct(self):
        if self.ext:
            return True
        return False



dodo1 = Dodo(False, "Grey", False)


print((dodo1))







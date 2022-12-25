class a:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}_ {self.age}"

    def __getattribute__(self, item):
        if item == "name":
            return "you can not access name ! "
        elif item == "age":
            return "you can not access age !"
        else:
            return f"this is __getattribute__ method ! \"{item}\" does not exist !"


p1 = a("Sam", 44)
print(p1)

z = a("Sam", 44)
print(p1.lastName)

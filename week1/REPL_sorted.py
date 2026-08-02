# records = [
#     {"分类": "餐饮", "金额": "33.5"},
#     {"分类": "交通", "金额": "12.0"},
#     {"分类": "餐饮", "金额": "88.0"},
# ]
# print(sorted(records, key=lambda r: r["金额"]))

# print(sorted(records, key=lambda r: r["金额"], reverse=True))

# print(sorted(records, key=lambda r: (r["分类"], r["金额"])))

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} 说：汪")

    def birthday(self):
        self.age += 1
        return self.age

d1 = Dog("旺财", 3)
d2 = Dog("小黑", 5)

# d1.name
# d2.name
# d1.bark()
# d2.bark()
# d1.birthday()
# d1.age
# d2.age
print(type(Dog.birthday))
print(type(d1.birthday))
print(Dog.birthday(d1))
print(d1.birthday.__self__ is d1)
print(d1.birthday.__func__ is Dog.birthday)
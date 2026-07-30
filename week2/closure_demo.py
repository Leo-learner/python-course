def make_counter():
    count = 0
    def counter():
        nonlocal count
        count = count + 1
        return count
    return counter

c1 = make_counter()
c2 = make_counter()
print(c1())
print(c1())
print(c1())
print(c2())
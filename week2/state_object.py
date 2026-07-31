def make_counter(step=1):
    count = 0
    def counter():
        nonlocal count
        count += step
        return count
    def reset():
        nonlocal count
        count = 0
    return counter, reset
counter, reset = make_counter()
print(counter())
print(counter())
print(counter())
reset()
print(counter())
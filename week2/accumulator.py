def make_accumulator(start=0):
    total = start
    def inner(num):
        nonlocal total
        total += num
        return total
    return inner
acc1 = make_accumulator()
print(acc1(2))
print(acc1(3))
acc2 = make_accumulator(100)
print(acc2(2))
print(acc1(1))
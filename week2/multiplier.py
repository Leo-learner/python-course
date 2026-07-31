def make_multiplier(n):
    def inner(num):
        num *= n
        return num
    return inner
mul1=make_multiplier(2)
mul2=make_multiplier(3)
print(mul1(5))
print(mul1(6))
print(mul2(13))
print(mul2(2))
print(mul2(4))



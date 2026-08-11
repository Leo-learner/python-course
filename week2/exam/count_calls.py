import functools
def count_calls(label):
    def decorator(func):
        count = 0
        @functools.wraps(func)
        def inner(*args, **kwargs):
            nonlocal count
            count += 1
            print(f"[{label}] 第{count}次调用")
            result = func(*args, **kwargs)
            return result
        return inner
    return decorator

@count_calls("问候")
def greet(name):
    return f"你好，{name}"

@count_calls("加法")
def add(a, b):
    return a + b

print(greet("Leo"))
print(greet("张三"))
print(add(3, 4))

deco = count_calls("共享")

@deco
def f(): pass

@deco
def g(): pass

f(); f(); g()
print(greet.__name__)
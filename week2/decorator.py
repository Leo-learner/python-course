def add(a, b):
    return a + b
def call_and_report(func, *args, **kwargs):
    result = func(*args, **kwargs)
    print("调用了", func.__name__)
    print("传了", args, kwargs)
    print("返回了", result)
    return result
call_and_report(add, 3, 4)
call_and_report(print, "hi", "there", sep="-")
r = call_and_report(add, 3, 4)
print(r)          # 必须是 7
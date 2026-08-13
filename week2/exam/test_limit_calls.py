import functools
import pytest
class CallLimitExceeded(Exception):
    pass
def limit_calls(max_times):
    def decorator(func):
        count = 0
        @functools.wraps(func)
        def wrappers(*args, **kwargs):
            nonlocal count
            count += 1
            if count > max_times:
                raise CallLimitExceeded(f"{func.__name__}函数调用超出上限，上限为{max_times}，目前已调用{count}次")
            result = func(*args, **kwargs)
            return result
        return wrappers
    return decorator

@limit_calls(2)
def greet(name):
    return f"你好，{name}"

@limit_calls(3)
def add(a, b):
    return a + b

@limit_calls(2)
def good_bye(name):
    return f"再见，{name}"

def main():
    print(greet("Leo"))
    print(greet("张三"))
    print(add(3, 4))
    print(add(1, 1))
    print(greet("小明"))

    print(greet.__name__)

def test_exceed_call_limit():
    print(good_bye("Claude"))
    print(good_bye("Opus"))
    with pytest.raises(CallLimitExceeded):
        print(good_bye("Fable"))

if __name__ == "main":
    main()
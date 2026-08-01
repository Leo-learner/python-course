import time 
import functools
import random

def retry(times=1, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"捕获到{e}，第{attempt}次尝试")
                    if attempt == times:
                        raise 
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(times=3, delay=0.5)
def always_fail():
    raise ValueError("我就是会失败")

@retry(times=3, delay=0.5)
def flaky():
    # 用随机数模拟：大概率失败、小概率成功
    if random.random() < 0.2:
        print("成功！")
    else:
        raise ValueError("随机数测试失败")
    
@retry(times=3, delay=0.5)
def fine(a, b):
    return a + b

flaky()
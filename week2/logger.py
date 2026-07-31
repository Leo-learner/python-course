def make_logger(prefix):
    def inner(*args):
        print(f"[{prefix}]", *args)
    return inner

logger1 = make_logger('DEBUG')
logger2 = make_logger('INFO')
logger1(1, 2, 3)
logger2(1, 2)
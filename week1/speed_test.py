import time 
my_list = [i for i in range(1000001)]
my_set = set(my_list)

target = 0

start = time.perf_counter()
found_in_list = target in my_list
end = time.perf_counter()
list_time = end - start
print(f"Time taken to search in list: {list_time: .9f} seconds")

start = time.perf_counter()
found_in_set = target in my_set
end = time.perf_counter()
set_time = end - start
print(f"Time taken to search in set: {set_time: .9f} seconds")

print(f"{list_time / set_time: .9f}")

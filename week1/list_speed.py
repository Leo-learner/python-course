import time

start = time.perf_counter()
test_append = []
for i in range(100001): 
    test_append.append(i)
end = time.perf_counter()
print(f"Time taken to create list: {end - start: .9f} seconds")

start = time.perf_counter()
test_insert = []
for i in range(100001): 
    test_insert.insert(0, i)
end = time.perf_counter()
print(f"Time taken to create list with insert: {end - start: .9f} seconds")
from count_min_sketch import CountMinSketch

columns = 100
hash_functions_count = 5

count_min_sketch = CountMinSketch(column_size=columns, hash_functions=hash_functions_count)

# Adding 1 -> 1+3 times
count_min_sketch.add(1)
count_min_sketch.add_multiple_items(1, 3)

# Adding 2 -> 5 times
count_min_sketch.add_multiple_items(2, 5)

print("1's count:", count_min_sketch.estimate(1))
print("2's count:", count_min_sketch.estimate(2))

print("3's count:", count_min_sketch.estimate(3))
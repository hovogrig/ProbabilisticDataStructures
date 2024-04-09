from hll import HyperLogLog

numbers = range(100000)

hll = HyperLogLog(bits_for_bucket_index=16)

for num in numbers:
    hll.add(num)

print(hll.estimate())
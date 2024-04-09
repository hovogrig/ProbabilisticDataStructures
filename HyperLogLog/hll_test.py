from hll import HyperLogLog

hll = HyperLogLog(bits_for_bucket_index=16)

for num in range(100000):
    hll.add(num)

print("Cardinality estimate: " + str(hll.estimate_cardinality()))
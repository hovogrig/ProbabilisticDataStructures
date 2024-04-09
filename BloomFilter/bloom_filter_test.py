from bloom_filter import BloomFilter

bit_array_size = 10
hash_functions_count = 2

bloom_filter = BloomFilter(bit_array_size, hash_functions_count)

# Adding items to the Bloom Filter
bloom_filter.add("Apple")
bloom_filter.add("Banana")
bloom_filter.add("Grape")

# Checks whether Bloom Filter contains the items or not
print("The bloom filter contains 'Apple':", bloom_filter.contains("Apple"))
print("The bloom filter contains 'Pear':", bloom_filter.contains("Pear"))
# Bloom Filter

A Bloom filter is a probabilistic data structure used for testing whether an element is a member of a set or not.

## Algorithm Description

At first, we initialize a fixed-length array with 0's. When adding an element to the Bloom Filter, we calculate its different hashes and update the corresponding indexes with 1 in the array. Later, when checking whether an element is in the set or not, we repeat these steps: calculating hashes and verifying whether all indexes are 1 or not. If we find at least one position where it is 0, the element is considered not present.

## Note

There could be False Positive cases, where the algorithm incorrectly indicates that an element is present when it is not. This issue can be minimized by adjusting the values of the array size and the number of hash functions.

## Usage

The `BloomFilter` class takes 2 arguments:

- `size`: The size of the Bloom Filter (number of bits).
- `hash_functions_count`: The number of hash functions to use.

It has the following methods:
- `add(element)`: Adds an element to the Bloom Filter.
- `contains(element)`: Checks whether an element is in the set or not.

## References

- [Towards Data Science - Probabilistic Data Structures Decoded: Enhancing Performance in Modern Computing](https://towardsdatascience.com/probabilistic-data-structures-decoded-enhancing-performance-in-modern-computing-17f700e6ea47)

# Probabilistic Data Structures

Probabilistic data structures are efficient data structures that use randomness to provide approximate answers to queries with high probability. They are widely used in big data analytics, networking, and databases to handle large datasets efficiently.

## Bloom Filter

A Bloom Filter is a space-efficient probabilistic data structure used to test whether an element is a member of a set. It provides fast membership queries with a controlled probability of false positives.

### Usage

Bloom Filters are useful in scenarios where you need to check membership in a large set quickly. They are commonly used in caching systems, spell checkers, and network packet filtering.

### Resources

- [Bloom Filter on Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter)

## Count-Min Sketch

A Count-Min Sketch is a probabilistic data structure used to estimate the frequency of elements in a stream of data. It uses hash functions to map elements to different counters, providing approximate frequency counts.

### Usage

Count-Min Sketches are handy for tracking frequency counts in data streams, particularly in scenarios like traffic monitoring, clickstream analysis, and network traffic analysis.

### Resources

- [Count-Min Sketch on Wikipedia](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch)

## HyperLogLog

HyperLogLog is a probabilistic data structure used for approximating the cardinality (the number of distinct elements) of large data sets. It achieves high accuracy with low memory usage.

### Usage

HyperLogLog is valuable in scenarios where you need to estimate the cardinality of massive data sets efficiently. It's commonly used in web analytics, database systems, and distributed systems.

### Resources

- [HyperLogLog on Wikipedia](https://en.wikipedia.org/wiki/HyperLogLog)

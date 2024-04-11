# HyperLogLog

HyperLogLog is a probabilistic data structure used for approximating the cardinality (the number of distinct elements) of large data sets.

## Algorithm Description

First, calculate the hash of each item in the set to be analyzed, obtaining a binary number. This value is then decomposed into two parts: the first "b" bits determine which bucket of the estimator this number falls into out of the N = 2^b available ones, and the rest of the bits count the amount of leading zeros to estimate the probability of this number occurring. Each estimator bucket M_j, 0 ≤ j < 2^b, stores the maximum amount of leading zeros found for all the values associated with that bucket. After processing all the items this way, calculate the harmonic mean of the value 2^M_j for all the buckets. This mean value will be multiplied by a constant "alpha" and the number of buckets; the obtained result is the raw HyperLogLog estimate. Then perform bias correction to refine the estimate.

## Note

The Standard Error (SE) of the algorithm is defined as: SE = 1.04 / sqrt(N), with 2 ^ p = N, where p is considered as a parameter of HLL specifying the desired accuracy.


## Usage

The `HyperLogLog` class takes one argument:

- `bits_for_bucket_index`: The number of buckets = 2^bits_for_bucket_index.

It has the following methods:
- `add(element)`: Adds an element to the HyperLogLog.
- `estimate_cardinality()`: Estimates the cardinality (number of distinct elements) in the HyperLogLog data structure.

## References

- [HyperLogLog whitepaper](https://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf)
- [Towards Data Science - HyperLogLog: A Simple but Powerful Algorithm for Data Scientists](https://towardsdatascience.com/hyperloglog-a-simple-but-powerful-algorithm-for-data-scientists-aed50fe47869)

# Count Min Sketch

A Count-Min Sketch is a probabilistic data structure used to estimate the frequency of elements in a stream of data.

## Algorithm Description

Initially, we initialize a fixed-length matrix of size (hash_function_count x columns) with 0's. When adding an element, we calculate its different hashes and increment the value of the corresponding indexes in the matrix. Later, when estimating an element's frequency, we repeat these steps: calculating hashes and taking the minimum value of corresponding values.

## Usage

The `CountMinSketch` class takes 2 arguments:

- `column_size`: The number of columns in the sketch.
- `hash_functions`: The number of hash functions to use. This is also the number of rows in the sketch.

It has the following methods:
- `add(element)`: Adds an element to the Count Min Sketch.
- `add_multiple_items(element, count)`: Adds `count` occurrences of an item to the Count-Min Sketch.
- `estimate(element)`: Estimates the frequency of an item in the Count-Min Sketch.

## References

- [Towards Data Science - Probabilistic Data Structures Decoded: Enhancing Performance in Modern Computing](https://towardsdatascience.com/probabilistic-data-structures-decoded-enhancing-performance-in-modern-computing-17f700e6ea47)

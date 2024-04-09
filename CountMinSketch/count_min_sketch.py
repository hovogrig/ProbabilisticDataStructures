import hashlib

class CountMinSketch:
    def __init__(self, column_size, hash_functions):
        """
        Initializes a Count-Min Sketch.

        Parameters:
            column_size (int): The number of columns in the sketch.
            hash_functions (int): The number of hash functions to use.
        """
        self.matrix = [[0] * column_size for _ in range(hash_functions)]  # 2D array representing the Count-Min Sketch
        self.columns = column_size
        self.hash_functions = hash_functions


    def add(self, item):
        """
        Adds an item to the Count-Min Sketch.

        Parameters:
            item: The item to add.
        """
        self.add_multiple_items(item, 1)


    def add_multiple_items(self, item, count):
        """
        Adds multiple occurrences of an item to the Count-Min Sketch.

        Parameters:
            item: The item to add.
            count (int): The number of occurrences of the item.
        """
        indexes = self._get_hashed_indexes(item)
        for i in range(self.hash_functions):
            self.matrix[i][indexes[i]] += count


    def estimate(self, item):
        """
        Estimates the frequency of an item in the Count-Min Sketch.

        Note: The Count-Min Sketch may produce approximate results due to hash collisions
        and limited space, leading to potential overestimation.

        Parameters:
            item: The item to estimate the frequency for.

        Returns:
            int: An estimate of the frequency of the item.
        """
        indexes = self._get_hashed_indexes(item)
        minimum = self.matrix[0][indexes[0]]
        for i in range(1, len(indexes)):
            tmp = self.matrix[i][indexes[i]]
            if tmp < minimum:
                minimum = tmp
        return minimum
    

    def _get_hashed_indexes(self, item):
        """
        Generates hashed indexes for the given item.

        Parameters:
            item: The item to hash.

        Returns:
            list: A list of hashed indexes.
        """
        indexes = []
        for i in range(self.hash_functions):
            # Use SHA256 hash function to generate the index
            text_to_be_hashed = (str(item) + str(i)).encode('utf-8')
            index = int(hashlib.sha256(text_to_be_hashed).hexdigest(), 16) % self.columns
            indexes.append(index)
        return indexes

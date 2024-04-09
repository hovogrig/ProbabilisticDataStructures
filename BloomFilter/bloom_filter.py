import hashlib

class BloomFilter:
    def __init__(self, size, hash_functions_count):
        """
        Initializes a Bloom Filter.

        Parameters:
            size (int): The size of the Bloom Filter (number of bits).
            hash_functions_count (int): The number of hash functions to use.
        """
        self.array = [0] * size  # Initialize the bit array
        self.size = size  # Store the size of the array
        self.hash_functions_count = hash_functions_count  # Store the number of hash functions


    def add(self, item):
        """
        Adds an item to the Bloom Filter.

        Parameters:
            item: The item to add.
        """
        indexes = self.__get_hashed_indexes(item)
        for i in range(self.hash_functions_count):
            self.array[indexes[i]] = 1  # Set the corresponding bits to 1


    def contains(self, item):
        """
        Checks if the Bloom Filter possibly contains an item.

        Note: The Bloom Filter might produce false positives (indicating the item might be in the set),
        but never false negatives (if it returns false, the item is definitely not in the set).

        Parameters:
            item: The item to check for.

        Returns:
            bool: True if the item is possibly in the Bloom Filter, False otherwise.
        """
        indexes = self.__get_hashed_indexes(item)
        for i in range(self.hash_functions_count):
            if self.array[indexes[i]] == 0:
                return False  # If any bit is 0, the item is definitely not in the set
        return True  # Otherwise, the item might be in the set


    def __get_hashed_indexes(self, item):
        """
        Generates hashed indexes for the given item.

        Parameters:
            item: The item to hash.

        Returns:
            list: A list of hashed indexes.
        """
        indexes = []
        for i in range(self.hash_functions_count):
            # Use SHA256 hash function to generate the index
            text_to_be_hashed = (str(item) + str(i)).encode('utf-8')
            index = int(hashlib.sha256(text_to_be_hashed).hexdigest(), 16) % self.size
            indexes.append(index)
        return indexes

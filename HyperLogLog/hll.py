import hashlib
from math import log


class HyperLogLog:
    def __init__(self, bits_for_bucket_index):
        self.bits_for_bucket_index = bits_for_bucket_index
        self.buckets_count = 1 << self.bits_for_bucket_index
        self.buckets = [0] * self.buckets_count
        self.alpha = 0.7213 / (1 + 1.079 / self.buckets_count)


    def add(self, item): 
        hash_int = self.__hash(item)
        index = hash_int & (self.buckets_count - 1)
        reminder = hash_int >> self.bits_for_bucket_index
        self.buckets[index] = max(self.buckets[index], self.__rightmost_binary_1_position(reminder))


    def estimate(self):
        buckets_harmonic_mean = self.buckets_count / sum(2 ** (-register) for register in self.buckets)
        estimate = self.alpha * self.buckets_count * buckets_harmonic_mean
        return self.__apply_bias_correction(estimate)


    def __hash(self, item):
        item = str(item).encode('utf-8')
        hash = hashlib.sha256(item)
        hex_ = hash.hexdigest()
        return int(hex_, base=16)


    def __rightmost_binary_1_position(self, num):
        """The (number of trailing zeroes in the binary representation of num) + 1"""
        i = 0
        while (num >> i) & 1 == 0:
            i += 1
        return i + 1

    def __apply_bias_correction(self, E):
        # Small-range correction
        if E < (5 / 2.0 * self.buckets_count):
            V = len([b for b in self.buckets if b == 0])
            if V:
                E = self.buckets_count * log(self.buckets_count / float(V))
        # Large-range correction
        elif E > (1 / 30.0) * 2 ** 32:
            E = -(2 ** 32) * log(1 - (E / 2 ** 32))
        return E

import pickle
import random


class BloomFilter:
    def __init__(self, n):
        m = n * 10
        self.vec = [0] * m
        self.functions = BloomFilter.make_functions(7, m)

    def fit(self, items):
        for i in items:
            self.put(i)

    def put(self, item):
        item = item.lower()
        for f in self.functions:
            self.vec[BloomFilter.hash(item, f)] = 1

    def contains(self, item):
        item = item.lower()
        for f in self.functions:
            if self.vec[BloomFilter.hash(item, f)] == 0:
                return False
        return True

    def save(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(file_name):
        with open(file_name, 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def hash(item, f):
        a, p, m = f
        res = 0
        for i, s in enumerate(item):
            res += ord(s) * a ** i

        return (res % p) % m
        #return res % m

    @staticmethod
    def make_functions(k, m):
        #ps = [29, 31, 37, 41, 43, 47, 53]
        ps = [20112473, 20969239, 20800553, 20804731]
        random.seed()

        functions = []
        for i in range(k):
            p = ps[i % 4]
            a = random.randint(1, 37)
            functions.append((a, p, m))

        return functions

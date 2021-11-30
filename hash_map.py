import unittest
import math

"""insert hash map stuff here I guess..."""

class HashTable():

    innerDictionaryForHashTable = dict()

    def __init__(self, size):
        self.size = size

    def insert(self,key):

        for index in range(self.size):
            hashedPosition = self.hashKey(key,index)
            if self.innerDictionaryForHashTable[hashedPosition] == None:
                self.innerDictionaryForHashTable[hashedPosition] = key
                return None

    def search(self, key):
        for index in range(self.size):
            hashedPosition = self.hashKey(key,index)
            if self.innerDictionaryForHashTable[hashedPosition] == key:
                return hashedPosition
            if self.innerDictionaryForHashTable[hashedPosition] == None:
                return None

    def hashKey(self, key, index):
        def auxiliaryHash():
            hashingNumber = (math.sqrt(5)-1)/2
            return math.floor(self.size * (key * hashingNumber) % 1)

        return (auxiliaryHash() + index) % self.size



class TestClass(unittest.TestCase):
    """insert tests here"""
    pass


def main():

    unittest.main()


if __name__ == '__main__':
    main()

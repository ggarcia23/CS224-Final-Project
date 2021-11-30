import unittest
import math

"""insert hash map stuff here I guess..."""

class HashTable():


    def __init__(self, size):
        self.size = size
        self.innerList = [None for x in range(size)]


    def insert(self,key):

        for index in range(self.size):
            hashedPosition = self.hashKey(key,index)
            if not self.innerList[hashedPosition]:
                self.innerList[hashedPosition] = key
                return None

    def search(self, key):
        for index in range(self.size):
            hashedPosition = self.hashKey(key,index)
            if self.innerList[hashedPosition] == key:
                return hashedPosition
            if self.innerList[hashedPosition] == None:
                return None

    def hashKey(self, key, index):
        def auxiliaryHash():
            hashingNumber = (math.sqrt(5)-1)/2
            return math.floor(self.size * ((key * hashingNumber) % 1))
        return (auxiliaryHash() + index) % self.size



class TestClass(unittest.TestCase):
    """insert tests here"""
    def test_insert_and_search_key_of_table_of_size_127(self):
        testTable = HashTable(127)
        testTable.insert(31313)
        result = testTable.search(31313)
        self.assertEqual(63,result)


def main():

    unittest.main()


if __name__ == '__main__':
    main()

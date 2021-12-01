import unittest
import math

"""insert hash map stuff here I guess..."""

class HashTable():

    size = 127

    def __init__(self):
        self.innerList = [None for x in range(self.size)]

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
        testTable = HashTable()
        testTable.insert(31313)
        result = testTable.search(31313)
        self.assertEqual(63,result)

    def test_char_in_hashTable(self):
        testTable = HashTable()
        testTable.insert(ord('C'))
        result = testTable.search(ord('C'))
        self.assertEqual(51,result)

    def test_insert_and_search_with_multiple_values_inserted(self):
        testTable = HashTable()
        testTable.insert(48923432)
        testTable.insert(2324353543)
        testTable.insert(1233434556547674)
        testTable.insert(23546566575476)
        testTable.insert(65346456356436543636)
        testTable.insert(31313)
        result = testTable.search(31313)
        self.assertEqual(63, result)




def main():

    unittest.main()


if __name__ == '__main__':
    main()

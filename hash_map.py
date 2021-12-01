""" A hash map that handles collisions with open addressing
    moduleauthor:: Wendall Roberts and Gerardo Garcia
"""

import unittest
import math


class HashTable():
    """
    size is the size of the hash table, being 127
    """
    size = 127

    def __init__(self):
        """
        :
        """
        self.innerList = [None for x in range(self.size)]

    def insert(self, key):
        """ Inserts a key given by the parameter and hashes it into in proper hashed position in the hash table of size 127

        :param key: element containing the key to be hashed
        :type key: int
        :return: None
        """
        for index in range(self.size):
            hashedPosition = self.hashKey(key, index)
            if not self.innerList[hashedPosition]:
                self.innerList[hashedPosition] = key
                return None

    def search(self, key):
        """ Will search for the specified key in the hash table returning they keys position if found, returning None
            if key is not found in hash table

        :param key: int value of key to searched in hash table
        :type key: int
        :return: the hashed position of the searched key
        :rtype: int
        """
        for index in range(self.size):
            hashedPosition = self.hashKey(key, index)
            if self.innerList[hashedPosition] == key:
                return hashedPosition
            if self.innerList[hashedPosition] == None:
                return None

    def delete(self, key):
        """ will search for key, and delete it from the hash table, freeing its position from the hash table

        """
        pass

    def hashKey(self, key, index):
        """ finds the hashing position of the desired key by calling an inner function and modding it by the size of
            the hash table, returning the hashed position of the key

        :param key: value of key to be hashed
        :param index: index of the table
        :type key: int
        :type index: int
        :return: the hashed position of the key
        :rtype: int
        """

        def auxiliaryHash():
            """

            :return: the floor of the result given by the hashing number
            :rtype: int
            """
            hashingNumber = (math.sqrt(5) - 1) / 2
            return math.floor(self.size * ((key * hashingNumber) % 1))

        return (auxiliaryHash() + index) % self.size


class TestClass(unittest.TestCase):
    """ A testing class - will run automatically whenever the script is called

    """

    def test_insert_and_search_key_of_table_of_size_127(self):
        testTable = HashTable()
        testTable.insert(31313)
        result = testTable.search(31313)
        self.assertEqual(63, result)

    def test_insert_and_search_key_of_zero(self):
        testTable = HashTable()
        testTable.insert(0)
        result = testTable.search(0)
        self.assertEqual(0, result)

    def test_insert_two_numbers_and_search_key(self):
        testTable = HashTable()
        testTable.insert(23)
        testTable.insert(463)
        result = testTable.search(463)
        self.assertEqual(19, result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()

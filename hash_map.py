""" A hash map that handles collisions with open addressing
    moduleauthor:: Wendall Roberts and Gerardo Garcia
"""

import unittest
import math


class HashTable:
    """
    size is the size of the hash table, being 127
    """
    size = 127

    def __init__(self):
        """
        :
        """
        self.innerList = [None for _ in range(self.size)]

    def insert(self, key):
        """ Inserts a key given by the parameter and hashes it into in proper
        hashed position in the hash table of size 127

        :param key: element containing the key to be hashed
        :type key: int
        :return: None
        """
        for index in range(self.size):
            hashed_position = self.hash_key(key, index)
            if not self.innerList[hashed_position] or self.innerList[hashed_position] == "DELETED":
                self.innerList[hashed_position] = key
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
            hashed_position = self.hash_key(key, index)
            if self.innerList[hashed_position] == key:
                return hashed_position
            if self.innerList[hashed_position] is None:
                return None

    def delete(self, key):
        """ will search for key, and delete it from the hash table, freeing its position from the hash table

        """
        key_to_be_deleted = self.search(key)
        self.innerList[key_to_be_deleted] = "DELETED"

    def hash_key(self, key, index):
        """ finds the hashing position of the desired key by calling an inner function and modding it by the size of
            the hash table, returning the hashed position of the key

        :param key: value of key to be hashed
        :param index: index of the table
        :type key: int
        :type index: int
        :return: the hashed position of the key
        :rtype: int
        """

        def auxiliary_hash():
            """

            :return: the floor of the result given by the hashing number
            :rtype: int
            """
            hashing_number = (math.sqrt(5) - 1) / 2
            return math.floor(self.size * ((key * hashing_number) % 1))

        return (auxiliary_hash() + index) % self.size


class TestClass(unittest.TestCase):
    """ A testing class - will run automatically whenever the script is called

    """

    def test_insert_and_search_key_of_table_of_size_127(self):
        test_table = HashTable()
        test_table.insert(31313)
        result = test_table.search(31313)
        self.assertEqual(63, result)

    def test_insert_and_search_key_of_zero(self):
        test_table = HashTable()
        test_table.insert(0)
        result = test_table.search(0)
        self.assertEqual(0, result)

    def test_insert_two_numbers_and_search_key(self):
        test_table = HashTable()
        test_table.insert(23)
        test_table.insert(463)
        result = test_table.search(463)
        self.assertEqual(19, result)

    def test_char_in_hashTable(self):
        test_table = HashTable()
        test_table.insert(ord('C'))
        result = test_table.search(ord('C'))
        self.assertEqual(51, result)

    def test_insert_and_search_with_multiple_values_inserted(self):
        test_table = HashTable()
        test_table.insert(48923432)
        test_table.insert(2324353543)
        test_table.insert(1233434556547674)
        test_table.insert(23546566575476)
        test_table.insert(65346456356436543636)
        test_table.insert(31313)
        result = test_table.search(31313)
        self.assertEqual(63, result)

    def test_search_and_delete(self):
        test_table = HashTable()
        test_table.insert(31313)
        test_table.delete(31313)
        test_table.insert(31313)
        result = test_table.search(31313)
        self.assertEqual(63, result)

    def test_delete(self):
        test_table = HashTable()
        test_table.insert(31313)
        test_table.delete(31313)
        result = test_table.search(31313)
        self.assertEqual(None, result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()

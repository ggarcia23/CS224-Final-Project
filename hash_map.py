""" A hash map implementation that hashes keys into their proper indexes, dealing with
    collisions through open-addressing
    module author:: Wendall Roberts and Gerardo Garcia
"""
import unittest
import math


class HashTable:
    """
    size is a variable storing the length of the hash table, being 127
    """
    size = 127

    def __init__(self):
        """
        Initializes a list of with a size of 127, indexes filled with "None"
        """
        self.innerDictionary = {x: None for x in range(self.size)}

    def insert(self, key):
        """ Takes the key given by parameter, and hashes the key
            into its proper slot in the hash map

        :param key: element containing the key to be hashed
        :type key: int
        :return: None
        """
        for index in range(self.size):
            hashed_position = self.hash_key(key, index)
            if not self.innerDictionary[hashed_position] or self.innerDictionary[hashed_position] == "DELETED":
                self.innerDictionary[hashed_position] = key
                return None

    def search(self, key):
        """ Searches for the specified key in the hash map, given by the parameter, and returns the key if found,
        if not found it will return None

        :param key: int value of key to searched in hash table
        :type key: int
        :return: the hashed position of the searched key
        :rtype: int
        """

        hashed_key = self.innerDictionary[key]
        if type(hashed_key) is not str:
            return self.innerDictionary[key]
        return None

    def delete(self, key):
        """ Searches for specified key, and deletes it from the hash map, freeing up its slot

        """
        def search_for_key():
            """ Searches for the specified key in the hash map, given by the parameter, and returns the key if found,
        if not found it will return None

        :return: the hashed position of the searched key
        :rtype: int
        """
            for index in range(self.size):
                hashed_position = self.hash_key(key, index)
                if self.innerDictionary[hashed_position] == key:
                    return hashed_position
                if self.innerDictionary[hashed_position] is None:
                    return None

        key_to_be_deleted = search_for_key()
        self.innerDictionary[key_to_be_deleted] = "DELETED"

    def hash_key(self, key, index):
        """ Finds the hashing position of the desired key by calling an inner function and modding it by the size of
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
        result = test_table.search(63)
        self.assertEqual(31313, result)

    def test_insert_and_search_key_of_zero(self):
        test_table = HashTable()
        test_table.insert(0)
        result = test_table.search(0)
        self.assertEqual(0, result)

    def test_insert_463(self):
        test_table = HashTable()
        test_table.insert(463)
        result = test_table.search(19)
        self.assertEqual(463, result)

    def test_char_in_hashTable(self):
        test_table = HashTable()
        test_table.insert(ord('C'))
        result = test_table.search(51)
        self.assertEqual(67, result)

    def test_search_and_delete(self):
        test_table = HashTable()
        test_table.insert(31313)
        test_table.delete(31313)
        test_table.insert(31313)
        result = test_table.search(63)
        self.assertEqual(31313, result)

    def test_delete(self):
        test_table = HashTable()
        test_table.insert(31313)
        test_table.delete(31313)
        result = test_table.search(63)
        self.assertEqual(None, result)

    def test_collision_at_key_seventy_nine(self):
        test_table = HashTable()
        test_table.insert(3894)
        test_table.insert(90)
        result = test_table.search(80)
        self.assertEqual(90, result)

    def test_deletion_followed_by_a_would_be_collision(self):
        test_table = HashTable()
        test_table.insert(3894)
        test_table.delete(3894)
        test_table.insert(90)
        result = test_table.search(79)
        self.assertEqual(90, result)

    def test_collisions_at_key_38(self):
        test_table = HashTable()
        test_table.insert(8301)
        test_table.insert(2612)
        result = test_table.search(39)
        self.assertEqual(2612, result)

    def test_multiple_collisions_at_key_37(self):
        test_table = HashTable()
        test_table.insert(4408)
        test_table.insert(3277)
        test_table.insert(8445)
        result = test_table.search(39)
        self.assertEqual(8445, result)

    def test_multiple_collisions_and_then_deletion(self):
        test_table = HashTable()
        test_table.insert(4408)
        test_table.insert(3277)
        test_table.insert(8445)
        test_table.delete(3277)
        result = test_table.search(39)
        self.assertEqual(8445, result)

    def test_multiple_collisions_at_key_37_and_38(self):
        test_table = HashTable()
        test_table.insert(4408)
        test_table.insert(8301)
        test_table.insert(3277)
        result = test_table.search(39)
        self.assertEqual(3277, result)

    def test_multiple_collisions_at_key_37_and_38_with_deletion(self):
        test_table = HashTable()
        test_table.insert(4408)
        test_table.insert(8301)
        test_table.delete(8301)
        test_table.insert(3277)
        result = test_table.search(38)
        self.assertEqual(3277, result)

    def test_when_empty(self):
        test_table = HashTable()
        result = test_table.search(12)
        self.assertEqual(None, result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()

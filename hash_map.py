""" A hash table implementation that hashes keys into their proper indexes, dealing with
    collisions through open-addressing
    module author:: Wendall Roberts and Gerardo Garcia
"""
import unittest
import math


class HashTable:
    """ Size is a int variable that stores the length of the hash table, being 127
    """
    size = 127

    def __init__(self):
        """ Initializes a hash table (dictionary) of size 127
        """
        self.innerDictionary = {x: None for x in range(self.size)}

    def insert(self, key):
        """ Takes the key given by parameter, and hashes the key
            into its proper slot in the hash map

        :param key: int value that stores the key to be inserted into the hash table
        :type key: int
        """
        if type(key) is not int:
            return "That is not a valid key"

        for index in range(self.size):
            hashed_position = self.hash_key(key, index)
            if not self.innerDictionary[hashed_position] or self.innerDictionary[hashed_position] == "DELETED":
                self.innerDictionary[hashed_position] = key
                break

    def search(self, key):
        """ Searches for the specified key given by the parameter, and returns the key if found in the hash table, if
        the key is not found, then it will return 'None'

        :param key: int value of the specified key that's to be searched in the hash table
        :type key: int
        :return: the key found in the hash table
        :rtype: int
        """

        if type(key) is not int:
            return "That is not a valid key"

        hashed_key = self.innerDictionary[key]
        if type(hashed_key) is not str:
            return self.innerDictionary[key]
        return None

    def delete(self, key):
        """ Searches for the specified key in the hash table, freeing up its position in the hash table by
        assigning it the value of 'DELETED', allowing its position to be hashed for future keys

        :param key: integer value that stores the key to be searched and deleted
        :type key: int
        """

        if type(key) is not int:
            return "That is not a valid key"

        def search_for_key():
            """ Searches for the specified key in the hash table, given by the parameter, and returns the keys hashed
            position if found. If the key is not found, then the it'll return 'None'

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
        """ Finds the hashed position of the specified key given by the parameter by calling the inner 'auxiliary_hash'
        function and adding the parameter given index to mod by the hash table size to find the keys hashed position

        :param key: value of key to be hashed
        :param index: current index of the hash table being used to hash the key into
        :type key: int
        :type index: int
        :return: the hashed position of the key in the hash table
        :rtype: int
        """

        def auxiliary_hash():
            """ Inner hash function that handles collisions using multiplication, returning a hashing number that's to
            be combined with the index to help find the hashing position of the key in the hash table

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

    def test_when_hash_table_is_empty(self):
        test_table = HashTable()
        result = test_table.search(12)
        self.assertEqual(None, result)

    def test_collision_and_deletion(self):
        test_table = HashTable()
        test_table.insert(4408)
        test_table.insert(3277)
        test_table.delete(3277)
        test_table.delete(4408)
        test_table.insert(8445)
        result = test_table.search(37)
        self.assertEqual(8445, result)

    def test_multiple_collisions_deletions_and_inserts(self):
        test_table = HashTable()
        test_table.insert(4408)
        test_table.insert(3277)
        test_table.insert(8445)
        test_table.delete(3277)
        test_table.insert(2612)
        test_table.delete(4408)
        result = test_table.search(38)
        self.assertEqual(2612, result)

    def test_multiple_multiple_insertions_and_deletions_at_key_69_71_72(self):
        test_table = HashTable()
        test_table.insert(8248)
        test_table.insert(8104)
        test_table.insert(6130)
        test_table.insert(1483)
        test_table.delete(6130)
        test_table.insert(7151)
        test_table.delete(1483)
        test_table.insert(8172)
        result_71 = test_table.search(71)
        result_72 = test_table.search(72)
        self.assertEqual(7151, result_71)
        self.assertEqual(8172, result_72)

    def test_insert_negative_key(self):
        test_table = HashTable()
        test_table.insert(-5340)
        result = test_table.search(88)
        self.assertEqual(-5340, result)

    def test_collisions_for_negative_keys_at_index_11(self):
        test_table = HashTable()
        test_table.insert(-6904)
        test_table.insert(-5629)
        test_table.insert(-8213)
        result = test_table.search(13)
        self.assertEqual(-8213, result)

    def test_multiple_collisions_at_index_37_with_negative_keys(self):
        test_table = HashTable()
        test_table.insert(-2590)
        test_table.insert(4408)
        test_table.insert(-7059)
        result = test_table.search(39)
        self.assertEqual(-7059, result)

    def test_insert_and_delete_negative_keys_at_index_11(self):
        test_table = HashTable()
        test_table.insert(-6904)
        test_table.insert(-5629)
        test_table.delete(-6904)
        test_table.insert(-8213)
        result = test_table.search(11)
        self.assertEqual(-8213, result)

    def test_insert_negative_number(self):
        test_table = HashTable()
        test_table.insert(-1)
        result = test_table.search(48)
        self.assertEqual(-1, result)

    def test_insert_not_int(self):
        test_table = HashTable()
        self.assertEqual( "That is not a valid key", test_table.insert("Test String"))

    def test_search_not_int(self):
        test_table = HashTable()
        self.assertEqual( "That is not a valid key", test_table.search("Test String"))

    def test_delete_not_int(self):
        test_table = HashTable()
        self.assertEqual( "That is not a valid key", test_table.delete("Test String"))

def main():
    unittest.main()


if __name__ == '__main__':
    main()

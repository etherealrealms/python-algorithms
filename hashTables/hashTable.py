import random

from algorithm.Algorithm import Algorithm


def generate_test_data(length=200):
    data = []
    random_int = range(0, 2**12)

    for i in (range(0, length)):
        key = random.choice(random_int)
        value = random.choice(['apple', 'banana', 'orange', 'apple', f'the number {i}'])
        data.append((key, value))

    return data


def default_hash_key_function(key, number_of_buckets, max_key_length=32):
    """Takes a key and returns a string value that represents the bucket identifier"""
    raw_string_key = str(key)
    string_key = raw_string_key[:min(max_key_length, len(raw_string_key))]
    the_hash = 0

    for character_index, character in enumerate(string_key):
        the_hash += ord(character) + character_index

    return the_hash % number_of_buckets


max_number_of_buckets = 10
default_test_data = generate_test_data()


class HashTable(Algorithm):
    def __init__(self, test_data=default_test_data, number_of_buckets=max_number_of_buckets, hash_key_function=default_hash_key_function):
        Algorithm.__init__(self)
        self._buckets = {}
        self._hash_key_function = hash_key_function
        self._number_of_buckets = number_of_buckets
        self._test_data = test_data[:]

    def find(self, key):
        hash_key = self._hash_key_function(key, self._number_of_buckets)
        records = self._buckets.get(hash_key)

        if records is None:
            return None

        for (index, record) in enumerate(records):
            self._number_of_executions += 1
            if key == record[0]:
                return index, record

        return None

    def add(self, key, value):
        hash_key = self._hash_key_function(key, self._number_of_buckets)
        key_value_tuple = self._buckets.get(hash_key)
        item_to_add = key, value
        self._number_of_executions += 1

        if key_value_tuple is None:
            self._buckets[hash_key] = [item_to_add]
        else:
            existing_records = self.find(key)

            if existing_records is None:
                self._buckets[hash_key].append(item_to_add)
            else:
                self._buckets[hash_key][existing_records[0]] = item_to_add

    def exec_test(self, iteration, test_datum):
        return self.add(test_datum[0], test_datum[1])

    def test(self):
        Algorithm.test(self)
        print(str(self))

    def __str__(self):
        string_rep = ''
        for (hash_key, records_in_bucket) in self._buckets.items():
            string_rep += f'\nBucket (Hash Key: {hash_key})\n'

            for (i, record) in enumerate(records_in_bucket):
                string_rep += f'\tRecord {i + 1}: {record}\n'

        return string_rep


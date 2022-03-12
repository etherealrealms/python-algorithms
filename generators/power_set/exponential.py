from algorithm.Algorithm import Algorithm


class PowerSetExponential(Algorithm):
    def __init__(self, test_data=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']):
        Algorithm.__init__(self)
        self._test_data = test_data[:]

    @staticmethod
    def get_str_binary_representation(n, number_of_digits):
        """"
        :param n: integer >= 0
        :param number_of_digits: integer >= 0
        :return: string of length number_of_digits that is a binary representation of n
        """
        result = ''

        while n > 0:
            result = str(n % 2) + result
            n //= 2

        result_length = len(result)

        if result_length > number_of_digits:
            raise ValueError(f'The length of n does not match the number of digits {number_of_digits} passed in')

        for index in range(number_of_digits - result_length):
            result = '0' + result

        return result

    @staticmethod
    def generate_powerset(ordered_list):
        """
            Runs in exponential time!
        """
        length_of_list = len(ordered_list)

        # Why 2**length_of_list? Because we want to move through all possible subsets of ordered_list and we can
        # do this using a binary representation to show this!
        # Sneaky huh? How does this work imagine that we are enumerating all possibilities of a 2**length_of_lis binary
        # string where 1 denotes an element at
        number_of_possible_subsets = 2**length_of_list

        print(f'\nThere are {number_of_possible_subsets} subsets for the list {ordered_list} of length {length_of_list}\n')

        for i in range(number_of_possible_subsets):
            binary_string = PowerSetExponential.get_str_binary_representation(i, length_of_list)
            subset = []

            # get the subset of ordered_list for iteration i where the string is 1 denotes the existence of the element
            # at that index
            for j in range(length_of_list):
                if binary_string[j] == '1':
                    subset.append(ordered_list[j])

            yield subset

    def test(self):
        test_list = self._test_data

        for test_count in range(len(test_list)):
            print(f"\n\nTest #{test_count}")
            for i, power_set_subset in enumerate(PowerSetExponential.generate_powerset(test_list[0:test_count + 1])):
                print(f'subset {i}: {power_set_subset}')




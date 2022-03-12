from algorithm.Algorithm import Algorithm

the_haystack = [x for x in range(5000000)]


class BinarySearch(Algorithm):
    def __init__(self, haystack=the_haystack):
        Algorithm.__init__(self)
        self._sorted_haystack = sorted(haystack)
        self._test_data = [0, 1, 454435, 43545436, 4356445, 5645, 345434]

    def search(self, needle):
        self._number_of_executions = 0
        item_found = None

        haystack_length = len(self._sorted_haystack)

        if needle is None or haystack_length == 0:
            return item_found

        low = 0
        size_of_list = haystack_length
        high = haystack_length

        if needle < self._sorted_haystack[0] or needle > self._sorted_haystack[-1]:
            return None

        if needle == self._sorted_haystack[0]:
            return 0, needle

        if needle == self._sorted_haystack[-1]:
            return haystack_length - 1, needle

        while low < high and size_of_list != 0:
            self._number_of_executions += 1

            size_of_list = ((high - low) // 2)

            haystack_value = self._sorted_haystack[low + size_of_list]

            if haystack_value < needle:
                low += size_of_list
            elif haystack_value > needle:
                high -= size_of_list
            else:
                item_found = haystack_value
                break

        return item_found

    def exec_test(self, iteration, test_datum):
        return self.search(test_datum)
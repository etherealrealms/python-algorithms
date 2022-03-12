from algorithm.Algorithm import Algorithm

test_data = list(range(1000, 0, -1))


class MergeSort(Algorithm):
    def __init__(self, list_to_sort=test_data):
        Algorithm.__init__(self)
        self._test_data = [list_to_sort[:]]

    def merge_rest_of_sub_list(self, the_target_list, the_source_list, start_index):
        for index in range(start_index, len(the_source_list)):
            self._number_of_executions += 1
            the_target_list.append(the_source_list[index])

    def merge_lists(self, left_list, right_list):
        results = []
        length_of_left_list = len(left_list)
        length_of_right_list = len(right_list)

        left_list_counter = 0
        right_list_counter = 0

        while left_list_counter < length_of_left_list and right_list_counter < length_of_right_list:
            self._number_of_executions += 1
            left_value = left_list[left_list_counter]
            right_value = right_list[right_list_counter]

            if left_value <= right_value:
                results.append(left_value)
                left_list_counter += 1
            else:
                results.append(right_value)
                right_list_counter += 1

        self.merge_rest_of_sub_list(results, left_list, left_list_counter)
        self.merge_rest_of_sub_list(results, right_list, right_list_counter)

        return results

    def sort(self, the_list):
        length_of_list = len(the_list)
        self._number_of_executions += 1

        if length_of_list <= 1:
            return the_list[:]
        else:
            middle_index_of_list = length_of_list // 2
            left_list = self.sort(the_list[:middle_index_of_list])
            right_list = self.sort(the_list[middle_index_of_list:])

        return self.merge_lists(left_list, right_list)

    def exec_test(self, iteration, test_datum):
        return self.sort(test_datum)

from algorithm.Algorithm import Algorithm

test_data = list(range(1000, 0, -1))


class SelectionSort(Algorithm):
    def __init__(self, list_to_sort=test_data):
        Algorithm.__init__(self)
        self._test_data = [list_to_sort[:]]

    def sort(self, the_list):
        copy_of_test_data = the_list[:]
        test_data_length = len(copy_of_test_data)

        for (i, datum_to_sort) in enumerate(the_list):
            start_comparison_index = i + 1
            self._number_of_executions += 1

            if start_comparison_index < test_data_length:
                for (j, comparison_datum) in enumerate(the_list[start_comparison_index:]):
                    self._number_of_executions += 1
                    current_comparison_index = j + start_comparison_index

                    if comparison_datum < datum_to_sort:
                        copy_of_test_data[i], copy_of_test_data[current_comparison_index] = (
                            copy_of_test_data[current_comparison_index], copy_of_test_data[i]
                        )

        return copy_of_test_data

    def exec_test(self, iteration, test_datum):
        return self.sort(test_datum)


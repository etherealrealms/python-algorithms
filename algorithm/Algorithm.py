class Algorithm(object):
    def __init__(self):
        self._number_of_executions = 0
        self._test_data = []

    def generate_test_data(self):
        for data in self._test_data:
            yield data

    def exec_test(self, iteration, test_datum):
        return 'Please override me!'

    def test(self):
        for (i, test_datum) in enumerate(self.generate_test_data()):
            self._number_of_executions = 0
            result = self.exec_test(i, test_datum)
            print(
                f'Test Result {i}\n{"-" * 20}\nTest Data: {test_datum}\nResult: {result}\nExecution Count: {self.get_number_of_executions()}\n\n'
            )

    def get_number_of_executions(self):
        return self._number_of_executions

from algorithm.Algorithm import Algorithm


class Fibonacci(Algorithm):

    number_cache = [0, 1]

    def __init__(self):
        Algorithm.__init__(self)
        self._test_data = [0, 1, 10, 120, 99]

    def get_fibonacci_number(self, n):
        used_cache = True

        for i in range(len(Fibonacci.number_cache), n+1):
            used_cache = False
            self._number_of_executions += 1
            Fibonacci.number_cache.append(Fibonacci.number_cache[i - 1] + Fibonacci.number_cache[i - 2])

        if used_cache:
            self._number_of_executions += 1

        return Fibonacci.number_cache[n]

    def exec_test(self, iteration, test_datum):
        return self.get_fibonacci_number(test_datum)
class Generator:
    @staticmethod
    def generate(s):
        print(' '.join([str(i ** 2) for i in range(s + 1)]))

    @staticmethod
    def generate_evens(s):
        print(', '.join(list(filter(lambda x: x != '', [str(i) if i % 2 == 0 else '' for i in range(s + 1)]))))

    @staticmethod
    def filter_range(s):
        print(', '.join(
            list(filter(lambda x: x != '', [str(i) if (i % 3 == 0 or i % 4 == 0) else '' for i in range(s + 1)]))))

    @staticmethod
    def yield_test(a, b):
        for i in range(a, b + 1):
            yield i * i
    @staticmethod
    def descending(n):
        print([i for i in range(n+1)][::-1])


genr = Generator
# input
genr.generate(5)
genr.generate_evens(20)
genr.filter_range(10)
for numbers in genr.yield_test(2, 10):
    print(numbers, end=' ')
print()
genr.descending(20)
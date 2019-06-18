
def fib(num):
    a, b = 0, 1;
    for _ in range(num):
        a, b = b, a+b;
        yield a;

class Fib (object):
    def __init__(self, num):
        self._num = num;
        self.a , self.b = 0, 1;
        self.idx = 0;

    def __iter__(self):
        return self;

    def __next__(self):
        if (self.idx < self._num):
            self.a, self.b = self.b, self.a+self.b;
            self.idx += 1;
            return self.a;
        raise StopIteration();

def main():
    fib(6);

if __name__ == '__main__':
    main();

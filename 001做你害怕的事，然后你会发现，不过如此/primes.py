#看了廖老师的python教程，每隔一段时间就写个求素数的程序

def numlist():
    n = 1
    while True:
        n += 2
        yield n

def primes(maxn):
    yield 2
    nl = numlist()
    num = next(nl)
    while num <= maxn:
        yield num
        nl = filter(lambda x, y = num: x % y > 0, nl)
        num = next(nl)

if __name__ == '__main__':
    print(list(primes(100)))

def binom(n, k):
    '''slowly calculate the binomial coefficient'''
    if n <= 0:
        return 1
    if n < 2 * k:
        k = n - k
    if k == 0:
        return 1

    return binom(n - 1, k) + binom(n - 1, k - 1)


print(binom(5, 3))
print(binom(10, 7))
print(binom(15, 11))
print(binom(20, 13))
# print(binom(25, 9))

for n in range(11):
    for k in range(n + 1):
        print(binom(n, k), end="\t")
    print()


def fibList(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fibList(10000000)

def fib(n):


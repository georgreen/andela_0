'''A that generates prime number in a range(0, n)'''

def primeNumber_generator(n):
    """
       n is a positive integer
       outpout -> alist of primes between 0-n
    """
    if(type(n) != int or n < 0): raise TypeError

    if(n < 2):
        return []
    if(n == 2):
        return [2]
    j = 3
    results = [2]
    while(j <= n):
        if([(j % x) == 0 for x in results].__contains__(True)):
            pass
        else:
            results.append(j)
        j = j + 1

    return results


print(primeNumber_generator(1000))

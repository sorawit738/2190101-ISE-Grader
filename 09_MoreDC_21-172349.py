def factor(N):
    result = []
    prime = 2
    while N > 1:
        expo = 0
        while N % prime == 0:
            expo += 1
            N /= prime
        result.append([prime, expo])
        prime += 1

    # remove primes with exponents of 0
    i = len(result) - 1
    while i >= 0:
        if result[i][1] == 0:
            result.pop(i)
        i -= 1

    return result

exec(input().strip())

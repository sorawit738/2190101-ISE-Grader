def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(N):
    prime = N + 1
    while not is_prime(prime):
        prime += 1
    return prime
    
def next_twin_prime(N):
    prime = next_prime(N)
    prime2 = next_prime(prime)
    while abs(prime - prime2) != 2:
        prime = next_prime(prime)
        prime2 = next_prime(prime2)
    s = '(' + str(prime) + ', ' + str(prime2) + ')'
    return s

exec(input().strip())
import math
def gcd(m, n):
    return math.gcd(m, n)

def is_feasible(m, n, d):
    if d > n and d > m:
        return False
    return d % gcd(m, n) == 0

if __name__ == "__main__":
    n = 3
    m = 5
    d = 4
    print(is_feasible(m, n, d))

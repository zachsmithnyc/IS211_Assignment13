def factorial(n):
    if n < 0:
        raise ValueError("Factorial doesn't exist for negative numbers.")
    elif n in [0,1]:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a,b):
        if a == 0:
            return b
        else:
            return gcd(b % a, a)

def compareTo(s1, s2):
    print(s1, s2)
    if len(s1) and len(s2) == 0:
            return 0
    elif len(s1) == 0:
            return -1
    elif len(s2) == 0:
            return 1

    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])




if __name__ == '__main__':
    #factorial test
    for i in range(10):
        print(f'factorial({i}) = {factorial(i)}')
    
    #fibonacci test
    print(f'fibonacci(10) = {fibonacci(10)}')
    print(f'fibonacci(12) = {fibonacci(12)}')

    #GCD test
    print(f'gcd(24, 56) = {gcd(24, 56)}')
    print(f"gcd(100, 45) = {gcd(100, 45)}")
    
    # compare strings test
    print(f"compareTo('Zach', 'Zachary') = {compareTo('Zach', 'Zachary')}")
    print(f"compareTo('Yankee', 'yank') = {compareTo('Yankee', 'yankee')}")
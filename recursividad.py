def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

import time

def palindromo(s):
        if len(s) <=1:
            return True

        if s[0] != s[-1]:
              return False
        return palindromo(s[1:-1])
print (palindromo("reconocer"))
 

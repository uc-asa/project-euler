"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def getPrimeFactor(n):
  if (n < 2):
    return n
  maxPrime = 2
  while (n % 2 == 0):
    n = n/2
  i = 3
  while i<= n:
    while n%i == 0:
      maxPrime = i
      n = n/i
    i +=2
  return maxPrime
a = getPrimeFactor(600851475143)
print(a);

#!/usr/bin/python3.4

"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def largestPrimeFactor(n):
   i = 2
   while i*i <= n:
      while n % i == 0:
         n = n / i
         print(n,' ',i)
      i = i + 1
   return n

print(largestPrimeFactor(12))
print(largestPrimeFactor(13195))
print(largestPrimeFactor(600851475143))

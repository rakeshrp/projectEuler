#!/usr/bin/python3.4

"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


# first solution
limit = 1000
sum = 0

for i in range(limit):
   if (not (i % 3)) or (not (i % 5)):
     sum += i

print(sum)

# second solution
sum = 0

for i in range(limit):
   if (i % 3) == 0:
      sum += i
   else:
      if (i % 5) == 0:
         sum += i

print(sum)

#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# random.choice
import string
import random


import string
import random

# 方法一
seeds = string.digits
random_str = []
for i in range(4):
    random_str.append(random.choice(seeds))
print("".join(random_str))

# 方法二
seeds = string.digits
random_str = random.choices(seeds, k=4)
print("".join(random_str))

# 方法三
seeds = string.digits
random_str = random.sample(seeds, k=4)
print("".join(random_str))


# 源码查看
# def sample(self, population, k):
#           """Chooses k unique random elements from a population sequence or set.
#
#           Returns a new list containing elements from the population while
#           leaving the original population unchanged.  The resulting list is
#           in selection order so that all sub-slices will also be valid random
#           samples.  This allows raffle winners (the sample) to be partitioned
#          into grand prize and second place winners (the subslices).
#
#          Members of the population need not be hashable or unique.  If the
#          population contains repeats, then each occurrence is a possible
#          selection in the sample.
#
#          To choose a sample in a range of integers, use range as an argument.
#          This is especially fast and space efficient for sampling from a
#          large population:   sample(range(10000000), 60)
#          """
#
#          # Sampling without replacement entails tracking either potential
#          # selections (the pool) in a list or previous selections in a set.
#
#          # When the number of selections is small compared to the
#          # population, then tracking selections is efficient, requiring
#          # only a small set and an occasional reselection.  For
#          # a larger number of selections, the pool tracking method is
#          # preferred since the list takes less space than the
#          # set and it doesn't suffer from frequent reselections.
#
#          if isinstance(population, _Set):
#              population = tuple(population)
#          if not isinstance(population, _Sequence):
#              raise TypeError("Population must be a sequence or set.  For dicts, use list(d).")
#          randbelow = self._randbelow
#          n = len(population)
#          if not 0 <= k <= n:
#              raise ValueError("Sample larger than population or is negative")
#          result = [None] * k
#          setsize = 21        # size of a small set minus size of an empty list
#          if k > 5:
#              setsize += 4 ** _ceil(_log(k * 3, 4)) # table size for big sets43         if n <= setsize:
#              # An n-length list is smaller than a k-length set
#              pool = list(population)
#              for i in range(k):         # invariant:  non-selected at [0,n-i)
#                  j = randbelow(n-i)
#                  result[i] = pool[j]
#                  pool[j] = pool[n-i-1]   # move non-selected item into vacancy
#          else:
#              selected = set()
#              selected_add = selected.add
#              for i in range(k):
#                  j = randbelow(n)
#                  while j in selected:
#                      j = randbelow(n)
#                  selected_add(j)
#                  result[i] = population[j]
#          return result
import sys


def multiple():
   for n in sys.stdin:
      n = int(n.strip())
      numbers = list(range(1, n + 1))
      non_multiple = [number if number % 3 == 0 else 0 for number in numbers]
#for number in numbers:
#   if number % 3 == 0:
#      non_multiple.append(number)
#   else:
#      non_multiple.append(0)
      print("Non-multiples of 3 replaced:", non_multiple)
multiple()

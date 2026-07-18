from re import findall
import sys
from string import ascii_lowercase

letter = list(ascii_lowercase)
letters = r'+|'.join(letter) + '+'

for line in sys.stdin:
   line = line.strip()
   match = findall(letters, line)
   squashed = [f'{len(m)}{m[0]}' for m in match]
   print(''.join(squashed))

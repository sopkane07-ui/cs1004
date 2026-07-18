import sys
from re import findall

for line in sys.stdin:
   line = line.strip()
   caps = r'[A-Z]+'
   sequence = findall(caps, line)
   print(max(sequence, key=len))

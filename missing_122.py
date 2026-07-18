# missing_122.py

"""
import sys

def main():
   line1 = sys.stdin.readline().strip()
   line2 = sys.stdin.readline().strip()

   M, N = map(int, line1.split())
   full = set(range(M, N + 1))
   i = 0
   seen = set()

   while i < len(line2):
      for length in range(1, len(str(N)) + 1):
         num = int(line2[i:i+length])
         if M <= num <= N:
            seen.add(num)
            i += length
            break
   print((full - seen).pop())
if __name__ == "__main__":
   main()
"""

# missing_122.py

import sys

def main():
   line1 = sys.stdin.readline().strip()
   line2 = sys.stdin.readline().strip()

   M, N = map(int, line1.split())

   for missing in range(M, N + 1):
                        # build full sequence excluding one number
      candidate = ''.join(str(i) for i in range(M, N + 1) if i != missing)

      if candidate == line2:
         print(missing)
         return


if __name__ == "__main__":
   main()

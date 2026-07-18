# if letter already in word remove duplicate, if len
import sys

for line in sys.stdin:
   words = {}
   count = 0
   line = line.strip()
   for char in line:
      if char not in words:
         words[char] = 1
      elif char in words:
         words[char] = words[char] + 1

   if len(words) > 2:
      freqs = sorted(words.values(), reverse=True)
      keep = freqs[0] + freqs[1]
      count = len(line) - keep
      print(count)

   else:
      count = 0
      print(count)
   #len - 2 = s
   #print(count)


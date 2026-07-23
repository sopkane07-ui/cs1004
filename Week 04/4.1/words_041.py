from string import punctuation
import sys
seen = {}
count = 0

for lines in sys.stdin:
   tokens = lines.lower().strip().split()
   for token in tokens:
      token = token.strip(punctuation)
      if token not in seen:
         seen[token] = 1
      else:
         seen[token] = seen[token] + 1
for words in sorted(seen):
   print(words +':',seen[words])

import sys

line = sys.stdin.readline().strip()
a, b = line.split()
#print(a)
#print(b)

for ch in a:
   if ch in b:
      same = ch
      break

col = a.index(same)
row = b.index(same)

for r in range(len(b)):
   word = ''
   for c in range(len(a)):
      if r == row:
         word += a[c]
      elif c == col:
         word += b[r]
      else:
         word += '.'
   print(word)







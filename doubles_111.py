import sys

lines = []
words = {}

for line in sys.stdin:
   lines.append(line.strip())

doubles = {}
for line in lines:
   words[line] = line.count('aa') + line.count('ee') + line.count('ii') + line.count('oo') + line.count('uu')
   doubles[line] = words[line]
max_num = (max(doubles.values()))
for n in doubles:
   if doubles[n] == max_num:
      print(n)

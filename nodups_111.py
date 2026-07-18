'''
import sys
from string import punctuation

dict = {}
for line in sys.stdin:
   l = ''
   for word in line.split():
      if word.lower().strip(punctuation) not in dict:
         dict[word.lower().strip(punctuation)] = '.'
         l = l + word + ' '
      else:
         if word.lower().endswith(',') or word.lower().endswith('.') or word.lower().endswith('!'):
            l = l + '.' + word[-1] + ' '
         else:
            l = l + (dict[word.strip(punctuation)]) + ' '
   print(l.strip()))
'''
import sys
from string import punctuation

seen = set()

for line in sys.stdin:
   output = []
   for word in line.split():
      clean = word.lower().strip(punctuation)

      if clean not in seen:
         seen.add(clean)
         output.append(word)
      else:
         if word[-1] in punctuation:
            output.append("." + word[-1])
         else:
            output.append(".")

   print(" ".join(output))

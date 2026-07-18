import sys

vowels = "aeiou"

for line in sys.stdin:
   line = line.strip()
   i = 0
   result = ""

   while i < len(line):
      result += line[i]

      if line[i] in vowels:
         i += 3
      else:
         i += 1

   print(result)

# 1. remove any vowel except for first and last
# replace multiple letters with only one letter
import sys
lines = sys.stdin.readlines()
vowels = ['a', 'e', 'i', 'o', 'u']
for line in lines:
   new = ''
   line = line.strip()
   words = line.split()
   for word in words:
      lower = word.lower()
      i = 0
      for i in range(len(lower) - 1):
         if lower[i] == lower[i + 1]:
            new += lower[i]
            i = i + 2
         else:
            new += lower[i]
            i = i + 1
print(new)
'''
    for word in words:
       for letter in range(1, len(word:
       lower_letter = letters.lower()
       if lower_letter not in vowels:
          new += letters
    print(new)
'''

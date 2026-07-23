# goes through each letter in each word. if vowels(dictionary) in word add one
import sys
from string import punctuation

vowels = {}

vowelz = 'aeiou'
for lines in sys.stdin:
   line = lines.lower().strip().split()
   for tokens in line:
      tokens = tokens.strip(punctuation)
      for letter in tokens:
         if letter in vowelz and letter not in vowels:
            vowels[letter] = 0
            #print(vowels)
         for vowel in vowels:
            if vowel in letter:
               vowels[letter] = vowels[letter] + 1

vowels = sorted(vowels.items(), key=lambda x: x[1], reverse=True)
#print(vowels)
#count = []
for char, count in vowels:
   m_count = len(str(vowels[0][1]))
   m_count = int(m_count)
   print(f"{char}: {count:>{m_count}}")
   #print(m_count)

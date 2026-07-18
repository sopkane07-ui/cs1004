import sys

"""
with open("dictionary05.txt") as low:
   low = low.readlines()
"""

low = sys.stdin.readlines()

def all_vowel(w):
   #vowel
   w = w.strip().lower()
   check = ('a' in w, 'e' in w, 'i' in w, 'o' in w, 'u' in w)
   return all(check)


def iary(w):
   if w.endswith("iary"):
      iary_words.append(w)

e_word = []
previous = 0

all_vowels = [word for word in low if all_vowel(word)]
all_vowels = sorted(all_vowels, key=len)


print("Shortest word containing all vowels:", all_vowels[0].strip())

iary_words = []
for char in low:
   char = char.strip().lower()
   count_e = char.strip().lower().count('e')
   if count_e > previous:
      previous = count_e
      e_word = [char]
   elif count_e == previous:
      previous = count_e
      e_word.append(char)
   iary(char)


print("Words ending in iary:", len(iary_words))
print("Words with most e's:", e_word)





"""
shortest = []
vowels = 'aeiou'

file = sys.argv[1]
with open(file) as words:
   words = words.readlines()
   for word in words:
      word = word.strip()
      wor = []
      for char in vowels:
         if char in word:
            wor.append(char)
      wor = ''.join(wor)
"""

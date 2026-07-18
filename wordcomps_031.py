import sys

#words = ['ganle', 'GanlE', 'angle', 'Galen', 'glean', 'Lange']
words = sys.stdin.readlines()

n = []
m = []
a = []
q = []
cie = []
angle = []

def seven(w):
   length = len(w)
   if length == 17:
      n.append(w)
   elif length >= 18:
      m.append(w)
   return n
   return m

def contains(w):
   if 'cie' in word:
      cie.append(word)
   return cie


def anagram(w):
   first = 'angle'
   check = w.lower()
   for char in check:
      if char in first:
         first = first.replace(char, '', 1)
         check = check.replace(char, '', 1)
   if len(first) == 0 and len(check) == 0 and w != 'angle':
      angle.append(w)

for word in words:
   word = word.strip()
   seven(word)
   contains(word)
   anagram(word)
   counta = 0
   countq = 0
   for char in word:
      char = char.lower()
      if char == 'a':
         counta = counta + 1
      elif char == 'q':
         countq = countq + 1
   if counta == 4:
      a.append(word)
   if countq >= 2:
      q.append(word)


print('Words containing 17 letters:', n)
print('Words containing 18+ letters:', m)
print("Words with 4 a's:", a)
print("Words with 2+ q's:", q)
print('Words containing cie:', cie)
print('Anagrams of angle:', angle)

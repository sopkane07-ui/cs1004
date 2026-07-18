import sys
"""
lines = sys.stdin.read()
candidates = list(range(1, 21))

i = 0
while i < len(lines):
   lines = lines.strip()
   guess = int(lines[i].strip())
   responce = lines[i + 1].strip()
   #print(guess)
   #print(candidates)
   if responce == 'higher':
      candidates = [c for c in candidates if c > guess]
   elif responce == 'lower':
      candidates = [c for c in candidates if c < guess]
   else:
      print('Bert can be trusted' if guess in candidates else 'Bert is not to be trusted')

   i = i + 2

"""
min_val = 1
max_val = 20

lines = [line.strip() for line in sys.stdin if line.strip()]

i = 0
while i < len(lines):
   guess = int(lines[i])
   result = lines[i + 1]
   i = i + 2

   if result == 'higher':
      min_val = max(min_val, guess + 1)

   elif result == 'lower':
      max_val = min(max_val, guess - 1)

   elif result == 'correct':
      if min_val <= guess <= max_val:
         print('Bert can be trusted')
      else: print('Bert is not to be trusted')

      min_val = 1
      max_val = 20


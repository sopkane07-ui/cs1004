import sys

lines = sys.stdin.readlines()
row_words = []
#column_words = []
for row in lines:
   row = row.strip()
   parts = row.split('.')
   for word in parts:
      word = word.strip()
      if len(word) >= 2:
         row_words.append(word)

columns_words = []
column_length = len(lines[0])
for column_id in range(column_length):
   word = ''
   for row in lines:
      word += row[column_id]
      #print('column', column_id, ':', word)
      #print(word)
   sp = word.split('.')
   #print(sp)
   for i in sp:
      i = i.strip()
      #print(i)
      if len(i) >= 2:
         columns_words.append(i)

final = set(columns_words + row_words)
final = sorted(final)
final = ', '.join(final)
print(final)
#result = ''

'''
for word in final:
   result += word
print(result)
'''


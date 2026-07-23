import sys

names = {}
for line in sys.stdin:
   line = line.strip().split(',')
   for people in line:
      if people not in names:
         names[people] = 1
      elif people in names:
         names[people] = names[people] + 1

#print(names)
#max_name = (max(names.values()))
#name_value = [name for name in names if names[name] == max_name]
#print(name_value)

new_name = ''
for name in names:
   if names[name] == 4 and len(new_name) == 0:
      new_name = new_name + name
   elif names[name] == 4 and len(new_name) > 0:
      new_name = new_name + ', ' + name

if len(new_name) >= 1:
   print(new_name)
else:
   print('Uh-oh')

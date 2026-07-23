def count(s):
   if s == '':
      return 0
   return 1 + count(s[1:])

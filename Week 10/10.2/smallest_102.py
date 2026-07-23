def smallest(s):
   if len(s) == 1:
      return s[0]
   small = smallest(s[1:])
   if s[0] < small:
      return s[0]
   else:
      return small

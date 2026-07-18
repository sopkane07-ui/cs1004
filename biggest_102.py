def biggest(s):
   if len(s) == 1:
      return s[0]
   big = biggest(s[1:])
   if s[0] > big:
      return s[0]
   else:
      return big

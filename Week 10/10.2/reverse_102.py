def reverse(l):
   if len(l) == 0:
      return l
   return [l[-1]] + reverse(l[:-1])


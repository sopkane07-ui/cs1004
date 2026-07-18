def double(n, index=0):
   if len(n) == 0:
      return n
   if index % 2 == 0:
      first = n[0] * 2
   else:
      first = n[0]
   return [first] + double(n[1:], index = index + 1)

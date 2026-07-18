def flatten(lst):
   if lst == []:
      return []

   first = lst[0]
   rest = lst[1:]

   if isinstance(first, list):
      return flatten(first) + flatten(rest)
   else:
      return [first] + flatten(rest)

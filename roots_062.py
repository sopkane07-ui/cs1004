import sys
def root(s):
   a, b, c = s
   a = int(a)
   b = int(b)
   c = int(c)
   if ((b ** 2) - (4 * a * c) >= 0):
      square_root = ((b ** 2) - (4 * a * c)) ** 0.5
      b = b * -1
      divide = 2 * a
      root1 = (b + square_root) / divide
      root2 = (b - square_root) / divide
      return root2, root1
   else:
      return None, None
for line in sys.stdin:
   line = line.strip().split()
   root1, root2 = root(line)
   if root1 and root2:
      root1 = round(root1, 1)
      root2 = round(root2, 1)
      print(f"{root1}, {root2}")
   else:
      print(None)

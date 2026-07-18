import sys

#line1 = 'panicked\n'
#line2 = 'unpanicked\n' #should not print
#line3 = 'PaNiCked\n'
#lines = [line1, line2, lin

for line in sys.stdin:
   line = line.strip()
   keep = ''
   for c in line.lower():
      if c in 'nice':
         keep = keep + c
   if keep == 'nice':
      print(line)

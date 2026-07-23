import sys

lines = sys.stdin.readlines()

for line in lines:
   correct = []
   line = line.strip().split()
   k = int(line[0])
   q = int(line[1])
   r = int(line[2])
   b = int(line[3])
   n = int(line[4])
   p = int(line[5])
   correct.append(str(2 - k))
   correct.append(str(2 - q))
   correct.append(str(4 - r))
   correct.append(str(4 - b))
   correct.append(str(4 - n))
   correct.append(str(16 - p))
   print(' '.join(correct))

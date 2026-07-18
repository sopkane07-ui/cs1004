import sys
M = sys.stdin.readline().strip()
M = int(M)
N = sys.stdin.readline().strip().split()
sorted_n = sorted(N)

trips = 1
weight = 0
i = 0
for i in range(len(sorted_n)):
   sorted_n[i] = int(sorted_n[i])
   if len(sorted_n) == 1 and sorted_n[i] == 0:
      trips = 0
   if (weight + sorted_n[i]) <= M:
      weight += sorted_n[i]
      #print(weight)
   elif (weight + sorted_n[i]) > M:
      weight = 0
      trips += 1
      weight += sorted_n[i]
      #print(weight)
   i += 1
print(trips)

import sys

temps = list(map(int, sys.stdin.read().split()))

best_day = 0
best_temp = float('inf')

for i in range(len(temps) - 2):
   current_max = max(temps[i], temps[i + 2])

   if current_max < best_temp:
      best_temp = current_max
      best_day = i

print(best_day + 1, best_temp)

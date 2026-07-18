import sys

best_runner = None
best_time = None  # in seconds

for line in sys.stdin:
   parts = line.strip().split()
   name = parts[0]
   times = parts[1:]
   valid = True
   runner_best = None
   for t in times:
   # Validate format
      if ":" not in t:
         valid = False
         break
      mins, secs = t.split(":", 1)
      if not (mins.isdigit() and secs.isdigit()):
         valid = False
         break

      mins = int(mins)
      secs = int(secs)

      if secs >= 60:
         valid = False
         break
      total_seconds = mins * 60 + secs
      if runner_best is None or total_seconds < runner_best:
         runner_best = total_seconds
      # Skip runner if invalid
   if not valid:
      continue
      # Compare to global best
   if best_time is None or runner_best < best_time:
      best_time = runner_best
      best_runner = name
    # Convert best time
mins = best_time // 60
secs = best_time % 60

print(f"{best_runner}: {mins}:{secs:02}")

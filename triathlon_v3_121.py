class Triathlete:
   def __init__(self, name, tid):
      self.name = name
      self.tid = tid
      self.times = {}
   def add_time(self, sport, time):
      self.times[sport] = time
   def get_time(self, it):
      return self.times.get(it, 0)
   def total_time(self):
      return sum(self.times.values())
   def __str__(self):
      total_seconds = self.total_time()
      minutes = total_seconds // 60
      seconds = total_seconds % 60
      return f'Name: {self.name}\nID: {self.tid}\nRace time: {minutes}:{seconds:02d}'
   def __eq__(self, other):
      return self.total_time() == other.total_time()
   def __gt__(self, other):
      return self.total_time() > other.total_time()
   def __lt__(self, other):
      return self.total_time() < other.total_time()

class Triathlon(object):
   def __init__(self):
      self.athletes = {}
   def add(self, triathlete):
      self.athletes[triathlete.tid] = triathlete
   def lookup(self, tid):
      return self.athletes.get(tid)
   def remove(self, tid):
      if tid in self.athletes:
         del self.athletes[tid]
   def __str__(self):
      sorted_athletes = sorted(self.athletes.values(), key=lambda t: t.name)
      result = [str(athlete) for athlete in sorted_athletes]
      return "\n".join(result)

   def best(self):
      if not self.athletes:
         return None
      return min(self.athletes.values(), key=lambda t: t.total_time())

   def worst(self):
      if not self.athletes:
         return None
      return max(self.athletes.values(), key=lambda t: t.total_time())

class Meeting(object):
   def __init__(self, hour, minute, duration):
      self.hour = hour
      self.minute = minute
      self.duration = duration
   def __str__(self):
      return f"{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)"

class Schedule(object):
   def __init__(self):
      self.d = {}
   def add(self, a):
      self.d[a.hour] = a
   def __str__(self):
      list = []
      list.append('Schedule')
      list.append('--------')
      sorted_list = sorted(self.d.keys())
      count = 0
      for word in sorted_list:
         list.append(str(self.d[word]))
         count += 1
      count = str(count)
      list.append(f'Meetings today: {count}')
      return '\n'.join(list)

















'''
class Schedule(object):
   def __init__(self):
      self.l = []

   def add(self, e):
      self.l.append(str(e))

   def __str__(self):
      lines = []
      sorted_lines = sorted(self.l)
      lines.append("Schedule")
      lines.append("--------")
      for line in sorted_lines:
         lines.append(line)
      lines.append("Meetings today: {}".format(len(self.l)))
      return "\n".join(lines)
'''


class Meeting(object):
   def __init__(self, hour, minute, duration):
      self.hour = hour
      self.minute = minute
      self.duration = duration
   def __str__(self):
      return f"0{self.hour}:0{self.minute} ({self.duration} minutes)"


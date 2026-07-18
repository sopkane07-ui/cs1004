class Lamp(object):
   def __init__(self, on=False, off=True):
      self.on = on
      self.off = off
   def turn_on(self):
      self.on = True
      self.off = False
   def turn_off(self):
      self.on = False
      self.off = True
   def toggle(self):
      if self.on == True:
         self.on = False
         self.off = True
      else:
         self.on = True
         self.off = False


class Vehicle(object):
   def __init__(self, reg, cat, mileage, drivers):
      self.reg = reg
      self.cat = cat
      self.mileage = mileage
      self.drivers = drivers
   def __str__(self):
      drivers_str = ", ".join(self.drivers)
      return f'Reg: {self.reg}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {drivers_str}'

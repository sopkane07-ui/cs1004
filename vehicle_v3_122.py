class Vehicle(object):
   def __init__(self, reg, cat, mileage, drivers=None):
      self.reg = reg
      self.cat = cat
      self.mileage = mileage
      self.drivers = [] if drivers is None else drivers

   def add_driver(self, drivers):
      self.drivers.append(drivers)

   def service_due(self):
      if self.mileage == 0:
         return "Service due in 10000 mile(s)"
      if self.mileage % 10000 == 0:
         return "Service due now"
      next_service = ((self.mileage // 10000) + 1) * 10000
      miles_left = next_service - self.mileage
      return f"Service due in {miles_left} mile(s)"

   def __str__(self):
      drivers_str = ", ".join(self.drivers)
      return f'Reg: {self.reg}\nCategory: {self.cat}\nMileage: {self.mileage}\nDrivers: {drivers_str}\n{self.service_due()}'

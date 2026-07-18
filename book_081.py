class Book(object):
   def set_attributes(self, title, author, pages):
      self.title = title
      self.author = author
      self.pages = pages
      self.status = 'available'

   def print_attributes(self):
      print(f"{self.author}. {self.title}. {self.pages} pp.")
      print(f"Currently {self.status}")
   def borrow_book(self):
      self.status = 'on loan'
   def return_book(self):
      self.status = 'available'

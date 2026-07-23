from string import punctuation
class Email(object):
   def __init__(self, eid, sender, subject, body, recipients=None):
      self.eid = eid
      self.sender = sender
      self.subject = subject
      self.body = body
      if recipients is None:
         self.recipients = []
      else:
         self.recipients = recipients
   def add_recipient(self, email):
      self.recipients.append(email)
   def spam_score(self):
      #percentage of upper case letters
      # if not a whole number sount it to the nearest int
      #8/10
      upper_cases = 0
      number_of_letters = 0
      for letter in self.body:
         if letter.isupper():
            upper_cases += 1
         if letter.isalpha():
            number_of_letters += 1
      if (upper_cases == 1 and number_of_letters == 1):
         percentage = 1
      else:
         percentage = round((upper_cases / number_of_letters) * 100)
      return percentage
   def __str__(self):
      recipients = ', '.join(self.recipients)
      return f'From: {self.sender}\nTo: {recipients}\nSubject: {self.subject}\n{self.body}'


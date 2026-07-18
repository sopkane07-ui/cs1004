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
   def __str__(self):
      recipients = ', '.join(self.recipients)
      return f'From: {self.sender}\nTo: {recipients}\nSubject: {self.subject}\n{self.body}'


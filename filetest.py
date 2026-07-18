#!/usr/bin/env python3

from file_092 import File

def main():
   f = File('secrets.txt')
   print(f)
   print()

   f.add_line('John likes Mary')
   f.add_line('Mary likes John')
   print(f)
   print()

"""
   f.add_permission('Vera', 'w')
   f.del_permission('Vera', 'r') # No effect
   f.add_permission('Sean', 'r')
   f.add_permission('Sean', 'w')
   f.del_permission('Liam', 'r') # No effect
   print(f)
   print()

   f.del_permission('Sean', 'w')
   f.del_permission('Vera', 'w')
   print(f)
   print()

   assert(f.can_read('Sean'))
   assert(not f.can_read('Vera'))
   assert(not f.can_write('Vera'))
   assert(not f.can_read('Joey'))
"""

if __name__ == '__main__':
   main()

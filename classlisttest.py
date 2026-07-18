#!/usr/bin/env python3

from classlist_v1_131 import Student, Classlist

def main():

   cl = Classlist()
   s1 = Student('Boris Spassky', 25345654, ['DC121'])
   s2 = Student('Bobby Fischer', 25907321, ['DC121'])

   cl.add(s1)
   cl.add(s2)

   s = cl.lookup(25345654)
   assert(isinstance(s, Student))
   assert(s.name == 'Boris Spassky')
   assert(s.cao == 25345654)
   assert(s.prefs == ['DC121'])

   cl.remove(25345654)
   s = cl.lookup(25345654)
   assert(s is None)

if __name__ == '__main__':
   main()

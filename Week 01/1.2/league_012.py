#!/usr/bin/env python3
"""
import sys

clubs = []
remain = []

for line in sys.stdin:
   line = line.strip()
   i = 0
   while i < len(line) and not line[i].isalpha():
      i = i + 1
   j = i
   while j < len(line) and (line[j].isalpha() or line[j] == " " or line[j] == "&"):
      j = j + 1
   clubs.append(line[i:j])
   remain.append(line[j:])

clublen = len(max(clubs, key=len))

print("POS CLUB" + " " * (clublen - 3) + "P   W   D   L  GF  GA  GD PTS") #*tokens[-8:] a list
#* splits the tokenst
pos = 1

for i in range(len(clubs)):
   tokens = remain[i].split()
   print(f"{pos:3d}" + " " + f"{clubs[i]:{clublen}s}" + f"{tokens[0]:3s} " + f"{tokens[1]:>2s}  " + f"{tokens[2]:>2s}  " + f"{tokens[3]:>2s}  " + f"{tokens[4]:>2s}  " + f"{tokens[5]:>2s} " + f"{tokens[6]:>3s} " + f"{tokens[7]:>3s}")
   pos = pos + 1

#tokens[1:-8] is the football club
#" ".join(tokens)



lines = '1 Arsenal 16 14 1 1 40 14 26 43', '10 Brighton & Hove Albion 16 7 3 6 28 24 4 24', '2 Manchester City 16 11 3 2 44 16 28 36', '3 Newcastle United 17 9 7 1 32 11 21 34', '4 Manchester United 16 10 2 4 24 20 4 32'
print("POS CLUB                     P   W   D   L  GF  GA  GD PTS")

#to get the width
longest = 0
for line in lines:
   line = line.strip()
   if len(line) > longest:
      longest = len(line)

for l in lines:
   l = l.split()
   POS = (f'{l[0]:{""}>3}')
   print(POS)
"""

import sys
lines = sys.stdin.readlines()

rows = []
maxclubwidth = 0

for line in lines:
    tokens = line.split()
    pos = tokens[0]
    numericfields = tokens[-8:]
    p, w, d, l, gf, ga, gd, pts = numericfields
    club = " ".join(tokens[1:-8])
    if len(club) > maxclubwidth:
        maxclubwidth = len(club)

    rows.append((pos, club, p, w, d, l, gf, ga, gd, pts))

print(
     f"{'POS':>3} "
     f"{'CLUB':<{maxclubwidth}} "
     f"{'P':>2} {'W':>2} {'D':>2} {'L':>2} "
     f"{'GF':>2} {'GA':>2} "
     f"{'GD':>3} {'PTS':>3}"
)

for pos, club, p, w, d, l, gf, ga, gd, pts in rows:
      print(
       f"{pos:>3} "
       f"{club:<{maxclubwidth}} "
       f"{p:>2} {w:>2} {d:>2} {l:>2} "
       f"{gf:>2} {ga:>2} "
       f"{gd:>3} {pts:>3}"
   )











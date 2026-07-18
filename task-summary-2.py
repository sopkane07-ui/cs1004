#!/usr/bin/env python3

import sys

tasks = {}
users = []
line = sys.stdin.readline().rstrip()

while len(line) > 0:
   tokens = line.split("/")
   correct = line.split(".")
   if tokens[0] not in tasks:
      tasks[tokens[0]] = 0
   if "correct" == correct[-1]:
      tasks[tokens[0]] = tasks[tokens[0]] + 1
   line = sys.stdin.readline().rstrip()
for user in tasks:
   print(user + " " + str(tasks[user]))

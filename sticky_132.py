import sys

typed = sys.stdin.readline().rstrip()
shown = sys.stdin.readline().rstrip()

sticky = set()

for i in range(len(shown) - 1):
   if shown[i] == shown[i + 1]:
      sticky.add(shown[i])

print("".join(sorted(sticky)))

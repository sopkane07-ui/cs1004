import sys

def main():

   nums = sorted(list(map(int, sys.stdin.readline().split())))
   letters = ['A', 'B', 'C', 'D', 'E', 'F']
   values = dict(zip(letters, nums))
   order = sys.stdin.readline().strip()
   o = []
   for ord in order:
      o.append(ord)
   result = [str(values[ch]) for ch in order]
   print(" ".join(result))


if __name__ == "__main__":
   main()

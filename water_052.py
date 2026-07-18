#!/usr/bin/env python3

import sys

def max_water(heights):
   left = 0
   right = len(heights) - 1
   max_area = 0

   while left < right:
      width = right - left
      height = min(heights[left], heights[right])
      area = width * height
      max_area = max(max_area, area)

# Move the pointer at the shorter line inward
      if heights[left] < heights[right]:
         left += 1
      else:
         right -= 1

   return max_area

def main():
   line = sys.stdin.readline().strip()
   heights = list(map(int, line.split()))
   print(max_water(heights))

if __name__ == "__main__":
   main()

#!/usr/bin/env python3

weight = int(input())
height = int(input())

bmi = weight / (height * height) * 1000
if bmi >= 30:
   print("obese")
elif bmi == 25 and bmi < 29.9:
   print("overweight")
elif bmi == 18.5 and bmi < 24.9:
   print("normal")
else:
   print("underweight")

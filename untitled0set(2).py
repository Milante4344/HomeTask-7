# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IOOI3mhE3G8MRzSdqkzEdVSYxFq_bYjY
"""

x = int(input())
x1 = []
for xx in range(x):
  x2 = int(input())
  x1.append(x2)
set1 = set(x1)

z = int(input())
z1 = []
for zz in range(z):
  z2 = int(input())
  z1.append(z2)
set2 = set(z1)

S = set1.intersection(set2)

S2 = 0

for i in range(len(S)):
  S2+=1
print(S2)


from airSpace import*
from graph import*
from path import*
""" ===========================================================================================
Program to test the airspace classes
"""
A = buildAirSpace("Cat")
L = buildAirGraf(A)
Plot(L)
A = input("Dime el nodo(En mayúscula):")
PlotNode(L, A)

B = input("Dime el nodo 1 (En mayúscula):")
C= input("Dime el nodo 2 (En mayúscula):")
P = FindShortestPath(L,B, C)
if P:
  print("Path found:", [n.name for n in P.nodes])
  print("Total cost:", P.cost)
  PlotPath(L, P)
else:
  print("No path found.")
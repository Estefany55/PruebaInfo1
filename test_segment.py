from segment import *

n1 = Node("A", 1, 20)
n2 = Node("B", 8, 17)
n3 = Node("C", 16, 21)
segment = Segment(n1,n2)
print(f"Origin:{segment.origin_node.name}")
print(f"Destination: {segment.destination_node.name}")
print(f"Cost: {segment.cost}")

segment2 = Segment(n2,n3)
print(f"Origin:{segment2.origin_node.name}")
print(f"Destination: {segment2.destination_node.name}")
print(f"Cost: {segment2.cost}")
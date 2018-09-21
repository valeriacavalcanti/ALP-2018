# Avaliação 2
# Questão 4

import math

ax, ay = input().split(" ")
bx, by = input().split(" ")
cx, cy = input().split(" ")

ax, ay = int(ax), int(ay)
bx, by = int(bx), int(by)
cx, cy = int(cx), int(cy)

ab = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
bc = math.sqrt((bx - cx) ** 2 + (by - cy) ** 2)

area = (ab * bc) / 2

print("%.2f m2" % area)

from math import tan
from math import radians
import math
dis = 20
kakudo = radians(32)
hight = dis * tan(kakudo)
hight = math.floor(hight * 100) / 100
print(str(hight) + "m")

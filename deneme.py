import math
import random
from ball import *
for i in range(20):
	angle = random.uniform(0, 2*math.pi)
	print(math.cos(angle), math.sin(angle))

import math

print("Degree\t\tSin\t\tCos")

for i in range(361)[::10]:
    cos = math.cos(math.radians(i))
    sin = math.sin(math.radians(i))
    
    print(i,"\t\t",\
          format(cos, "6.4f"),"\t", \
          format(sin, "6.4f"))
    

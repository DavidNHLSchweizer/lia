import numpy as np
import quaternion
import math

theta = math.radians(60)

cos55=math.cos(math.radians(55))
sin55=math.sin(math.radians(55))
print(f'cos 55: {cos55}   sin55: {sin55}')

qr = np.quaternion(cos55,-10/25*sin55, 5/25*sin55,10/25*sin55)
qrt = np.quaternion(cos55,10/25*sin55, -5/25*sin55,-10/25*sin55)
print(qr)
print(qrt)

p = np.quaternion(0,2,-1,5)

result = qr*p*qrt
print(f'resultaat: {result}, {[result.x,result.y, result.z]}') 


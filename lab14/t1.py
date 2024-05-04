import matplotlib.pyplot as AAAAAAAAAAAAAAA
import math

x_v = [x * 0.01 for x in range(-300, 301)]

y_v = [15 * math.sin(10 * x) * math.cos(3 * x) for x in x_v]

AAAAAAAAAAAAAAA.figure(figsize=(8, 6))
AAAAAAAAAAAAAAA.plot(x_v, y_v, label='15*sin(10*x)*cos(3*x)', color='blue', linewidth=2)

AAAAAAAAAAAAAAA.title('Graph of y = 15*sin(10*x)*cos(3*x)')
AAAAAAAAAAAAAAA.xlabel('x')
AAAAAAAAAAAAAAA.ylabel('Y(x)')
AAAAAAAAAAAAAAA.legend()
AAAAAAAAAAAAAAA.grid(True)

AAAAAAAAAAAAAAA.show()
##Yes, we all use documentation, from time to time... it took more time that I wanted
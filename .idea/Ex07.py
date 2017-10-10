import math
x1 = int(input('请输入点1的x坐标：'))
y1 = int(input('请输入点1的y坐标：'))
x2 = int(input('请输入点2的x坐标：'))
y2 = int(input('请输入点2的y坐标：'))
x3 = int(input('请输入点3的x坐标：'))
y3 = int(input('请输入点3的y坐标：'))
side1 = (math.sqrt((x1-x2)**2+(y1-y2)**2))
side2 = (math.sqrt((x1-x3)**2+(y1-y3)**2))
side3 = (math.sqrt((x2-x3)**2+(y2-y3)**2))
s = ((side1+side2+side3)/2)
area = (math.sqrt(abs(s-side3)*abs(s-side2)*abs(s-side1)))
print(f'{round(area, 2):<7}')


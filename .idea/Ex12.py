import time
s = time.time()
d = s/3600/24
d2 = s//86400
h = (d-d2)*24
print("当前距离1970年1月1日过去了",round(d),"天",round(h),"时")

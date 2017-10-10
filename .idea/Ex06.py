a = int(input("请输入一个三位整数："))
num1 = a//100 #获取百位数
num2 = a%100//10 #获取十位数
num3 = a%10 #获取个位数
num = f'{num1+num2+num3:>4}'
print(num)
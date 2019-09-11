#  F=1.8C + 32
#  C = (F-32) / 1.8
F =  float(input('亲，请输入华氏度，我们将帮你转化为摄氏度'))
C = (F - 32) / 1.8
print('%.2f  摄氏度' %C)

 # PS C:\Users\Administrator> & E:/anaconda/python.exe e:/day01.py
 # 亲，请输入华氏度，我们将帮你转化为摄氏度60
 # 15.56  摄氏度


Number = input('请输入一个数字:')
bai = int(Number[0])
shi = int(Number[1])
ge = int(Number[2])
if bai **3 + shi **3 + ge **3 == int(Number):
    print('是水仙花')
else:
    print('不是水仙花')
    
 # PS C:\Users\Administrator> & E:/anaconda/python.exe c:/Users/Administrator/Desktop/Day01/day01.py
# 请输入一个数字:802
# 不是水仙花



F = float(input('请输入英尺数，我们将帮你转化为米数'))
C = F * 0.305
print('%.2f 米' %C)
 # PS C:\Users\Administrator> & E:/anaconda/python.exe e:/day01.py
 # 请输入英尺数，我们将帮你转化为米数100
 # 30.50 米



r = float(input('请输入圆柱的半径,我们将算出圆的表面积'))
l = float(input('请输入圆柱的高，我们将输出圆柱的体积'))
a = r * r * 3.14
v = a * l
print('%.2f  圆的表面积' %a)
print('%.2f  圆柱的体积' %v)
 # PS C:\Users\Administrator> & E:/anaconda/python.exe e:/day01.py
 # 请输入圆柱的半径,我们将算出圆的表面积6
 # 请输入圆柱的高，我们将输出圆柱的体积5
 # 113.04  圆的表面积
 # 565.20  圆柱的体积



M = float(input('请输入水的千克数'))
f = float(input('请输入水的最终温度'))
i = float(input('请输入水的初始温度'))
Q = M * (f - i) * 4184
print('%.2f  总共所需的能量' %Q)
 # PS C:\Users\Administrator> & E:/anaconda/python.exe e:/day01.py
 # 请输入水的千克数20
 # 请输入水的最终温度20
 # 请输入水的初始温度10
 # 836800.00  总共所需的能量



x = float(input('请输入差额'))
n = float(input('请输入年利率'))
l = x * (n / 1200) 
print('%.2f  利息' %l)
 # PS C:\Users\Administrator> & E:/anaconda/python.exe e:/day01.py
 # 请输入差额5000
 # 请输入年利率60
 # 250.00  利息



v0 = float(input('请输入初始速度'))
v1 = float(input('请输入末速度'))
t = float (input('请输入变化的时间'))
a = (v1 - v0) / t
print('%.2f 平均加速度' %a)
 # PS C:\Users\Administrator> & E:/anaconda/python.exe e:/day01.py
 #请输入初始速度200
 #请输入末速度300
 #请输入变化的时间30
 #3.33 平均加速度



c = float(input('请输入每月的存款'))
z = c + c * (0.05 / 12)*6
print('%.2f 账户总额' %z)
 
 # PS C:\Users\Administrator> & E:/anaconda/python.exe e:/day01.py
 # 请输入每月的存款6000
 #6150.00 账户总额


num = int(input("Enter a number between 0 and 1000："))
if num < 0 and num > 1000:
    print('输入有误')
else:
    a = int(num % 100)
    b = a % 10 # 百位数
    c = int(a / 10) # 十位数
    d = int(num / 100) # 个位数
    sum = b + c + d
print('The sum of the digits is %d'%sum)
 
 # PS C:\Users\Administrator> & E:/anaconda/python.exe e:/day01.py
 # Enter a number between 0 and 1000：663
 # The sum of the digits is 15

 ""
if condition:
        xxxx  
    else:
        xxxx
""
username =input ('请输入用户名')
password = input('请输入密码')
if username =="admin"and password = '123456':
    print('身份验证成功！')
else:
     ('身份验证失败！')







